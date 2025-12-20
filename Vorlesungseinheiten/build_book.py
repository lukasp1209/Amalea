import os

# Die Reihenfolge der Einheiten im Buch
UNITS = [
    "01_Lineare_Regression_MSE",
    "02_Logistische_Regression",
    "03_Softmax_Multiclass",
    "04_Regularisierung",
    "05_Optimierung",
    "06_CNN_Basics",
    "07_Attention",
    "08_Bias_Variance",
    "09_Ensembling",
]

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
OUTPUT_FILE = os.path.join(BASE_DIR, "BOOK.md")

def get_script_content(unit_folder):
    """Sucht nach script.md oder handout.md im notes-Ordner."""
    possible_files = ["script.md", "handout.md"]
    notes_dir = os.path.join(BASE_DIR, unit_folder, "notes")
    
    if not os.path.exists(notes_dir):
        return None, None

    for fname in possible_files:
        fpath = os.path.join(notes_dir, fname)
        if os.path.exists(fpath):
            with open(fpath, "r", encoding="utf-8") as f:
                return f.read(), fname
    return None, None

def main():
    full_content = []
    # Titelblatt
    full_content.append("# Deep Learning Lecture Notes\n\n")
    full_content.append("### Zusammenfassung der Vorlesungseinheiten\n\n")
    full_content.append("**Stand:** Heute\n\n")
    full_content.append("---\n\n")
    
    print(f"Erstelle Buch aus {len(UNITS)} Einheiten...")

    for unit in UNITS:
        content, fname = get_script_content(unit)
        if content:
            print(f"  + Füge hinzu: {unit} ({fname})")
            # Seitenumbruch für PDF-Generierung (Pandoc)
            full_content.append(f"\n\n<div style=\"page-break-after: always;\"></div>\n\n")
            full_content.append(content)
        else:
            print(f"  ! WARNUNG: Kein Skript gefunden für {unit}")

    with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
        f.write("".join(full_content))
    
    print(f"\nFertig! Datei erstellt: {OUTPUT_FILE}")
    print("PDF generieren mit: pandoc BOOK.md -o book.pdf --toc --pdf-engine=xelatex")

if __name__ == "__main__":
    main()