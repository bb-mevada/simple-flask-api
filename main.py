from flask import Flask, jsonify
import jwt # pip install jwt

app = Flask(__name__)


@app.route("/")
def welcome():
    return "Welcome"


@app.route("/palindrome/<string:value>")
def palindrome(value):
    if value == value[::-1]:
        result = {"is_palindrome": True, "value": value}
    else:
        result = {"is_palindrome": False, "value": value}
    
    return jsonify(result)


if __name__ == "__main__":
    app.run(debug=True)
