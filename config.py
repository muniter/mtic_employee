import os

basedir = os.path.abspath(os.path.dirname(__file__))

CSRF_ENABLED = True
SECRET_KEY = "shh"

SQLALCHEMY_DATABASE_URI = "sqlite:///" + os.path.join(basedir, "app.db")
# SQLALCHEMY_DATABASE_URI = 'mysql://myapp@localhost/myapp'

BABEL_DEFAULT_LOCALE = "en"
# ------------------------------
# GLOBALS FOR GENERAL APP's
# ------------------------------
UPLOAD_FOLDER = basedir + "/app/static/uploads/"
IMG_UPLOAD_FOLDER = basedir + "/app/static/uploads/"
IMG_UPLOAD_URL = "/static/uploads/"
IMG_SIZE = (150, 150, True)
AUTH_TYPE = 1
AUTH_ROLE_ADMIN = "Sudo"
AUTH_ROLE_PUBLIC = "Public"
APP_NAME = "MisionTIC Employee"
USER_MODELS = ["Employee", "EmployeeReport", "Department", "JobTitle"]
USER_MODELS_REGEX = f'({"|".join(USER_MODELS)})'
FAB_ROLES = {
    "User": [
        [USER_MODELS_REGEX, "can_list"],
        [USER_MODELS_REGEX, "can_show"],
        [USER_MODELS_REGEX, "menu_access"],
        [USER_MODELS_REGEX, "can_get"],
        [USER_MODELS_REGEX, "can_info"]
    ],
    "Admin": [
        [".*", "can_list"],
        [".*", "can_show"],
        [".*", "menu_access"],
        [".*", "can_get"],
        [".*", "can_info"]
    ]
}
# APP_THEME = ""  # default
# APP_THEME = "cerulean.css"      # COOL
# APP_THEME = "amelia.css"
# APP_THEME = "cosmo.css"
# APP_THEME = "cyborg.css"       # COOL
# APP_THEME = "flatly.css"
# APP_THEME = "journal.css"
APP_THEME = "readable.css"
# APP_THEME = "simplex.css"
# APP_THEME = "slate.css"          # COOL
# APP_THEME = "spacelab.css"      # NICE
# APP_THEME = "united.css"
