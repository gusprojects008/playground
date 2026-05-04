import srt
from pathlib import Path
from TTS.api import TTS
from deep_translator import GoogleTranslator
import subprocess
import os
import argparse
import tempfile
from cli_core.files import new_file_path

def get_duration(file):
    result = subprocess.run(
        ["ffprobe", "-v", "error", "-show_entries", "format=duration",
         "-of", "default=noprint_wrappers=1:nokey=1", file],
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True
    )
    return float(result.stdout.strip())

def build_atempo_filter(speed):
    filters = []
    while speed > 2.0:
        filters.append("atempo=2.0")
        speed /= 2.0
    while speed < 0.5:
        filters.append("atempo=0.5")
        speed /= 0.5
    filters.append(f"atempo={speed}")
    return ",".join(filters)

def subtitle_transcriptor(input_subtitle: Path, source_lang: str, target_lang: str, output_audio: Path = None):
    audio_output = new_file_path(output_audio, "output.wav")

    with open(input_subtitle, "r", encoding="utf-8") as f:
        subs = list(srt.parse(f.read()))

    tts = TTS(model_name="tts_models/pt/cv/vits")
    translator = GoogleTranslator(source=source_lang, target=target_lang)

    segments = []
    
    with tempfile.TemporaryDirectory() as temp_dir:
        for i, sub in enumerate(subs):
            translated = translator.translate(sub.content)
            audio_file = os.path.join(temp_dir, f"seg_{i}.wav")

            tts.tts_to_file(text=translated, file_path=audio_file)

            start = sub.start.total_seconds()
            segments.append((start, audio_file))

        inputs = []
        filters = []

        for i, (start, file) in enumerate(segments):
            inputs += ["-i", file]
            delay = int(start * 1000)
            filters.append(f"[{i}:a]adelay={delay}|{delay}[a{i}]")

        mix = "".join(f"[a{i}]" for i in range(len(segments)))
        
        filter_complex = ";".join(filters) + f";{mix}amix=inputs={len(segments)}:duration=longest:normalize=0"

        cmd = ["ffmpeg", "-y", *inputs, "-filter_complex", filter_complex, str(audio_output)]
        
        try:
            subprocess.run(cmd, check=True, stdout=subprocess.DEVNULL, stderr=subprocess.STDOUT)
            print(f"Áudio final gerado com sucesso em: {audio_output}")
        except subprocess.CalledProcessError as e:
            print(f"Erro ao processar áudio com FFmpeg: {e}")

def parse_args():
    parser = argparse.ArgumentParser()

    parser.add_argument("--input", "-i", required=True, type=Path)
    parser.add_argument("--output", "-o", type=Path)
    parser.add_argument("--source-lang", required=True)
    parser.add_argument("--target-lang", required=True)

    return parser.parse_args()

def main():
    args = parse_args()
    subtitle_transcriptor(
        args.input,
        args.source_lang,
        args.target_lang,
        args.output
    )

if __name__ == "__main__":
    main()

