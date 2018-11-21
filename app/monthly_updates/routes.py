from flask import Blueprint, flash, render_template, url_for

mod = Blueprint('monthly_updates', __name__, url_prefix='/monthly-updates', template_folder='templates')

@mod.route("")
def home_pg():

	return render_template('home.html',title='Monthly Updates')

@mod.route("/<string:article_name>")
def monthly_update_pg(article_name):

    return article_name
