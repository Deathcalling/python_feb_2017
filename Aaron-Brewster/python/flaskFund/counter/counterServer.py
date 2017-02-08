from flask import Flask, render_template, request, redirect, session

app = Flask(__name__)
app.secret_key = 'pooperdooper'

@app.route('/', methods=['get', 'post'])
def counter():
    if 'count' not in session:
        session['count'] = 0
    else:
        session['count'] += 1

    if 'ninja' in request.form:
        session['count'] += 1
    elif 'hacker' in request.form:
        session['count'] = 1

    return render_template('counter.html')

app.run(debug=True)
