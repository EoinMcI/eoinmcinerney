from flask import Flask, redirect, render_template, request, session, abort, flash, url_for


application = Flask(__name__)
application.config['SECRET_KEY'] = "somethingsecure"


@application.route("/")
def home_pg():

    return render_template('home.html',title='Eoin McInerney')

if __name__ == '__main__':
    application.run()