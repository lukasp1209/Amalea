.PHONY: install lint fmt test smoke-notebooks

PYTHON ?= python
PYTHONPATH := $(PWD)/07_Deployment_Portfolio
SMOKE_NOTEBOOKS := \
	07_Deployment_Portfolio/01_MLOps_und_Deployment.ipynb \
	07_Deployment_Portfolio/02_NLP_und_Text_Generation.ipynb \
	07_Deployment_Portfolio/03_QUA3CK_MLOps_Integration.ipynb

install:
	$(PYTHON) -m pip install -r requirements-dev.txt -c requirements-07.lock.txt

lint:
	$(PYTHON) -m ruff check 07_Deployment_Portfolio tests --exclude "*.ipynb"

fmt:
	$(PYTHON) -m black 07_Deployment_Portfolio || true

test:
	PYTHONPATH=$(PYTHONPATH) $(PYTHON) -m pytest -q

smoke-notebooks:
	@for nb in $(SMOKE_NOTEBOOKS); do \
		name=$$(basename $$nb .ipynb); \
		echo "[nbconvert] $$nb"; \
		$(PYTHON) -m nbconvert --to notebook --execute $$nb \
			--output $${name}-executed.ipynb \
			--output-dir 07_Deployment_Portfolio/executed \
			--ExecutePreprocessor.kernel_name=python3 \
			--ExecutePreprocessor.timeout=300 \
			--Application.log_level=ERROR; \
	done
