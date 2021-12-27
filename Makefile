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
test tests:
	. .venv/bin/activate
	PYTHONPATH=src pytest tests
