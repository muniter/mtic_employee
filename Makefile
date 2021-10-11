PROJECT_BASE=$(shell pwd)
dev:
	(source $(PROJECT_BASE)/.venv/bin/activate)
	(FLASK_ENV=development FLASK_APP=app flask run)
