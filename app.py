from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
	return "For the demo, navigate to the endpoint /"

if __name__ == "__main__":
	app.run(debug=True, use_reloader=True)
