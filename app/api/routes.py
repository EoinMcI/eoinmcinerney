from flask import Blueprint

mod = Blueprint('api', __name__)

@mod.route('/get-stuff')
def get_stuff():
	return '{"results":"json"}'
