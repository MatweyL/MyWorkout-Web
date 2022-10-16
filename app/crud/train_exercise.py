from app import db
from app.models.base import TrainExercise
from app.utils.base import Singleton


class TrainExerciseCRUD(metaclass=Singleton):

    def get_max_sequence_number(self, user_id, train_id):
        sequence_number = 0
        for train_exercise in self.get_all(user_id, train_id):
            if train_exercise.sequence_number > sequence_number:
                sequence_number = train_exercise.sequence_number
        return sequence_number

    def get_all(self, user_id, train_id):
        train_exercises = db.session.execute(db.select(TrainExercise).filter(TrainExercise.myworkout_user_id == user_id,
                                                                             TrainExercise.train_id == train_id)).scalars()
        return train_exercises

    def get_by_id(self, sequence_number, user_id, train_id):
        return db.session.execute(db.select(TrainExercise).filter(TrainExercise.sequence_number == sequence_number,
                                                                  TrainExercise.myworkout_user_id == user_id,
                                                                  TrainExercise.train_id == train_id)).scalar()

    def create(self, train_exercise):
        db.session.add(train_exercise)
        db.session.commit()
        return train_exercise

    def update(self, train_exercise):
        train_exercise_to_update = self.get_by_id(train_exercise.sequence_number, train_exercise.myworkout_user_id, train_exercise.train_id)
        train_exercise_to_update.reps = train_exercise.reps
        train_exercise_to_update.sets = train_exercise.sets
        train_exercise_to_update.timeout = train_exercise.timeout
        train_exercise_to_update.exercise_id = train_exercise.exercise_id
        db.session.commit()
        return train_exercise_to_update

    def delete(self, sequence_number, user_id, train_id):
        train_exercise_to_delete = self.get_by_id(sequence_number, user_id, train_id)
        db.session.delete(train_exercise_to_delete)
        db.session.commit()
        return train_exercise_to_delete
