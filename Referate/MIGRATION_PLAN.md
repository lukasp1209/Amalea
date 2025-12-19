# Migrationsplan: Referate → Vorlesungseinheiten

**Status Quo:** Ordner `Referate/` enthält studentische Prüfungsleistungen (kurz, strikte Limits, Fokus auf Vortrag).
**Zielzustand:** Ordner `Vorlesungseinheiten/` (oder `Modules/`) enthält tiefgehende Lehrmaterialien (ausführlich, didaktisch, Fokus auf Verständnis & Übung).

## Phase 1: Umbenennung & Struktur (Sofort)

1.  **Rename**: Der Ordner `Referate/` wird logisch in `Vorlesungseinheiten/` umbenannt (im Repo vorerst als `Referate` belassen, aber inhaltlich geändert).
2.  **Index**: Die `README.md` wird von einer Prüfungsordnung zu einem Modulkatalog umgeschrieben.
3.  **Cleanup**: Entfernen aller Bewertungsschemata und Abgabefristen.

## Phase 2: Konvertierung der Inhalte (Laufend)

Für jedes bestehende Thema (1-9) gilt folgender Transformationsprozess:

| Artefakt | Alt (Referat) | Neu (Vorlesungseinheit) | Aktion |
| :--- | :--- | :--- | :--- |
| **Slides** | `slides.md` (max. 12 Folien) | `lecture.md` (Umfassend) | Limits aufheben, Erklärfolien ergänzen. |
| **Text** | `handout.pdf` (max. 4 Seiten) | `script.md` (Skript) | Formeln herleiten, Exkurse erlauben. |
| **Code** | `demo.ipynb` (Showcase) | `lab.ipynb` (Interaktiv) | Übungsaufgaben ("Your Turn") einfügen. |
| **App** | Optional | Pflicht | Interaktive Streamlit-App zur Visualisierung. |

## Phase 3: Integration (Zukunft)

1.  **Verlinkung**: Die Einheiten werden im Haupt-Curriculum (Woche 01-07) als "Deep Dives" verlinkt.
    *   *Beispiel:* Unit 09 (Ensembling) wird in Woche 04 (Advanced Algos) referenziert.
2.  **Build-Prozess**: Automatische Generierung von PDF-Skripten aus den Markdown-Notes mittels Pandoc/Quarto.

## Checkliste für neue Einheiten

- [ ] **Lernziele definiert?** (Was kann der Student danach?)
- [ ] **Theorie-Teil:** Slides + Skript vorhanden?
- [ ] **Praxis-Teil:** Lab-Notebook mit Lückentext-Code oder Aufgaben?
- [ ] **Visualisierung:** Streamlit-App oder interaktive Plots?
- [ ] **Self-Check:** Quizfragen am Ende des Skripts?

---
*Status: Phase 1 abgeschlossen. Migriert: Unit 09 (Ensembling), Unit 01 (LinReg & MSE).*