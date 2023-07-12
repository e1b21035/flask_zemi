from flask_zemi import app
from flask import render_template, request, Flask

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/form')
def form():
    name = "Test"
    return render_template('form.html')

@app.route('/result', methods=["POST"])
def result():
    data = request.form
    return render_template('result.html', data=data)
