from flask import Flask

app = Flask(__name__)

@app.route('/')
def homepage():
    return "Welcome to the homepage! FakePinterest"

if __name__ == "__main__":
    app.run(debug=True)
