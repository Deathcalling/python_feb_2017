from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def homePage():
    return render_template('index.html')

@app.route('/ninjas')
def ninjas():
    return render_template('ninjas.html')

@app.route('/dojos/newform')
def form():
    return render_template('dojos.html')

app.run(debug=True)
