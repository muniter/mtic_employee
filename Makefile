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

all: initdb initdata dev-run
