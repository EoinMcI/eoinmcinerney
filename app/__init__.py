from flask import Flask

app = Flask(__name__)
app.url_map.strict_slashes = False

from app.site.routes import mod
from app.monthly_updates.routes import mod
from app.evergreen.routes import mod
from app.local.routes import mod
from app.thoughts.routes import mod

from app.api.routes import mod

app.register_blueprint(site.routes.mod)
app.register_blueprint(monthly_updates.routes.mod)
app.register_blueprint(evergreen.routes.mod)
app.register_blueprint(local.routes.mod)
app.register_blueprint(thoughts.routes.mod)

app.register_blueprint(api.routes.mod, subdomain='api')
