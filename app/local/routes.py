from flask import Blueprint, flash, render_template, url_for

mod = Blueprint('local', __name__, url_prefix='/local', template_folder='templates')

@mod.route("")
def home_pg():

	return render_template('home.html',title='Local')

@mod.route("/<string:article_name>")
def local_pg(article_name):

    return article_name

