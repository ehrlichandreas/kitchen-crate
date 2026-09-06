# kitchen-crate

Rezeptsammlung in reinem Markdown, zum Nachbacken und Weitergeben.

## Übersicht

Allergene in Klammern: **G** Gluten, **E** Ei, **M** Milch, **N** Nüsse.
Laktosefrei ist nicht milchfrei.

**Gerichte / Kombis**

- [Zimtschnecken](rezepte/zimtschnecken.md) - Teig + Füllung + alle drei Saucen, skalierbar auf beliebige Stückzahl (G, E, M)
- [Zimtschnecken für die Arbeit](rezepte/zimtschnecken-fuer-die-arbeit.md) - Anlass-Plan: 27 + 6 laktosefrei, Ablauf, Einkaufsliste (G, E, M)
- [Zimtschnecken laktosefrei](rezepte/zimtschnecken-laktosefrei.md) - laktosefreier Teig, ohne Sauce (G, E, M laktosefrei)
- [Zimtschnecken mit Puddingcreme-Frischkäse-Frosting](rezepte/zimtschnecken-mit-puddingcreme-frischkaese-frosting.md) - einmal gebacken (G, E, M)
- [Zimtschnecken mit Pudding-Cheesecake-Frosting, 6 Stück](rezepte/zimtschnecken-pudding-cheesecake-frosting-6.md) - komplett ausgeschrieben, Probebacken mit Fotos und Befund (G, E, M)
- [Schokoschnecken](rezepte/schokoschnecken.md) - Hefeteig mit Schokotröpfchen statt Zimt, einmal gebacken (G, E, M)
- [Puddingschnecken](rezepte/puddingschnecken.md) - Hefeteig mit Puddingcreme als Füllung, ungetestet (G, E, M)
- [Chocolate-Chip-Macadamia-Cookies](rezepte/chocolate-chip-macadamia-cookies.md) - ca. 50 Stück (G, E, M, **N**)
- [Chocolate-Chip-Cookies nussfrei](rezepte/chocolate-chip-cookies-nussfrei.md) - Basis ohne Macadamia, ungetestet (G, E, M)

**Teile** (von den Kombis referenziert, funktionieren aber auch für sich)

- [Hefeteig-Grundrezept](rezepte/hefeteig-grundrezept.md) - 12 Stück, normal oder laktosefrei, mit Skalierungstabelle (G, E, M)
- [Zimt-Füllung](rezepte/fuellung-zimt.md) (M)
- [Schokotröpfchen-Füllung](rezepte/fuellung-schokotropfen.md) (M)
- [Vanillesauce](rezepte/sauce-vanille.md) (M, E)
- [Frischkäse-Frosting](rezepte/sauce-frischkaese-frosting.md) (M)
- [Karamellsauce](rezepte/sauce-karamell.md) (M)
- [Puddingcreme](rezepte/puddingcreme.md) (M, E)

**Nachschlagen**

- [Substitutionsliste](substitution.md) - Zutat fehlt? Was stattdessen geht, in welchem Verhältnis

Rezepte sind in Teile zerlegt (Teig, Füllung, Saucen), die für sich stehen.
Eine "Kombi"-Datei sagt, welche Teile in welcher Variante zusammengehören
und wo sie vom Basis-Rezept abweichen - so lassen sich neue Kombinationen
bauen, ohne Rezepte zu duplizieren. Mengen skalieren über einen Faktor
(Stückzahl ÷ 12), die Tabellen dazu stehen in den Teil-Rezepten.

## Struktur

- `rezepte/` - alles gleichrangig: komplette Gerichte, Teile (Teig, Füllung,
  Sauce) und "Kombi"-Dateien, die andere Dateien im selben Ordner
  referenzieren statt sie zu duplizieren. [`_vorlage.md`](rezepte/_vorlage.md) kopieren zum Anlegen.
- [`substitution.md`](substitution.md) - Zutat X fehlt? Was ersetzt sie, in welchem Verhältnis
- `rezepte/bilder/<rezept>/` - Fotos zu einem Rezept, auf 1200 px verkleinert, ohne Metadaten

## Rezept anlegen

```
cp rezepte/_vorlage.md rezepte/dein-rezept-name.md
```

Dateiname = Rezeptname, klein, mit Bindestrichen.

Regeln:
- Jedes Rezept nennt, wie viel es ergibt ("Portionen" bzw. "Reicht für").
- Teile, die von anderen Rezepten genutzt werden, führen unten "Verwendet in:".
- Ungetestete Ideen werden als solche markiert, nicht als Fakt.
- Neues Rezept = Eintrag in der Übersicht oben, sonst findet es niemand.
- `python3 check.py` prüft das alles mechanisch (Links, Mengen, Übersicht, Rückverweise, keine Gedankenstriche).

## Wachstumspfad (nicht jetzt bauen, nur damit klar ist wohin)

- Web/App: liest später einfach die Markdown-Dateien hier, kein Datenmodell-Wechsel nötig

## Lizenz

CC0 1.0 (siehe `LICENSE`, gilt auch für `check.py`): mach damit, was du
willst, ohne Nennung. Ohne Gewähr - die Rezepte sind privat entwickelt,
Mengen und Zeiten hängen von Ofen, Zutaten und Küche ab. Allergene stehen in
der Übersicht, was auf der Packung steht, prüft jeder selbst.
