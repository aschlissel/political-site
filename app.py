import flask
import pandas as pd

app = flask.Flask(__name__)

names = pd.read_csv('justices.csv')

@app.route("/justices", methods = ["POST"])
def justices():
	data = flask.request.json
	results = {'test': 'test'}
	return flask.jsonify(results)







app.run(debug=True)