# kitchen-crate

Private Sammlung: Rezepte, Substitution, alles rund ums Kochen/Backen.
Startet als reines Markdown, wächst mit Bedarf.

## Struktur

- `rezepte/` - alles gleichrangig: komplette Gerichte, Teile (Teig, Füllung,
  Sauce) und "Kombi"-Dateien, die andere Dateien im selben Ordner
  referenzieren statt sie zu duplizieren. `_vorlage.md` kopieren zum Anlegen.
- `substitution.md` - Zutat X fehlt? Was ersetzt sie, in welchem Verhältnis

## Rezept anlegen

```
cp rezepte/_vorlage.md rezepte/dein-rezept-name.md
```

Dateiname = Rezeptname, klein, mit Bindestrichen.

Regeln:
- Jedes Rezept nennt, wie viel es ergibt ("Portionen" bzw. "Reicht für").
- Teile, die von anderen Rezepten genutzt werden, führen unten "Verwendet in:".
- Ungetestete Ideen werden als solche markiert, nicht als Fakt.

## Wachstumspfad (nicht jetzt bauen, nur damit klar ist wohin)

- Bilder: `rezepte/bilder/<rezept-name>/` sobald das erste Rezept eins braucht
- Web/App: liest später einfach die Markdown-Dateien hier, kein Datenmodell-Wechsel nötig
