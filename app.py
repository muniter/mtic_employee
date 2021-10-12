from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
    return render_template('index.html')

@app.route("/user")
def user():
    data = {"title": "Usuario"}
    return render_template('user.html')

@app.route("/employee")
def employee():
    return render_template('employee.html')

@app.route("/employee-report")
def report():
    return render_template('employee-report.html')
