import datetime

from flask_login import UserMixin
from sqlalchemy import Column, Integer, String, DateTime, Text, VARCHAR, BOOLEAN, ForeignKey, func
from sqlalchemy.orm import relationship

from app.db.base import Base, db


# class Train(Base):
#     id = Column(Integer, primary_key=True, index=True, autoincrement=True)
#     name = Column(VARCHAR(64), nullable=False)
#     description = Column(Text, nullable=True)
#     timestamp = Column(DateTime, nullable=False, default=datetime.datetime.now())
#
#
# class Exercise(Base):
#     id = Column(Integer, primary_key=True, index=True, autoincrement=True)
#     name = Column(VARCHAR(64), nullable=False)
#     description = Column(Text, nullable=True)
#     can_delete = Column(BOOLEAN, nullable=False)
#     timestamp = Column(DateTime, nullable=False, default=datetime.datetime.now())
#     muscles = relationship('Muscle', secondary='exercise_muscle', back_populates='exercise')
#
#
# class Muscle(Base):
#     id = Column(Integer, primary_key=True, index=True, autoincrement=True)
#     name = Column(VARCHAR(64), nullable=False)
#     description = Column(Text, nullable=True)
#     timestamp = Column(DateTime, nullable=False, default=datetime.datetime.now())
#     exercises = relationship('Exercise', secondary='exercise_muscle', back_populates='muscle')
#
#
# class TrainExercise(Base):
#     sequence_number = Column(Integer, nullable=False)
#     train_id = Column(Integer, ForeignKey('train.id'), nullable=False)
#     exercise_id = Column(Integer, nulalble=False)
#     reps = Column(Integer, nullable=False)
#     sets = Column(Integer, nullable=False)
#     timeout = Column(Integer, nullable=False)
#
#
# class ExerciseMuscle(Base):
#     exercise_id = Column(Integer, ForeignKey('exercise.id'), nulalble=False)
#     muscle_id = Column(Integer, ForeignKey('muscle.id'), nulalble=False)


class MyworkoutUser(db.Model, Base, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    nickname = db.Column(db.String(32), nullable=False)
    password_hash = db.Column(db.String(128), nullable=False)
    email = db.Column(db.String(64), nullable=False, unique=True)
    timestamp = db.Column(db.DateTime, default=datetime.datetime.utcnow())

    def __repr__(self):
        return f"<user {self.id}>"
