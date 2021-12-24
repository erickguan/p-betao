.PHONY: env-update
env-update:
	. .venv/bin/activate
	pip install -r dev-requirements.txt

.PHONY: dep-update
dep-update:
	. .venv/bin/activate
	pip-compile requirements.in
	pip-compile dev-requirements.in

.PHONY: tests
test tests: seed
	. .venv/bin/activate
	PYTHONPATH=src pytest tests

.PHONY: seed
seed:
	. .venv/bin/activate
	rm -f discounts.db && python scripts/01_generate_mock.py
