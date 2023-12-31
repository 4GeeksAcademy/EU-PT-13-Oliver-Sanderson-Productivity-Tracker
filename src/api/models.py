from flask_sqlalchemy import SQLAlchemy
from hmac import compare_digest
from sqlalchemy import DateTime
import datetime

db = SQLAlchemy()

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True, nullable=False)
    name = db.Column(db.String(250), nullable=False)
    last_name = db.Column(db.String(250), nullable=False)
    password = db.Column(db.String(80), unique=False, nullable=False)
    is_active = db.Column(db.Boolean(), unique=False, nullable=False)

    def __repr__(self):
        return f'<User {self.email}>'

    def serialize(self):
        return {
            "id": self.id,
            "email": self.email,
            "name": self.name,
            "last_name": self.last_name,
            # do not serialize the password, its a security breach
        }
    def check_password(self, password):
        return compare_digest(password, self.password)
    
class Session(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    date = db.Column(db.DateTime, nullable=False)
    time_spent_secs = db.Column(db.Integer, nullable=False)
    work_time_secs = db.Column(db.Integer, nullable=False)
    fun_time_secs = db.Column(db.Integer, nullable=False)

    def __repr__(self):
        return f'<Session {self.date}>'
    
    def serialize(self):
        return {
            "id": self.id,
            "user_id": self.user_id,
            "date": self.date,
            "time_spent_secs": self.time_spent_secs,
            "work_time_secs": self.work_time_secs,
            "fun_time_secs": self.fun_time_secs,
        }
    
class Test(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    test_value = db.Column(db.String(120), nullable=False)

    Obj3 = datetime.datetime.now()
    todayDate = Obj3.date()
    todayTime = Obj3.time()
    print(Obj3)
    print(todayDate)
    print(todayTime)

    def __repr__(self):
        return f'<Test {self.test_value}>'
    
    def serialize(self):
        return {
            "id": self.id,
            "test_value": self.test_value,
        }