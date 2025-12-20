# AMALEA 2025 - Data Analytics & Big Data

<div align="center">
  <img src="./kurs-logo.png" alt="AMALEA 2025 Logo" width="400">
</div>

## Kursbeschreibung

> **AMALEA** = **"Angewandte Machine Learning Algorithmen"**  
> Basiert auf dem erfolgreichen AMALEA-Programm des KI-Campus: [ki-campus.org/amalea](https://ki-campus.org/amalea)

### Überblick

AMALEA 2025 ist ein vollständig modernisierter, praxisorientierter Notebook-basierter Kurs für "Data Analytics" & "Machine Learning", der speziell für Informatik-Studierende der IU ab dem 5. Semester konzipiert wurde. Der Kurs baut auf dem bewährten **"Angewandte Machine Learning Algorithmen"** Programm des KI-Campus auf und erweitert es um moderne Deployment-Strategien, interaktive Web-Anwendungen und industrierelevante MLOps-Kompetenzen. Der Kurs kombiniert theoretische Grundlagen mit intensiver praktischer Anwendung und bereitet Studierende auf die Anforderungen der modernen Datenwissenschaft vor. Durch die Entwicklung von 18+ interaktiven Jupyter Notebooks und 16+ produktionsreifen Streamlit-Anwendungen (alle Wochen 01–07 production-ready; W06/W07 CPU-freundlich) erwerben die Teilnehmer nicht nur technische Kompetenzen, sondern erstellen gleichzeitig ein beeindruckendes Portfolio für ihre berufliche Laufbahn.

### Pädagogisches Konzept

Der Kurs folgt einem projektbasierten Lernansatz, bei dem jede Woche aufeinander aufbauende Kompetenzen vermittelt werden. Beginnend mit Python-Grundlagen und Datenmanipulation führt der Lernpfad systematisch zu fortgeschrittenen Machine Learning-Verfahren, Neural Networks und schließlich zu produktionsreifen Deployment-Strategien. Besonders innovativ ist die Integration von 22 originalen AMALEA-Videos aus dem Jahr 2021, die nahtlos in die modernisierten Notebooks eingebettet sind und bewährte theoretische Konzepte mit aktuellen praktischen Anwendungen verbinden.

Ein zentrales Merkmal des Kurses ist die Betonung auf echte, industrierelevante Projekte. Anstatt theoretische Übungen zu absolvieren, entwickeln die Studierenden von Beginn an funktionsfähige Web-Anwendungen, die echte Daten verarbeiten und für reale Nutzer zugänglich sind. Dieser Ansatz bereitet optimal auf die Anforderungen moderner Arbeitsplätze vor, wo Data Scientists nicht nur Algorithmen verstehen, sondern auch komplette End-to-End-Lösungen entwickeln müssen.

### Lernziele und Kompetenzen

Nach erfolgreichem Abschluss des Kurses verfügen die Studierenden über ein umfassendes Skillset, das sie unmittelbar in der Berufspraxis einsetzen können. Sie beherrschen Python für Data Science auf professionellem Niveau und können selbstständig Machine Learning-Pipelines von der Datenaufbereitung bis zum Deployment entwickeln. Besonders wertvoll ist ihre Fähigkeit, interaktive Web-Anwendungen mit Streamlit zu erstellen, die komplexe Datenanalysen für Nicht-Techniker zugänglich machen.

Die Teilnehmer lernen moderne Deep Learning-Frameworks wie TensorFlow und Keras kennen und können Neural Networks für Computer Vision und Natural Language Processing implementieren. Durch die intensive Arbeit mit aktuellen Bibliotheken wie Hugging Face Transformers sind sie mit den neuesten Entwicklungen im Bereich der künstlichen Intelligenz vertraut. Gleichzeitig erwerben sie praktische MLOps-Kompetenzen, die für die Skalierung von Machine Learning-Lösungen in Produktionsumgebungen essentiell sind. Im Deployment-Modul (W07) arbeiten sie mit einer FastAPI-Demo; die NLP-Endpunkte (Sentiment/QA/Generate) nutzen leichte Hugging Face Pipelines (DistilBERT/Tiny-GPT-2), sodass API-Design, Monitoring und Deployment realistisch erprobt werden können.

### Kursstruktur und Inhalte

Der siebenwöchige Kurs ist in aufeinander aufbauende Module gegliedert, die jeweils spezifische Lernziele verfolgen. Die erste Woche etabliert solide Python-Grundlagen und führt in die Arbeit mit Pandas für Datenmanipulation ein. Ein besonderes Highlight ist das "Python in 3 Stunden" Notebook, das auch für Quereinsteiger einen schnellen, aber gründlichen Einstieg ermöglicht.

Die zweite Woche konzentriert sich auf die Entwicklung interaktiver Web-Anwendungen mit Streamlit und vertieft die Datenanalyse-Kompetenzen. Hier erstellen die Studierenden ihre erste produktionsreife Anwendung und lernen dabei die Grundlagen des Web-Deployments kennen. Die dritte Woche führt systematisch in Machine Learning ein, wobei der Fokus auf praktischer Anwendung und der Integration von ML-Modellen in Web-Interfaces liegt.

Das absolute Highlight des Kurses ist die vierte Woche mit dem "Big 3" Notebook, das eine umfassende praktische Einführung in die drei wichtigsten Machine Learning-Algorithmen bietet: Decision Trees, K-Nearest Neighbors und K-Means Clustering. Dieses Modul verbindet theoretisches Verständnis mit intensiver praktischer Anwendung und bereitet optimal auf komplexere Algorithmen vor.

Die fünfte Woche taucht tief in Neural Networks und Deep Learning ein, während die sechste Woche Computer Vision und Natural Language Processing mit vier spezialisierten Notebooks (Runner: `run_cv_notebooks.sh`, Executed-Notebooks inklusive) und vier begleitenden Streamlit-Anwendungen/Dashboards behandelt. Die finale siebte Woche konzentriert sich auf Deployment, MLOps und Portfolio-Entwicklung mit FastAPI-Demo (NLP-Endpunkte via leichte HF-Pipelines für Sentiment/QA/Generate), zwei produktionsreifen Streamlit-Dashboards und drei kompakten Notebooks; die Studierenden üben API-Handling, Monitoring und Deployment.

**Repository-Organisation:** Alle Kursmaterialien sind systematisch strukturiert mit wochenspezifischen Ordnern (01_Python_Grundlagen/ bis 07_Deployment_Portfolio/). Executed Notebooks in `executed_notebooks/` bieten sofort einsatzbereite Referenzimplementierungen, während `datasets/` alle notwendigen Datensätze für praktische Übungen enthält. Vorlesungseinheiten in `Vorlesungseinheiten/` vertiefen theoretische Konzepte, und `tests/` gewährleistet Code-Qualität durch umfassende Test-Suiten.

### Aktuelle Kursstruktur im Detail (2025)

Der vollständig modernisierte Kurs umfasst **24 Portfolio-Komponenten** und ist in einem professionellen Repository mit modularer Struktur organisiert:

| Woche | Thema | Core Notebooks | Streamlit Apps | Fokus |
|-------|-------|----------------|----------------|--------|
| **01** | Python Grundlagen | 4 | 3 | Foundation + QUA³CK Framework + Docker |
| **02** | Streamlit & Pandas | 1 | 3 | Interactive Web Development |
| **03** | Machine Learning | 1 | 2 | ML Pipeline Development |
| **04** | Advanced Algorithms | 2 | 1 | Ensembles & Unsupervised, MLflow/DVC Intro |
| **05** | Neural Networks | 2+ | 1 | Keras Basics & Transfer Learning Lite |
| **06** | Computer Vision & NLP | 5+ | 4+ | CV/NLP Fundamentals + Augmentation/Transfer |
| **07** | Deployment & Portfolio | 3 | 2 | FastAPI + Monitoring Dashboards (HF-Pipelines) |

**Gesamt: 18+ Core Notebooks + 16+ Streamlit Apps = 34+ Portfolio-Komponenten**

**Zusätzliche Ressourcen:**
- **Executed Notebooks** (`executed_notebooks/`): Sofort einsatzbereite, ausführbare Versionen aller wichtigen Notebooks
- **Datasets** (`datasets/`): Alle Kurs-Datensätze für praktische Übungen
- **Vorlesungseinheiten** (`Vorlesungseinheiten/`): Vertiefende Vorlesungseinheiten zu theoretischen Konzepten
- **Tests** (`tests/`): Umfassende Test-Suite für Qualitätssicherung
- **Backup** (`BACKUP_Original_AMALEA_Notebooks/`): Original-Versionen für Vergleich

### QUA³CK Framework Integration

Alle Projekte folgen dem systematischen **QUA³CK Prozessmodell**:
- **Q**uestion: Business Problem Definition & Requirements Analysis
- **U**nderstand: Comprehensive Data Exploration & Statistical Analysis  
- **A**cquire & Clean: Professional Data Pipeline & ETL Development
- **A**nalyze: Machine Learning Model Development mit MLFlow Tracking
- **A**pp: Production-Ready Streamlit Cloud Deployment
- **C**onclusion & **K**ommunikation: Portfolio Documentation & Presentation

### Innovative Technologien und Tools

Der Kurs setzt konsequent auf moderne, industrierelevante Technologien. Python 3.11+ bildet das Fundament, ergänzt durch leistungsfähige Bibliotheken wie Pandas, NumPy und Scikit-learn für klassisches Machine Learning. Für Deep Learning kommen TensorFlow und Keras zum Einsatz, während Hugging Face Transformers den Zugang zu modernsten NLP-Modellen ermöglicht. Dependencies sind pro Woche getrennt (Week-Requirements + Lockfiles), damit Installationen schlank und reproduzierbar bleiben: leichter Stack (W01–W03), MLOps (W04), Deep Learning (W05), CV/NLP (W06), Deployment (W07).

Ein besonderer Fokus liegt auf Streamlit als Framework für die Entwicklung interaktiver Web-Anwendungen. Diese Technologie ermöglicht es Data Scientists, ihre Analysen ohne umfangreiche Web-Entwicklungskenntnisse in benutzerfreundliche Interfaces zu verwandeln. Docker containerisiert die gesamte Entwicklungsumgebung und gewährleistet Konsistenz und Reproduzierbarkeit across verschiedene Systeme. Mehrere Dockerfile-Varianten (jupyter, streamlit, slim/full) bieten Flexibilität für verschiedene Use-Cases.

Für das Experiment Tracking und MLOps kommt MLflow zum Einsatz, während Git und GitHub für Versionskontrolle und Collaboration sorgen. Die Visualisierung erfolgt mit modernen Bibliotheken wie Plotly und Matplotlib, die interaktive und publikationsreife Grafiken ermöglichen. Qualitätssicherung erfolgt durch pytest für Unit-Tests, ruff und black für Code-Qualität und -Formatierung, und ein umfassendes Makefile für automatisierte Workflows.

### ML/DL-Algorithmen und Demos pro Woche (Auswahl)

- **W01–W02 (Basics & Apps):** Deskriptive Statistik, Pandas-Transformationen, einfache Visualisierungen; Streamlit-Widgets zur Datenexploration.
- **W03 (Classic ML):** Scikit-Learn Pipelines, Logistische Regression & RandomForest für Klassifikation, Lineare Regression für Housing; Hyperparameter-Playgrounds in Streamlit.
- **W04 (Advanced/MLops):** Ensembles (RandomForest/GradientBoosting-Patterns), Clustering (K-Means), Anomalie-Detektion; MLflow/DVC-Einstieg.
- **W05 (Deep Learning):** Keras-Sequential/Functional API, Dense-Netze für Tabulardaten, leichtgewichtige Transfer-Learning-Setups.
- **W06 (CV/NLP):** CNN-Grundlagen, Edge/Feature-Extraction mit OpenCV, Data Augmentation, Transfer Learning Lite; Transformers-Demo für Text (CPU-freundlich).
- **W07 (Deployment):** FastAPI-Demo mit Sklearn-Iris-Modell; NLP-Endpunkte mit leichten HF-Pipelines (Sentiment/QA/Generate) für API/Monitoring/Deployment-Übungen; zwei Streamlit-Dashboards für Monitoring & NLP.

### Studienleistung

Die Studienleistung erfordert die Entwicklung einer vollständigen MLOps-Anwendung, die eine End-to-End Machine Learning Pipeline, eine interaktive Streamlit-Web-App und ein Live-Deployment in der Streamlit Cloud umfasst. Dieser Ansatz geht weit über traditionelle Klausuren hinaus und bewertet die Fähigkeit, komplette, produktionsreife Lösungen zu entwickeln.

Die Studierenden haben maximale Freiheit bei der Themenwahl und werden ermutigt, Projekte zu entwickeln, die ihre persönlichen Interessen widerspiegeln und als Vorstudie für ihr Bachelorprojekt dienen können. Zur Inspiration werden Beispiele aus verschiedenen Bereichen angeboten: Predictive Analytics für Immobilienpreise, Computer Vision für medizinische Bildanalyse, NLP für Social Media Sentiment Analysis oder Business Intelligence Dashboards für Sales Forecasting.

### Datenquellen und Praxisbezug

Ein wesentlicher Aspekt des Kurses ist die Arbeit mit echten, großen Datensätzen aus verschiedenen Domänen. Die Studierenden lernen, öffentlich verfügbare Big Data Quellen zu nutzen, darunter Kaggle Datasets mit Millionen von Datensätzen, Google Dataset Search für spezialisierte Datenquellen, AWS Open Data für Cloud-basierte Anwendungen und Regierungsdatenportale wie Data.gov und das European Data Portal.

Für Business-Anwendungen stehen APIs wie Yahoo Finance für Finanzdaten, World Bank Open Data für wirtschaftliche Analysen und IMF-Daten für internationale Statistiken zur Verfügung. Wissenschaftliche Projekte können auf das UCI Machine Learning Repository, Papers with Code Datasets oder NASA Open Data zugreifen. Social Media und Entertainment-Anwendungen nutzen MovieLens für Empfehlungssysteme, Spotify API für Musikanalysen oder Reddit API für Social Media Analytics.

### Portfolio-Entwicklung und Karrierevorbereitung

Ein zentrales Ziel des Kurses ist die Entwicklung eines beeindruckenden Portfolios, das die Studierenden direkt in Bewerbungsgesprächen einsetzen können. Die 34+ Portfolio-Komponenten (18+ Notebooks + 16+ Streamlit Apps) demonstrieren nicht nur technische Kompetenz, sondern zeigen auch die Fähigkeit, komplexe Probleme vollständig zu lösen und benutzerfreundliche Interfaces zu entwickeln.

Alle entwickelten Anwendungen sind produktionsreif und öffentlich zugänglich, was sie von typischen Studienarbeiten unterscheidet. Arbeitgeber können die Live-Apps direkt testen und sich von den praktischen Fähigkeiten der Bewerber überzeugen. Zusätzlich bieten die Executed Notebooks in `executed_notebooks/` sofort einsatzbereite Referenzimplementierungen, während die Vorlesungseinheiten in `Vorlesungseinheiten/` theoretische Konzepte vertiefen.

Diese Herangehensweise bereitet optimal auf moderne Data Science Rollen vor, wo die Fähigkeit zur Kommunikation und Präsentation von Ergebnissen genauso wichtig ist wie die technische Umsetzung. Die modulare Repository-Struktur mit professionellen Entwicklungstools (pytest, ruff, Makefile) vermittelt zudem Industriestandards für Code-Qualität und Projektmanagement.

### Technische Infrastruktur und Support

Die gesamte Kursinfrastruktur ist vollständig dockerisiert und ermöglicht eine einheitliche Entwicklungsumgebung für alle Teilnehmer. Mit einem einzigen `docker-compose up` Kommando wird eine vollständige Data Science Workbench gestartet, die Jupyter Notebooks (Port 8888), Streamlit-Entwicklung (Port 8501) und MLflow für Experiment Tracking (Port 5001) umfasst. Zusätzlich stehen Slim-Varianten für ressourcenschonende Entwicklung zur Verfügung.

Das Repository ist modular strukturiert mit wochenspezifischen Requirements-Dateien für effiziente Installationen. Ein umfassendes Makefile automatisiert Build-, Test- und Formatierungsprozesse, während pytest und ruff für Qualitätssicherung sorgen. Executed Notebooks in `executed_notebooks/` bieten sofortige Referenzimplementierungen, und `datasets/` enthält alle Kurs-Datensätze für praktische Übungen.

Für Studierende, die lokale Installationen bevorzugen, ist eine detaillierte Anleitung mit allen erforderlichen Dependencies verfügbar. Ein umfassendes Troubleshooting-Kapitel behandelt häufige Probleme und deren Lösungen, während zusätzliche Ressourcen und Links zu offizieller Dokumentation bei der Vertiefung spezifischer Themen helfen. Die `Vorlesungseinheiten/` enthalten vertiefende Vorlesungseinheiten zu theoretischen Konzepten, und `tests/` bietet eine vollständige Test-Suite für Qualitätssicherung.

### Integration originaler AMALEA-Inhalte

Ein besonderer Wert wird auf die Kontinuität zu den bewährten originalen AMALEA-Inhalten gelegt. Alle 22 Videos aus dem Jahr 2021 sind strategisch in die modernisierten Notebooks integriert und bieten solide theoretische Grundlagen, die durch aktuelle praktische Anwendungen ergänzt werden. Diese Kombination gewährleistet, dass bewährte pädagogische Konzepte erhalten bleiben, während gleichzeitig modernste Technologien und Methoden vermittelt werden.

### Zukunftsorientierung und Industrie-Relevanz

AMALEA 2025 ist konsequent auf die Anforderungen der modernen Datenökonomie ausgerichtet. Die vermittelten Technologien und Methoden entsprechen dem aktuellen Industriestandard und bereiten die Studierenden auf gefragte Rollen wie Data Scientist, ML Engineer, oder Data Product Manager vor. Durch die Betonung auf End-to-End-Lösungen und Deployment-Kompetenzen sind die Absolventen in der Lage, sofort produktiv zu arbeiten und echten Business Value zu schaffen.

Der Kurs bereitet auch optimal auf weiterführende Studien vor, insbesondere für Masterstudiengänge im Bereich Data Science, Artificial Intelligence oder Machine Learning. Die erworbenen Kompetenzen in MLOps und Cloud-Deployment sind essentiell für fortgeschrittene Forschungsprojekte und industrielle Kooperationen.

---

*AMALEA 2025 verbindet bewährte pädagogische Konzepte mit modernster Technologie und bereitet eine neue Generation von Data Scientists vor, die nicht nur Algorithmen verstehen, sondern komplette, produktionsreife Lösungen entwickeln können, die echten Impact in der digitalen Wirtschaft erzielen. Mit 34+ Portfolio-Komponenten (18+ Notebooks + 16+ Apps), modularer Repository-Struktur und professionellen Entwicklungstools ist der Kurs optimal für moderne Data Science Karrieren ausgerichtet.*
