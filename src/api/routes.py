"""
This module takes care of starting the API Server, Loading the DB and Adding the endpoints
"""
from flask import Flask, request, jsonify, url_for, Blueprint
from api.models import db, User, Session, Test
from api.utils import generate_sitemap, APIException
import datetime
from sqlalchemy import delete

api = Blueprint('api', __name__)


@api.route('/users', methods=['GET'])
def handle_users():

    users = User.query.all()

    response_body = {}

    for index, user in enumerate(users):
        response_body["id" + str(index)] = (user.id)


    return jsonify(response_body), 200

@api.route('/sessions', methods=['GET', 'POST', 'DELETE'])
def handle_sessions():

    if request.method == "DELETE":
            Session.query.filter(Session.id >= 0).delete()
            db.session.commit()
            response_body = "Deleted all!"
            return jsonify(response_body), 200

    if request.method == "POST":
        # We create an instance without being recorded in the database
        session = Session()
        session.user_id = 3
        session.email = "test@test.com"
        session.date = datetime.datetime.now()
        session.time_spent_secs = 666
        session.work_time_secs = 333
        session.fun_time_secs = 333

        # We tell the database we want to record this user
        db.session.add(session)
        db.session.commit()

    # GET request just does this part

    response_body = {}
    results = Session.query.all()
    for index, result in enumerate(results):
            response_body["time_spent" + str(index)] = (result.time_spent_secs)
            response_body["fun_time" + str(index)] = (result.fun_time_secs)
            response_body["work_time" + str(index)] = (result.work_time_secs)


    # for index, session in enumerate(sessions):
    #     response_body["date" + str(index)] = (session.date)

    return jsonify(response_body), 200

@api.route('/test', methods=['GET', 'DELETE'])
def handle_tests():

    if request.method == "DELETE":
            Test.query.filter_by(test_value = "Sausage").delete()
            db.session.commit()
            response_body = "Deleted all!"

    if request.method == "GET":
         
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