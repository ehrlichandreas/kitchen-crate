#!/usr/bin/env python3
"""Fotos für ein Rezept ins Repo übernehmen.

    python3 bilder.py <rezept-name> foto1.jpg [foto2.jpg ...]

Legt die Bilder unter rezepte/bilder/<rezept-name>/ ab, verkleinert auf
1200 px (längste Seite, JPEG-Qualität 75) und entfernt alle Metadaten
(EXIF, GPS, Kommentare). Gibt den Markdown-Schnipsel zum Einfügen aus.

Braucht macOS (sips) und sonst nur die Standardbibliothek.
"""
import pathlib
import struct
import subprocess
import sys

ROOT = pathlib.Path(__file__).resolve().parent
MAX_PX = 1200
QUALITY = 75


def strip_metadata(path):
    """Alle APP1..APP15- und COM-Segmente aus einem JPEG entfernen, Bilddaten bleiben."""
    b = path.read_bytes()
    if b[:2] != b"\xff\xd8":
        sys.exit(f"{path}: kein JPEG")
    out = bytearray(b[:2])
    i = 2
    while i < len(b):
        if b[i] != 0xFF:
            sys.exit(f"{path}: JPEG-Struktur unerwartet an Byte {i}")
        marker = b[i + 1]
        if marker == 0xDA:  # Start of Scan: Rest sind Bilddaten
            out += b[i:]
            break
        length = struct.unpack(">H", b[i + 2:i + 4])[0]
        if not (0xE1 <= marker <= 0xEF or marker == 0xFE):
            out += b[i:i + 2 + length]
        i += 2 + length
    path.write_bytes(bytes(out))
    if b"Exif" in out or b"GPS" in out:
        sys.exit(f"{path}: Metadaten nicht vollständig entfernt")


def main(argv):
    if len(argv) < 3:
        sys.exit(__doc__)
    rezept, fotos = argv[1], argv[2:]
    if not (ROOT / "rezepte" / f"{rezept}.md").exists():
        sys.exit(f"rezepte/{rezept}.md gibt es nicht")
    ziel = ROOT / "rezepte" / "bilder" / rezept
    ziel.mkdir(parents=True, exist_ok=True)
    vorhanden = len(list(ziel.glob("*.jpg")))
    zeilen = []
    for n, src in enumerate(fotos, start=vorhanden + 1):
        src = pathlib.Path(src)
        if not src.exists():
            sys.exit(f"{src}: nicht gefunden")
        dst = ziel / f"{rezept}-{n:02d}.jpg"
        subprocess.run(
            ["sips", "-Z", str(MAX_PX), "-s", "format", "jpeg",
             "-s", "formatOptions", str(QUALITY), str(src), "--out", str(dst)],
            check=True, capture_output=True,
        )
        strip_metadata(dst)
        kb = dst.stat().st_size // 1024
        print(f"{dst.relative_to(ROOT)}  {kb} KB, ohne Metadaten", file=sys.stderr)
        zeilen.append(f"![Beschreibung](bilder/{rezept}/{dst.name})")
    print("\nIn rezepte/" + rezept + ".md einfügen und Beschreibung ersetzen:\n", file=sys.stderr)
    print("\n".join(zeilen))


if __name__ == "__main__":
    main(sys.argv)
