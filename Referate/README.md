# Prüfungsleistung: Referat (Kurs)

**Ziel:**
- **Kurz:** Jede Person wählt ein Thema aus dem Ordner `Referate/`, bereitet ein kompaktes Fachreferat vor und reicht ein 4‑seitiges Handout ein.
- **Lernziel:** Fachliches Verständnis nachweisen, komplexe Inhalte didaktisch strukturiert erklären und ein kleines Demo/Code‑Beispiel vorführen.

**Aufgabe:**
- Wähle eines der unten aufgeführten Themen aus (oder stimme es mit der Lehrperson ab).
- Bereite einen Vortrag von **20 Minuten** vor; anschließend **5 Minuten** Fragen/Feedback.
- Erstelle ein **Handout (max. 4 A4‑Seiten, PDF)**, das die Kernaussagen, kurze Herleitungen/Formeln, ein Beispiel und weiterführende Hinweise enthält.
- Lege alle Materialien in diesem Repository ab: `Referate/<Dein_Thema>/` mit der erwarteten Unterstruktur (siehe unten).

**Erwartete Ablieferung (Dateinamen & Ort):**
- `Referate/<Dein_Thema>/slides/` → Präsentation (`slides.pdf` oder `slides.pptx`).
- `Referate/<Dein_Thema>/notes/` → Handout als `handout.pdf` (max. 4 Seiten) und optional `talk_notes.md`.
- `Referate/<Dein_Thema>/code/` → Minimal lauffähiges Demo‑Notebook `demo.ipynb` oder Script `demo.py` (kurze Anleitung in `README.md`).
- `Referate/<Dein_Thema>/assets/` → alle verwendeten Bilder/Plots.

Committe/Push deine finalen Dateien in dieses Repo unter dem genannten Pfad bis zum in der Kursplattform angegebenen Abgabezeitpunkt.

**Bewertung (Rubrik):**
- **Inhaltliche Korrektheit & Tiefe:** 40 % — fachliche Richtigkeit, angemessene Tiefe, korrekte Formeln.
- **Didaktik & Verständlichkeit:** 25 % — Struktur, Klarheit, Visualisierungen, passende Beispiele.
- **Präsentation:** 15 % — Zeitmanagement (20 min), Sprechweise, Umgang mit Fragen.
- **Handout (Format & Inhalt):** 10 % — prägnant, vollständig und als PDF.
- **Code/Demo:** 10 % — funktioniert, ist knapp dokumentiert und demonstriert den Punkt.

**Formale Vorgaben:**
- Vortrag: strikt **20 Minuten** (± 1 Minute), danach 5 Minuten Q&A.
- Handout: maximal **4 Seiten A4**, PDF; klare Quellenangaben bei Bildern/Formeln.
- Slides: empfehlenswert ≤ 12 Folien; gut lesbare Schrift und beschriftete Achsen in Plots.
- Code: kurz und reproduzierbar; wenn Abhängigkeiten nötig sind, ergänzt `requirements.txt` im Ordner `code/`.

**Ordnerstruktur (erwartet):**
- `slides/` — Präsentationsdateien (`slides.pdf`, `slides.pptx`).
- `notes/` — `handout.pdf`, optional `talk_notes.md`.
- `code/` — `demo.ipynb` oder `demo.py`, ggf. `requirements.txt`.
- `assets/` — Bilder, Plots, ergänzende Dateien.

**Themenliste (Empfohlenes kompaktes Set):**
1. Lineare Regression & MSE
2. Logistische Regression (Sigmoid + Cross‑Entropy)
3. Softmax + Cross‑Entropy (Multiklassen)
4. Regularisierung (L1 vs L2)
5. Optimierung: Gradient Descent, Momentum, Adam
6. CNN Basics (Convolution Shapes + Pooling)
7. Scaled Dot‑Product Attention (Transformer‑Kern)
8. Bias–Variance Decomposition

**Hinweis zu bereits existierenden Ordnern:**
- Es gibt aktuell mehrere bereits angelegte Ordner. Falls du ein Thema nutzt, benenne deinen Ordner bitte `Referate/<Dein_Thema>` oder erstelle einen neuen Ordner mit diesem Namen. Auf Wunsch fasse ich Ordner zusammen oder erstelle Starter‑Templates.

**Abgabe & Support:**
- Abgabe erfolgt per Commit/Pull in dieses Repository unter `Referate/<Dein_Thema>/` bis zum auf der Kursplattform genannten Datum.
- Fragen oder Probleme: erstellt ein Issue im Kurs‑Repo oder kontaktiert die Lehrperson/TA über die Kursplattform.

Viel Erfolg — denk an klare Visualisierungen und ein kompaktes, aussagekräftiges Handout!