from flask import Flask, redirect, render_template, request, session, abort, flash, url_for


app = Flask(__name__)
app.config['SECRET_KEY'] = "somethingsecure"


@app.route("/")
def home_pg():



    return render_template('home.html',title='Eoin McInerney')

if __name__ == '__main__':
    app.run()