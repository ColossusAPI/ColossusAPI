from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('base.html')

@app.route('/sprint')
def sprint():
    return render_template('sprint.html')

@app.route('/po')
def po():
    return render_template('po.html')

@app.route('/importancia')
def imp():
    return render_template('importancia.html')

@app.route('/productbacklog')
def pbacklog():
    return render_template('productbacklog.html')

@app.route('/sm')
def sm():
    return render_template('sm.html')

@app.route('/equipe')
def equipe():
    return render_template('equipe.html')

app.run(debug=True)