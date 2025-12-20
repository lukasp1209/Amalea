# Mitmachen bei den Deep Learning Units

Wir freuen uns über Beiträge! Dieses Repository lebt davon, dass wir die Materialien gemeinsam verbessern. Egal ob Fehlerkorrekturen, neue Visualisierungen oder komplett neue Einheiten.

## Wie kann ich beitragen?

1.  **Fehler melden**: Erstelle ein Issue, wenn du einen mathematischen Fehler oder einen Bug im Code findest.
2.  **Verbesserungen einreichen**: Forke das Repo, mache deine Änderungen und erstelle einen Pull Request (PR).

## Struktur einer Unit

Jede neue Einheit muss zwingend folgende Ordnerstruktur einhalten, damit unser Build-System (`build_book.py`) funktioniert:

```text
XX_Thema_Name/
├── README.md           # Einstieg & Anleitung
├── requirements.txt    # Python-Abhängigkeiten
├── notes/
│   └── script.md       # Ausführliches Skript (wird Teil des Buchs)
├── slides/
│   └── lecture.md      # Folien für den Vortrag
└── code/
    ├── lab.py          # Interaktives Skript / Experimente
    └── app.py          # (Optional) Streamlit App
```

## Checkliste für Pull Requests

Bevor du einen PR einreichst, prüfe bitte:

- [ ] **Lauffähigkeit**: Lässt sich `lab.py` ohne Fehler ausführen?
- [ ] **Dependencies**: Sind alle neuen Libraries in `requirements.txt`?
- [ ] **Tests**: Laufen die Tests durch? (siehe unten)
- [ ] **Verständlichkeit**: Sind die Kommentare im Code hilfreich für Anfänger?

## Tests ausführen

Wir haben eine kleine Test-Suite, um sicherzustellen, dass die Kern-Algorithmen (Softmax, Gradienten etc.) korrekt sind.

```bash
# Im Hauptverzeichnis (Referate/)
python -m unittest tests/test_labs.py
```

Vielen Dank für deine Hilfe!