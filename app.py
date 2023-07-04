from flask import Flask, render_template, request

# move these over when organizing routes
from sqlalchemy import insert
from models.user import Users
from config.setup import session

app = Flask(__name__)

@app.route("/", methods=["GET"])
def send_data():
    if request.method == "GET":
        try:
            return "hi"
        except:
            return "ERROR HANDLING DATA"

@app.route("/add/", methods=["POST"])
def index():
    if request.method == "POST":
        try:
            new_user = Users(username=request.json["username"], email=request.json["email"], password=request.json["password"])
            session.add(new_user)
            session.commit()
            return "added"
        except:
            return "ERROR HANDLING DATA"

if __name__ == "__main__":
    app.run(debug=True)