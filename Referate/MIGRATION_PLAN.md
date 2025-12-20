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

## Fortschritts-Tracker (Phase 2)

| Unit | Thema | Status | Fehlende Komponenten |
| :--- | :--- | :--- | :--- |
| **01** | Lineare Regression | ✅ Fertig | - |
| **02** | Logistische Regression | ✅ Fertig | - |
| **03** | Softmax & Multiclass | ✅ Fertig | - |
| **04** | Regularisierung (L1/L2) | ✅ Fertig | - |
| **05** | Optimierung (Adam etc.) | ✅ Fertig | - |
| **06** | CNN Basics | ✅ Fertig | - |
| **07** | Attention / Transformer | ✅ Fertig | - |
| **08** | Bias-Variance | ✅ Fertig | - |
| **09** | Ensembling | ✅ Fertig | (Referenz-Implementierung) |

## Phase 3: Integration (Zukunft)

1.  **Build-Prozess**: `build_book.py` erstellt ein Gesamt-Skript (`BOOK.md`) aus allen Units. ✅
2.  **CI/CD**: GitHub Action für automatische PDF-Generierung eingerichtet. ✅
3.  **QA & Community**: `CONTRIBUTING.md` und Unit-Tests (`tests/test_labs.py`) erstellt. ✅
4.  **Verlinkung**: Die Einheiten werden im Haupt-Curriculum (Woche 01-07) als "Deep Dives" verlinkt.
    *   *Beispiel:* Unit 09 (Ensembling) wird in Woche 04 (Advanced Algos) referenziert.

## Checkliste für neue Einheiten

- [ ] **Lernziele definiert?** (Was kann der Student danach?)
- [ ] **Theorie-Teil:** Slides + Skript vorhanden?
- [ ] **Praxis-Teil:** Lab-Notebook mit Lückentext-Code oder Aufgaben?
- [ ] **Visualisierung:** Streamlit-App oder interaktive Plots?
- [ ] **Self-Check:** Quizfragen am Ende des Skripts?

---
*Status: Migration abgeschlossen. Alle Units (01-09) sind erstellt, CI/CD ist eingerichtet. Bereit für Integration ins Haupt-Curriculum.*