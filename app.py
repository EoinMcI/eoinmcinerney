from flask import Flask, flash, redirect, render_template, session, flash, url_for


app = Flask(__name__)
app.config['SECRET_KEY'] = "somethingsecure"


@app.route("/")
def home_pg():

	return render_template('home.html',title='Home')

@app.route("/why")
def why_pg():

	return render_template('home.html',title='Why')

@app.route("/about")
def about_pg():

	return render_template('home.html',title='About')

####################

@app.route("/monthly-updates")
def monthly_update_home_pg():

	return render_template('home.html',title='Monthly Updates')

@app.route("/monthly-updates/<string:article_name>/")
def monthly_update_pg(article_name):
    return article_name

####################

@app.route("/evergreen")
def evergreen_home_pg():

	return render_template('home.html',title='Evergreen')

@app.route("/evergreen/<string:article_name>/")
def evergreen_pg(article_name):
    return article_name

####################

@app.route("/local")
def local_home_pg():

	return render_template('home.html',title='Local')

@app.route("/local/<string:article_name>/")
def local_pg(article_name):
    return article_name

####################

@app.route("/thoughts")
def thoughts_home_pg():

	return render_template('home.html',title='Thoughts')
	
@app.route("/thoughts/<string:article_name>/")
def thought_pg(article_name):
    return article_name
	
	