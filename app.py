import main as m
from flask import Flask, render_template, redirect, request, url_for, jsonify, session
app = Flask(__name__)


@app.route('/')
def home():
    if request.method == 'GET':
        # number of questions
        n = 5
        result = m.p(5)
        return render_template('index.html', result=result)