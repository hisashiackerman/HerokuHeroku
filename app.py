
from flask import Flask, render_template, flash
# from forms import UserForm
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from datetime import datetime


app = Flask(__name__)
# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgres://zfldepccsydywe:199084877f6571c67b03c4b5ba0aa0fd6dc3a4db7e46bc54645bdcc01d9657ad@ec2-52-22-136-117.compute-1.amazonaws.com:5432/db00s6gbl9viqd'
app.config['SECRET_KEY'] = "e07e5ecdb25b94b71947500f166ce38e"

db = SQLAlchemy(app)


@app.route("/")
@app.route("/home")
def index():
    anime_list = ["Attack on Titan", "Steins;Gate", "Fate Series"]
    return render_template('index.html', anime_list=anime_list)


# if __name__ == '__main__':
#     app.run(debug=True)
