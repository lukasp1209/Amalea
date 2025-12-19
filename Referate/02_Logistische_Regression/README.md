# Cross-Entropy Loss

Formel:

$$\mathcal{L}_{\text{CE}} = -\frac{1}{N} \sum_{i=1}^N \big[ y_i \log \hat{y}_i + (1-y_i) \log(1-\hat{y}_i) \big]$$

Kurz: Loss für Klassifikation; straft sehr sichere Fehlvorhersagen stark.