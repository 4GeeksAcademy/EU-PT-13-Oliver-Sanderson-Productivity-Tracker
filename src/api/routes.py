"""
This module takes care of starting the API Server, Loading the DB and Adding the endpoints
"""
from flask import Flask, request, jsonify, url_for, Blueprint
from api.models import db, User, Session, Test
from api.utils import generate_sitemap, APIException
import datetime

api = Blueprint('api', __name__)


    



@api.route('/users', methods=['GET'])
def handle_users():

    users = User.query.all()

    response_body = {}

    for index, user in enumerate(users):
        response_body["id" + str(index)] = (user.id)


    return jsonify(response_body), 200

@api.route('/sessions', methods=['GET'])
def handle_sessions():

    # We create an instance without being recorded in the database
    session = Session()
    session.user_id = 3
    session.email = "test@test.com"
    session.date = datetime.datetime.now()
    session.time_spent_secs = 666


    # We tell the database we want to record this user
    db.session.add(session)
    db.session.commit()

    sessions = Session.query.all()

    response_body = {}

    for index, session in enumerate(sessions):
        response_body["date" + str(index)] = (session.date)

    return jsonify(response_body), 200

@api.route('/test', methods=['GET'])
def handle_tests():

    # We create an instance without being recorded in the database
    testA = Test()
    testA.test_value = "Sausage"

    # We tell the database we want to record this user
    db.session.add(testA)
    db.session.commit()

    tests = Test.query.all()

    response_body = {}

    for index, testers in enumerate(tests):
        response_body["value" + str(index)] = (testers.test_value)

    return jsonify(response_body), 200