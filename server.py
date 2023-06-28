from flask import Flask, render_template
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from config.setup import Users

Session = sessionmaker(bind=engine)
session = Session()
app = Flask(__name__)

# figure out how to make bind engine work along with request.json
@app.route("/")
def index():
    try:
        #new_user = Users(id=request.json.id, username=request.json.username)
        #return session.add(new_user)
        return "hellow world"
    except:
        return "ERROR HANDLING DATA"

if __name__ == "__main__":
    app.run(debug=True)