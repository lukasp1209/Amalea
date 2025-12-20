.PHONY: help install run test clean docker-build docker-run

help: ## Zeige diese Hilfe an
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-20s\033[0m %s\n", $$1, $$2}'

install: ## Installiere alle Abhängigkeiten
	pip install -r requirements.txt

run: ## Starte die Übungs-App
	streamlit run uebungs_app.py

run-components: ## Starte die Komponenten-Übersicht
	streamlit run streamlit_komponenten.py

run-first: ## Starte die erste App
	streamlit run meine_erste_app.py

test: ## Führe Tests aus (falls vorhanden)
	python -m pytest tests/ -v

clean: ## Räume temporäre Dateien auf
	find . -type f -name "*.pyc" -delete
	find . -type d -name "__pycache__" -delete
	rm -rf .pytest_cache/

docker-build: ## Baue Docker-Image
	docker build -t amalea-week1 .

docker-run: ## Starte Container
	docker run -p 8501:8501 amalea-week1

docker-compose-up: ## Starte mit docker-compose
	docker-compose up --build

jupyter: ## Starte Jupyter Lab
	jupyter lab