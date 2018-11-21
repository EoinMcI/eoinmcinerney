from flask import Blueprint, flash, render_template, url_for

mod = Blueprint('site', __name__, template_folder='templates')

@mod.route("/")
def home_pg():

	return render_template('home.html',title='Home')

@mod.route("/why")
def why_pg():

	return render_template('home.html',title='Why')

@mod.route("/about")
def about_pg():

	return render_template('home.html',title='About')
