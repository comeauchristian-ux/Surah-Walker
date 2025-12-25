import json
from pathlib import Path

IN_PATH = Path("data/quran-uthmani.txt")
OUT_PATH = Path("data/quran-uthmani.json")

def main():
    # Structure:
    # quran[surah_number] = list of ayah objects
    # each ayah: {"ayah": 1, "text": "...", "words": ["...","..."]}
    quran = {}

    for line in IN_PATH.read_text(encoding="utf-8").splitlines():
        line = line.strip()
        if not line:
            continue

        # Expected format: surah|ayah|text
        parts = line.split("|", 2)
        if len(parts) != 3:
            raise ValueError(f"Unexpected line format: {line[:80]}...")

        s = int(parts[0])
        a = int(parts[1])
        text = parts[2].strip()

        # Very simple tokenization for now (whitespace)
        # Later you can refine for punctuation/waqf signs.
        words = text.split()

        quran.setdefault(str(s), []).append({
            "ayah": a,
            "text": text,
            "words": words
        })

    OUT_PATH.write_text(
        json.dumps(quran, ensure_ascii=False, separators=(",", ":")),
        encoding="utf-8"
    )
    print(f"Wrote {OUT_PATH} with {len(quran)} surahs")

if __name__ == "__main__":
    main()
