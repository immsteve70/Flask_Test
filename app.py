from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "Hello, Flask"

@app.route("/about")
def about():
    return "<h1>AboutMe</h1><p>I'm Emmanuel, learning Flask step by step.</p>"

if __name__ == "__main__":
    app.run(debug=True)