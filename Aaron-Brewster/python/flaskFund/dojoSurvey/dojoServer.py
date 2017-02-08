from flask import Flask, render_template, request, redirect

app = Flask(__name__)

@app.route('/')
def form():
    return render_template('form.html')

@app.route('/result', methods=['post'])
def result():

    name = request.form['name']
    language = request.form['language']
    dojo = request.form['dojo']
    comment = request.form['comment']

    return render_template('result.html', name=name, language=language, dojo=dojo, comment=comment)

app.run(debug=True)
