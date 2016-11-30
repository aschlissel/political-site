from flask import Flask, render_template, request, jsonify
import pandas as pd
import os
from datetime import datetime

app = Flask(__name__)

df = pd.read_csv('justices.csv')
df.start = [datetime.strptime(x, '%Y-%m-%d') for x in df.start] 
df.end = [datetime.strptime(x, '%Y-%m-%d') for x in df.end] 

@app.route('/')
def index():
	return render_template('index.html')

@app.route('/justices')
def justices():
	justices = []
	year = request.args.get('year', 0, type=int)
	for i, row in df.iterrows():
		if row.start.year <= year <= row.end.year:
			justices.append(row.justice)
	return jsonify(result=year, justices=justices)


if __name__ == '__main__':
    app.debug= True
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)