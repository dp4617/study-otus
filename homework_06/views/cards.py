import logging

from flask import Blueprint, render_template, request, redirect, url_for
from sqlalchemy.exc import IntegrityError, DatabaseError
from werkzeug.exceptions import NotFound, BadRequest, InternalServerError
from models import db, Card

cards_app = Blueprint('cards_app', __name__)


@cards_app.route("/", endpoint='list')
def cards_shown():
    cards = Card.query.order_by(Card.name).all()
    return render_template('cards/list.html', cards=cards)


def get_card_name_from_form():
    card_name = request.form.get('card-name')
    if name := (card_name and card_name.strip()):
        return name

    raise BadRequest('Field card-name is required!')


def save_card(card_name):
    try:
        db.session.commit()
    except IntegrityError as ex:
        logging.warning("got integrity error with text %s", ex)
        raise BadRequest(f"Couldn't add product {card_name}, probably name is not unique")
    except DatabaseError:
        db.session.rollback()
        logging.exception("Got db error!")
        raise InternalServerError(f"Couldn't save card with name {card_name}")


@cards_app.route('/<card_id>/', methods=["GET", "POST"], endpoint='details')
def get_card(card_id: str):
    card = Card.query.get(card_id)
    if card is None:
        raise NotFound(f'Card with card name {card_id} not found!')
    if request.method == "GET":
        return render_template('cards/details.html', card=card)

    card_name = get_card_name_from_form()
    if card.name == card_name:
        raise BadRequest(f"This card is already named {card_name}")
    if Card.query.filter_by(name=card_name).count():
        raise BadRequest(f"card with name {card_name!r} already exists!")

    card.name = card_name
    save_card(card_name)
    return redirect(url_for('cards_app.details', card_id=card.id))


@cards_app.route('/add/', methods=['GET', 'POST'], endpoint='add')
def add_card():
    if request.method == 'GET':
        return render_template('cards/add.html')
    card_name = get_card_name_from_form()
    card = Card(name=card_name)
    db.session.add(card)

    save_card(card_name)
    return redirect(url_for('cards_app.details', card_id=card.id))



