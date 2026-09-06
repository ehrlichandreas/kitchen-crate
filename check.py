#!/usr/bin/env python3
"""Prüft die Sammlung. Exit 1, wenn etwas nicht stimmt.

- Jeder Verweis auf eine .md-Datei ist ein echter Link, und das Ziel existiert.
- Jedes eingebundene Bild existiert; Bilder unter rezepte/bilder/ sind klein und ohne Metadaten.
- Jedes Rezept nennt seine Menge (Portionen / Reicht für / Ergibt).
- Jedes Rezept steht in der README-Übersicht.
- "Verwendet in:" stimmt in beide Richtungen.
- Keine Gedankenstriche, nur einfacher Bindestrich.

Nur Standardbibliothek: python3 check.py
"""
import re
import sys
import pathlib

ROOT = pathlib.Path(__file__).resolve().parent
RZ = ROOT / "rezepte"
TEMPLATE = "_vorlage.md"

files = {p.name: p.read_text(encoding="utf-8") for p in RZ.glob("*.md")}
readme = (ROOT / "README.md").read_text(encoding="utf-8")
names = sorted(set(files) | {"substitution.md"}, key=len, reverse=True)
ref = re.compile(r"(?:\.\./|rezepte/)?(" + "|".join(map(re.escape, names)) + r")")
errors = []


def check_links(path, txt):
    in_code = False
    for ln, line in enumerate(txt.splitlines(), 1):
        if line.startswith("```"):
            in_code = not in_code
            continue
        if in_code:
            continue
        for m in ref.finditer(line):
            a, b = m.start(), m.end()
            as_text = line[max(0, a - 2):a] == "[`" and line[b:b + 2] == "`]"
            as_target = line[a - 1:a] == "(" and line[b:b + 1] == ")"
            if not (as_text or as_target):
                errors.append(f"{path.relative_to(ROOT)}:{ln}: Verweis ist kein Link: {m.group(0)}")
    for t in re.findall(r"\]\(([^)]+\.md)\)", txt):
        if not (path.parent / t).exists():
            errors.append(f"{path.relative_to(ROOT)}: Linkziel fehlt: {t}")
    for t in re.findall(r"!\[[^\]]*\]\(([^)]+)\)", txt):
        if not (path.parent / t).exists():
            errors.append(f"{path.relative_to(ROOT)}: Bild fehlt: {t}")


for p in sorted(RZ.glob("*.md")):
    check_links(p, files[p.name])
for p in (ROOT / "README.md", ROOT / "substitution.md"):
    check_links(p, p.read_text(encoding="utf-8"))

DASHES = ("\u2014", "\u2013")
for p in sorted(RZ.glob("*.md")) + [ROOT / "README.md", ROOT / "substitution.md"]:
    for ln, line in enumerate(p.read_text(encoding="utf-8").splitlines(), 1):
        if any(d in line for d in DASHES):
            errors.append(f"{p.relative_to(ROOT)}:{ln}: Gedankenstrich, bitte einfacher Bindestrich")

for name, txt in files.items():
    if name == TEMPLATE:
        continue
    if not re.search(r"\*\*(Portionen|Reicht für):\*\*|^## Reicht für|Ergibt \*\*", txt, re.M):
        errors.append(f"rezepte/{name}: keine Mengenangabe (Portionen / Reicht für)")
    if f"rezepte/{name}" not in readme:
        errors.append(f"rezepte/{name}: fehlt in der README-Übersicht")

for name, txt in files.items():
    m = re.search(r"^Verwendet in:(.*)$", txt, re.M)
    if not m:
        continue
    listed = set(re.findall(r"\(([^)]+\.md)\)", m.group(1)))
    body = txt.replace(m.group(0), "")
    linked_by_me = set(re.findall(r"\]\(([^)]+\.md)\)", body))
    users = {
        other for other, t in files.items()
        if other != name and f"({name})" in t and other not in linked_by_me
    }
    if listed != users:
        errors.append(
            f"rezepte/{name}: 'Verwendet in' sagt {sorted(listed) or '-'}, "
            f"verlinkt wird es aber von {sorted(users) or '-'}"
        )

for img in sorted((RZ / "bilder").rglob("*.jpg")):
    data = img.read_bytes()
    if b"Exif" in data or b"GPS" in data:
        errors.append(f"{img.relative_to(ROOT)}: enthält Metadaten (EXIF/GPS) - mit bilder.py aufnehmen")
    if len(data) > 400_000:
        errors.append(f"{img.relative_to(ROOT)}: {len(data)//1024} KB, zu groß - mit bilder.py verkleinern")

if errors:
    print("\n".join(errors))
    print(f"\n{len(errors)} Problem(e).")
    sys.exit(1)
print(f"ok: {len(files)} Rezepte, README, Substitution geprüft.")
