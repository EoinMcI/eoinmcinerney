from flask import Blueprint, flash, render_template, url_for

mod = Blueprint('thoughts', __name__, url_prefix='/thoughts', template_folder='templates')

@mod.route("")
def home_pg():

	return render_template('home.html',title='thoughts')

@mod.route("/<string:article_name>")
def thought_pg(article_name):

    return article_name
