from flask import Flask
app = Flask(__name__)

@app.route("/")
def home_pg():
    return "Home"

@app.route("/why")
def why_pg():
    return "Why"

@app.route("/about")
def about_pg():
    return "About"

@app.route("/monthly-updates")
def monthly_update_home_pg():
    return "Monthly Updates"
	
@app.route("/evergreen")
def evergreen_home_pg():
    return "Evergreens"
	
@app.route("/local")
def local_home_pg():
    return "Local"
	
@app.route("/thoughts")
def thoughts_home_pg():
    return "Thoughts"