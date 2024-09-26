from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
  return "", 200

@app.route("/login")
def login():
  return "<p>Login</p>", 200