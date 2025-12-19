# Prüfungsleistung: Referat

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

**Themenliste:**
1. Lineare Regression & MSE
2. Logistische Regression (Sigmoid + Cross‑Entropy)
3. Softmax + Cross‑Entropy (Multiklassen)
4. Regularisierung (L1 vs L2)
5. Optimierung: Gradient Descent, Momentum, Adam
6. CNN Basics (Convolution Shapes + Pooling)
7. Scaled Dot‑Product Attention (Transformer‑Kern)
8. Bias–Variance Decomposition

**Hinweise pro Thema (was thematisch ins Referat muss):**

- **Lineare Regression & MSE:** Herleitung des Modells und der MSE, analytische Lösung vs. numerische Optimierung, Kurven/Plots (Fit + Residuen), ein kurzes Datenset‑Demo und ein kleines Code‑Beispiel zum Fitten.

- **Logistische Regression (Sigmoid + Cross‑Entropy):** Sigmoid‑Funktion und Likelihood‑Argumentation, Ableitung der Cross‑Entropy, Entscheidungsgrenzen visualisieren, Binary‑Demo mit Confusion‑Matrix und kurzer Trainings‑Code.

- **Softmax + Cross‑Entropy (Multiklassen):** Softmax‑Formel und numerische Stabilität (log‑sum‑exp), Multiklassen‑Loss, kleine Multiclass‑Demo (Accuracy) und Beispielcode für Forward/Loss.

- **Regularisierung (L1 vs L2):** Regularisierungsziel formulieren, geometrische Intuition (Sparsity vs Shrinkage), Vergleichseffekt auf Koeffizienten, kurzer CV‑Test zur Wahl von Lambda und Demo‑Plots.

- **Optimierung: Gradient Descent, Momentum, Adam:** Update‑Regeln zeigen, Lernraten‑Effekte, Konvergenzkurven, Vergleichsplots verschiedener Optimierer, kleines Experiment zur Wahl des Lernrates.

- **CNN Basics (Convolution Shapes + Pooling):** Faltungsoperation erklären, Ausgabedimensionen (Kernel/Stride/Padding) herleiten, receptive field kurz erklären, Beispiel‑Layer durchrechnen und ein Visual‑Demo (z. B. Feature‑Maps).

- **Scaled Dot‑Product Attention:** Q/K/V‑Notation und Formel (inkl. Skalierung), Intuition für Attention‑Scores, Visualisierung von Attention‑Gewichten, kurzes Mini‑Beispiel (Transformer‑Block‑Sketch).

- **Bias–Variance Decomposition:** Zerlegung des Erwartungsfehlers erklären, illustrative Plots (Bias vs Variance), Beispiele durch Variation der Modellkomplexität und kurz Maßnahmen zur Reduktion (Regularisierung, Ensemble).

**Abgabe & Support:**
- Abgabe erfolgt per Commit/Pull in dieses Repository unter `Referate/<Dein_Thema>/` bis zum auf der Kursplattform genannten Datum.
- Fragen oder Probleme: erstellt ein Issue im Kurs‑Repo.

Viel Erfolg — denk an klare Visualisierungen und ein kompaktes, aussagekräftiges Handout!

---
**Musterbeispiel (zur Orientierung)**

Als konkretes Muster habe ich das Thema **`09_Ensembling`** umgesetzt, damit du ein vollständiges, korrektes Einreichungsbeispiel zum Ansehen und Kopieren hast. Die Implementierung findest du unter `Referate/09_Ensembling/` und enthält:

- `slides/` — ausgearbeitete Folienstruktur (`slides.md`, ≤12 Folien).
- `notes/handout.md` und `notes/handout.pdf` — vollständiges 4‑Seiten‑Handout mit Formeln, Experimentbeschrieb und Empfehlungen.
- `code/demo.ipynb` — ausführliches Notebook (EDA, Training, 5‑fold CV, Feature Importances, Learning Curve); ausgeführte Kopie: `code/executed_demo.ipynb`.
- `code/demo_run.py` — skriptfähige Version zur headless Ausführung (erzeugt Plots und `code/results.txt`).
- `code/requirements.txt` — benötigte Pakete (inkl. `scikit-learn`, `seaborn`).
- `assets/` — generierte PNGs: `feature_importances.png`, `learning_curve_rf.png`.
