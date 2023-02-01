import os

from flask import Flask
from werkzeug.exceptions import InternalServerError, HTTPException
from flask_migrate import Migrate

from views.cards import cards_app
from models import db


app = Flask(__name__)
app.register_blueprint(cards_app, url_prefix='/cards')

CONFIG_OBJ_PATH = 'config.{}'.format(os.getenv("CONFIG", "DevelopmentConfig"))
app.config.from_object(CONFIG_OBJ_PATH)

db.init_app(app)
migrate = Migrate(app, db)


@app.route("/")
def root():
    return '<h1>Welcome to the calendar!</h1>'


@app.errorhandler(KeyError)
def handle_key_error(exc):
    print('exc', exc)
    return InternalServerError(f"Oops, could't find that by key {exc}!")


@app.errorhandler(Exception)
def handle_all_exceptions(exc):
    if isinstance(exc, HTTPException):
        return exc
    print('exc', exc)
    return InternalServerError(f"Oops, unexpected exception")


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')

