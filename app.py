from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "<h1>Welcome to AWS EC2 Automation!</h1>"

@app.route("/status")
def status():
    return "<h2>Application is running successfully.</h2>"

if __name__ == "__main__":
    app.run(debug=True)