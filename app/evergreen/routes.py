from flask import Blueprint, flash, render_template, url_for

mod = Blueprint('evergreen', __name__, url_prefix='/evergreen', template_folder='templates')

@mod.route("")
def home_pg():

	return render_template('home.html',title='Evergreen')

@mod.route("/<string:article_name>")
def evergreen_pg(article_name):

    return article_name
