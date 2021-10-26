PROJECT_BASE=$(shell pwd)
dev-run:
	(source $(PROJECT_BASE)/.venv/bin/activate)
	(FLASK_ENV=development FLASK_APP=app flask run)
initdb:
	(source $(PROJECT_BASE)/.venv/bin/activate)
	rm -rf app.db
	(FLASK_ENV=development FLASK_APP=app flask fab create-db)
initdata:
	(source $(PROJECT_BASE)/.venv/bin/activate)
	rm -rf app.db
	(FLASK_ENV=development FLASK_APP=app flask initdata)
prod-init:
	rm -rf app.db
	(flask fab create-db)
	(flask initdata)
prod-run:
	(gunicorn app:app --bind 0.0.0.0:5000)

all: initdb initdata dev-run
