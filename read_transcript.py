from pathlib import Path

transcript_path = Path("transcript.txt")
text = transcript_path.read_text(encoding="utf-8")

lines = text.splitlines()

print("Characters:", len(text))
print("Lines:", len(lines))
print("First line:", lines[0])