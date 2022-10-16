from app import db
from app.models.base import ExerciseMuscle
from app.utils.base import Singleton


class ExerciseMuscleCRUD(metaclass=Singleton):

    def get_muscles_ids(self, exercise_id):
        ems = db.session.execute(db.select(ExerciseMuscle).filter_by(exercise_id=exercise_id)).scalars()
        muscles_ids = [em.muscle_id for em in ems]
        return muscles_ids

    def set_muscle(self, exercise_id, muscle_id):
        em = ExerciseMuscle(exercise_id=exercise_id, muscle_id=muscle_id)
        db.session.add(em)
        db.session.commit()
        return em

    def remove_muscle(self, exercise_id, muscle_id):
        em_to_remove = db.session.execute(db.select(ExerciseMuscle).filter(ExerciseMuscle.exercise_id==exercise_id, ExerciseMuscle.muscle_id==muscle_id)).scalar()
        db.session.delete(em_to_remove)
        db.session.commit()
        return em_to_remove
