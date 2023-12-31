from matsuri import app
from flask import render_template, request, Flask

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/form')
def form():
    return render_template('form.html')

@app.route('/result', methods=['POST', 'GET'])
def result():
    if(request.method == 'POST'):
        data = request.form
        return render_template('result.html', data=data)
    else:
        return render_template('getresult.html')

@app.route('/program')
def program():
    return render_template('program.html')