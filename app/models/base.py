import datetime

from flask_login import UserMixin
from sqlalchemy.orm import relationship

from app.db.base import Base, db


class Train(db.Model, Base):
    id = db.Column(db.Integer, primary_key=True, index=True, autoincrement=True)
    myworkout_user_id = db.Column(db.Integer, db.ForeignKey('myworkout_user.id'))
    name = db.Column(db.String(64), nullable=False)
    description = db.Column(db.Text)
    timestamp = db.Column(db.DateTime, default=datetime.datetime.utcnow())


class Exercise(db.Model, Base):
    id = db.Column(db.Integer, primary_key=True, index=True, autoincrement=True)
    myworkout_user_id = db.Column(db.Integer, db.ForeignKey('myworkout_user.id'), nullable=True)
    name = db.Column(db.String(64), nullable=False)
    description = db.Column(db.Text, nullable=True)
    timestamp = db.Column(db.DateTime, default=datetime.datetime.utcnow())


class Muscle(db.Model, Base):
    id = db.Column(db.Integer, primary_key=True, index=True, autoincrement=True)
    name = db.Column(db.String(64), nullable=False)
    description = db.Column(db.Text, nullable=True)
    timestamp = db.Column(db.DateTime, default=datetime.datetime.utcnow())


class TrainExercise(db.Model, Base):
    id = db.Column(db.Integer, primary_key=True, index=True, autoincrement=True)
    sequence_number = db.Column(db.Integer, nullable=False)
    myworkout_user_id = db.Column(db.Integer, db.ForeignKey('myworkout_user.id'))
    train_id = db.Column(db.Integer, db.ForeignKey('train.id'), nullable=False)
    exercise_id = db.Column(db.Integer, nullable=False)
    reps = db.Column(db.Integer, nullable=False)
    sets = db.Column(db.Integer, nullable=False)
    timeout = db.Column(db.Integer, nullable=False)


class ExerciseMuscle(db.Model, Base):
    id = db.Column(db.Integer, primary_key=True, index=True, autoincrement=True)
    exercise_id = db.Column(db.Integer, db.ForeignKey('exercise.id'), nullable=False)
    muscle_id = db.Column(db.Integer, db.ForeignKey('muscle.id'), nullable=False)


class MyworkoutUser(db.Model, Base, UserMixin):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nickname = db.Column(db.String(32), nullable=False)
    password_hash = db.Column(db.String(128), nullable=False)
    email = db.Column(db.String(64), nullable=False, unique=True)
    timestamp = db.Column(db.DateTime, default=datetime.datetime.utcnow())

    def __repr__(self):
        return f"<user {self.id}>"
