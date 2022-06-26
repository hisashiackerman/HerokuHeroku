

from flask import Flask, render_template, flash
from flask_sqlalchemy import SQLAlchemy

from datetime import datetime
from forms import UserForm, TwitterSearchForm
import twitter_bot_python as bot


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
# app.config['SQLALCHEMY_DATABASE_URI'] = 'postgres://zfldepccsydywe:199084877f6571c67b03c4b5ba0aa0fd6dc3a4db7e46bc54645bdcc01d9657ad@ec2-52-22-136-117.compute-1.amazonaws.com:5432/db00s6gbl9viqd'
app.config['SECRET_KEY'] = "e07e5ecdb25b94b71947500f166ce38e"

db = SQLAlchemy(app)


class Users(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(200), nullable=False)
    email = db.Column(db.String(120), nullable=False, unique=True)
    date_added = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self) -> str:
        return '<Name %r>' % self.name


@app.route("/", methods=['GET', 'POST'])
@app.route("/home", methods=['GET', 'POST'])
def index():
    form = UserForm()
    anime_list = ["Attack on Titan", "Steins;Gate", "Fate Series"]
    if form.validate_on_submit():
        user = Users(name=form.username.data, email=form.email_id.data)
        try:
            db.session.add(user)
            db.session.commit()
            website_users = Users.query.order_by(Users.date_added)
            return render_template('index.html', anime_list=anime_list, form=form, website_users=website_users)
        except:
            return render_template('index.html', anime_list=anime_list, form=form)

    website_users = Users.query.order_by(Users.date_added)
    return render_template('index.html', anime_list=anime_list, form=form, website_users=website_users)


@app.route('/analyse_tweets', methods=['GET', 'POST'])
def analyse_tweets():
    form = TwitterSearchForm()
    if form.validate_on_submit():
        username = form.username.data
        number_of_tweets = form.number_of_tweets.data
        bot.plot_graph(username, number_of_tweets)
        return render_template('result.html', username=username)
    return render_template('analyse_tweets.html', form=form)


if __name__ == '__main__':
    app.run(debug=True)
