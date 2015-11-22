"""
Routes and views for the flask application.
"""

from datetime import datetime
from flask import render_template, request, Flask
from FlaskWebProject import app

from FlaskWebProject.tokens import *
from FlaskWebProject.helper import *


@app.route('/')
def my_form():
	return render_template("my-form.html")
	
@app.route('/', methods=['POST'])
def my_form_post():
	text = request.form['text']
	wav = get_raw_wav(text)
	return render_template(
		'index.html',
		title = 'New Phrase',
		wavfile = wav
	)