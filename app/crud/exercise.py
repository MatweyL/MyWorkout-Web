from app import db
from app.crud.exercise_muscle import ExerciseMuscleCRUD
from app.models.base import Exercise
from app.utils.base import Singleton


class ExerciseCRUD(metaclass=Singleton):

    def get_all(self, user_id):
        return db.session.execute(db.select(Exercise).filter(Exercise.myworkout_user_id == user_id)).scalars()

    def get_by_id(self, user_id, exercise_id):
        return db.session.execute(db.select(Exercise).filter(Exercise.myworkout_user_id == user_id,
                                                                     Exercise.id == exercise_id)).scalar()

    def get_by_name(self, user_id, name):
        return db.session.execute(db.select(Exercise).filter(Exercise.myworkout_user_id == user_id, Exercise.name == name)).scalar()

    def get_names(self, user_id):
        return [e.name for e in db.session.execute(db.select(Exercise).filter(Exercise.myworkout_user_id == user_id)).scalars()]

    def create(self, exercise):
        db.session.add(exercise)
        db.session.commit()
        return exercise

    def update(self, exercise):
        user_id = exercise.myworkout_user_id
        exercise_id = exercise.id
        exercise_to_update = self.get_by_id(user_id, exercise_id)

        exercise_to_update.name = exercise.name
        exercise_to_update.description = exercise.description
        db.session.commit()
        return exercise_to_update

    def delete(self, user_id, exercise_id):
        exercise_to_delete = self.get_by_id(user_id, exercise_id)
        db.session.delete(exercise_to_delete)
        db.session.commit()
        return exercise_to_delete
