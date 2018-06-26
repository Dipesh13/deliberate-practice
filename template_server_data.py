from flask import Flask, request
from flask_cors import CORS
import json

app = Flask(__name__)
CORS(app)

@app.route('/upload',methods=['POST'])
def upload_data():
	data = json.loads(request.data)
	label = data['label']
	return json.dumps(data['label'])


if __name__ == '__main__':
	app.run(host="0.0.0.0",port=8000, debug = True)