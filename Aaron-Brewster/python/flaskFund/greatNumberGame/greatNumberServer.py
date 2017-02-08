from flask import Flask, render_template, session, request
import random

app = Flask(__name__)
app.secret_key = 'pooperdooper'

@app.route('/')
def numberGame():

	if 'button' in request.args:
		if request.args['button'] == 'Try again...':
			session.clear()

	h = ''
	w = False
	guess = None

	if 'n' not in session:
		session['n'] = random.randint(1, 100)

	if 'guess' in request.args:
		guess = int(request.args['guess'])
		if session['n'] == guess:
			h = 'Good Jeeoooorrrrbb, perhaps you can make it to a hospital in time... Oh what the heck... I\'ll just keep you!'
			w = True
		elif session['n'] < guess:
			h = 'Lower... Oh... That had to hurt!'
		else:
			h = 'Higher... Weeeellll I wouldn\'t miss that if I were you'
	else:
		h = 'Guess a number, before I tear out your lungs!'

	return render_template('greatNumber.html', h=h, w=w, guess=guess)

app.run(debug=True)
