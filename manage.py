import os
from flask_wtf.csrf import CsrfProtect

from app import create_app


config_name = os.getenv('FLASK_CONFIG')
app = create_app(config_name)


if __name__ == '__main__':
    #SECRET_KEY = 'the random string'
    CsrfProtect(app)
    app.run(debug=True)
  
