"""Build beats.json (and a sentence-level .srt) from script.md.

A beat lasts its narration plus PAUSE seconds per [pause]: Speechify drops intra-clip silence,
so pauses are held frames, and explainer-compile pads the audio to the video. The narration
length is the ffprobe duration of audio/<Beat>.mp3 when it exists, else an estimate at WPM.

Run after editing script.md, and again after `speechify-tts --script beats.json`:
    python build_beats.py
Subtitles are rebuilt from the rendered beats with --srt <render dir> (each beat's span is
its real video length; cues split by sentence, timed by word share within the beat).
"""
import json, re, shutil, subprocess, sys, pathlib

# george measured 192-197 wpm over three Macro videos; 2.5 s per held pause (Macro convention)
WPM, PAUSE = 195, 2.5
here = pathlib.Path(__file__).parent


def probe(path):
    if not path.exists() or not shutil.which("ffprobe"):
        return None
    r = subprocess.run(["ffprobe", "-v", "error", "-show_entries", "format=duration",
                        "-of", "csv=p=0", str(path)], capture_output=True, text=True)
    try:
        return float(r.stdout.strip())
    except ValueError:
        return None


def parse():
    src = (here / "script.md").read_text(encoding="utf-8")
    for m in re.finditer(r"^## (Beat\w+) - (\d+) s\n(.*?)(?=^## |\Z)", src, re.M | re.S):
        bid, budget, body = m.group(1), int(m.group(2)), m.group(3)
        text = re.sub(r"\s+", " ", body.replace("[pause]", " ")).strip()
        yield bid, budget, body.count("[pause]"), text


def build():
    path = here / "beats.json"
    voice = json.loads(path.read_text(encoding="utf-8")).get("voice") if path.exists() else None
    beats = []
    for bid, budget, pauses, text in parse():
        audio = here / "audio" / f"{bid}.mp3"
        measured = probe(audio)
        narration = measured if measured else len(text.split()) / WPM * 60
        beats.append(dict(id=bid, text=text, audio=f"audio/{bid}.mp3",
                          seconds=round(narration + pauses * PAUSE, 3),
                          narration_seconds=round(narration, 3),
                          narration_measured=bool(measured),
                          budget_seconds=budget, pauses=pauses))
    out = dict(voice=voice, total_seconds=round(sum(b["seconds"] for b in beats), 3), beats=beats)
    path.write_text(json.dumps(out, indent=2, ensure_ascii=False), encoding="utf-8")
    for b in beats:
        print(f"{b['id']:24s} {b['seconds']:7.1f} s  ({b['pauses']} pauses, budget {b['budget_seconds']})")
    print(f"{len(beats)} beats, {out['total_seconds'] / 60:.1f} min")


def srt(render_dir):
    def stamp(t):
        ms = int(round(t * 1000))
        h, ms = divmod(ms, 3_600_000); m, ms = divmod(ms, 60_000); s, ms = divmod(ms, 1000)
        return f"{h:02d}:{m:02d}:{s:02d},{ms:03d}"
    manifest = json.loads((here / "beats.json").read_text(encoding="utf-8"))
    cues, clock = [], 0.0
    for b in manifest["beats"]:
        span = probe(pathlib.Path(render_dir) / f"{b['id']}.mp4") or b["seconds"]
        sentences = re.findall(r"[^.!?]+[.!?]+[\"”’]?|[^.!?]+$", b["text"])
        words = [len(s.split()) for s in sentences]
        speech = b["narration_seconds"] / sum(words)   # pauses are silent, at no fixed place
        t = clock
        for s, w in zip(sentences, words):
            cues.append((t, min(t + w * speech, clock + span), s.strip()))
            t += w * speech
        clock += span
    lines = []
    for i, (a, z, s) in enumerate(cues, 1):
        lines += [str(i), f"{stamp(a)} --> {stamp(z)}", s, ""]
    out = here / f"{here.name}.srt"
    out.write_text("\n".join(lines), encoding="utf-8")
    print(f"{len(cues)} cues, {clock / 60:.1f} min -> {out.name}")


if __name__ == "__main__":
    if len(sys.argv) == 3 and sys.argv[1] == "--srt":
        srt(sys.argv[2])
    else:
        build()
