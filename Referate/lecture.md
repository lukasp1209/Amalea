% Vorlesung Unit 07: Attention & Transformer

Slide 1: "Attention Is All You Need"
- Paper von Google (2017).
- Löste RNNs/LSTMs ab.
- Basis für ChatGPT, BERT, Claude, etc.

Slide 2: Das Problem mit RNNs
- Sequenziell: Langsam auf GPUs.
- Vergesslich: "The cat ... [100 words] ... was hungry." RNN vergisst "cat".
- Attention löst das durch direkten Zugriff auf alle Wörter.

Slide 3: Self-Attention Intuition
- Satz: "Das Tier überquerte die Straße nicht, weil **es** zu müde war."
- Worauf bezieht sich "**es**"?
- Self-Attention verbindet "es" stark mit "Tier" (und nicht mit "Straße").

Slide 4: Q, K, V - Die Mechanik
- Query (Suchanfrage): Was brauche ich?
- Key (Index): Passt das zu mir?
- Value (Inhalt): Die Information.
- Score = Query * Key.

Slide 5: Transformer Block
- Input -> Self-Attention -> Feed Forward Network.
- Add & Norm (Residual Connections) dazwischen.
- Stackable: GPT-3 hat 96 solcher Layer.

Slide 6: Positional Encoding
- Transformer hat keinen Sinn für Reihenfolge.
- Wir müssen die Position (Index 1, 2, 3...) explizit in die Daten codieren.
- Meist durch Addition von Sinus-Wellen zum Embedding.