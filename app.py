from flask import Flask, render_template, request, jsonify
import pandas as pd
import os

app = Flask(__name__)

names = pd.read_csv('justices.csv')

@app.route('/')
def index():
	return render_template('index.html')

@app.route('/justices')
def justices():
	year = request.args.get('year', 0, type=int)
	return jsonify(result=year)


if __name__ == '__main__':
    app.debug= True
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)