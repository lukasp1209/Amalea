# Vorlesungsskript: Attention & Transformer

## 1. Rückblick: Sequenzverarbeitung vor 2017
Früher nutzte man RNNs (Recurrent Neural Networks). Diese verarbeiten Wort für Wort sequenziell.
*   **Problem 1 (Bottleneck):** Der gesamte Inhalt des Satzes muss in einen einzigen Vektor ("Hidden State") gepresst werden. Bei langen Sätzen geht Information verloren.
*   **Problem 2 (Speed):** Man kann Wort 10 erst berechnen, wenn Wort 9 fertig ist. Keine Parallelisierung auf GPUs möglich.

## 2. Die Idee von Attention
Statt nur den letzten Zustand zu nutzen, erlauben wir dem Modell, auf **alle** vorherigen Zustände zuzugreifen.
Es berechnet für jeden Output eine Gewichtung: "Wie wichtig ist Input-Wort $j$ für Output-Wort $i$?"

## 3. Self-Attention (Der Kern des Transformers)
Self-Attention wendet dieses Prinzip auf den Satz selbst an. Jedes Wort schaut auf jedes andere Wort im gleichen Satz, um seinen Kontext zu verstehen.

### Die Metapher: Datenbank-Suche
Für jedes Wort erstellen wir drei Vektoren:
1.  **Query ($Q$):** Wonach suche ich? (z.B. "Ich bin ein Pronomen, worauf beziehe ich mich?")
2.  **Key ($K$):** Was biete ich an? (z.B. "Ich bin ein Substantiv, männlich.")
3.  **Value ($V$):** Was ist mein Inhalt? (Die eigentliche Wortbedeutung).

### Die Formel (Scaled Dot-Product Attention)
$$ \text{Attention}(Q, K, V) = \text{softmax}\left(\frac{QK^T}{\sqrt{d_k}}\right) V $$

1.  $QK^T$: Berechnet die Ähnlichkeit (Dot Product) zwischen meiner Suche ($Q$) und allen Angeboten ($K$).
2.  $\text{softmax}$: Wandelt die Scores in Wahrscheinlichkeiten um (Summe = 1). Das sind die **Attention Weights**.
3.  $\cdot V$: Wir berechnen den gewichteten Durchschnitt der Inhalte ($V$).

## 4. Multi-Head Attention
Ein einziger Attention-Mechanismus reicht oft nicht. Ein "Head" achtet vielleicht auf Grammatik, ein anderer auf semantische Bezüge.
Deshalb nutzen Transformer mehrere Heads parallel und konkatenieren die Ergebnisse.

## 5. Positional Encoding
Da der Transformer alle Wörter gleichzeitig sieht (keine Sequenz), weiß er nicht, ob "Mann beißt Hund" oder "Hund beißt Mann" gemeint ist.
Lösung: Wir addieren zu jedem Wortvektor ein Muster, das die Position codiert (Sinus/Cosinus-Wellen verschiedener Frequenzen).

## 6. Architektur-Überblick (GPT vs. BERT)
*   **Encoder-Only (z.B. BERT):** Sieht den ganzen Satz (links und rechts). Gut für Klassifikation, Sentiment.
*   **Decoder-Only (z.B. GPT):** Sieht nur, was bisher geschah (maskierte Attention). Gut für Textgenerierung.
*   **Encoder-Decoder (z.B. T5, Original Transformer):** Gut für Übersetzung.

## 7. Übungsaufgabe (`code/lab.py`)
Wir simulieren Self-Attention mit NumPy:
1.  Wir definieren Dummy-Embeddings für 4 Wörter.
2.  Wir berechnen die Attention-Scores.
3.  Wir visualisieren, welches Wort auf welches andere "achtet".