from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
    return render_template('index.html')

@app.route("/user")
def user():
    data = {"title": "Usuario"}
    return render_template('form_view.html')

@app.route("/employee-report")
def employee():
    data = {"title": "Empleados"}
    return f"<p>Hello, employee!</p>"

@app.route("/reports")
@app.route("/reports/<int:id>")
def report(id):
    data = {"title": "Reportes"}
    return f"<p>Hello, report {id}!</p>"
