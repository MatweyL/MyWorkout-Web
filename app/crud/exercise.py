from app.crud.exercise_muscle import ExerciseMuscleCRUD
from app.utils.base import Singleton


class ExerciseCRUD(metaclass=Singleton):

    def __init__(self):
        self.exercises = [
            {
                "name": "pull-ups",
                "description": "There is no description"
            },
            {
                "name": "push-ups",
                "description": "baldezh"
            },
            {
                "name": "handstand",
                "description": "Eee rock"
            },
        ]
        for exercise in self.exercises:
            exercise["exercise_id"] = self.exercises.index(exercise)
            exercise["can_delete"] = 0

    def get_all(self):
        return self.exercises

    def get_by_id(self, exercise_id):
        if 0 <= exercise_id < len(self.exercises):
            return self.exercises[exercise_id]
        return None

    def get_by_name(self, name):
        for exercise in self.exercises:
            if exercise["name"] == name:
                return exercise

    def create(self, exercise_dto):
        self.exercises.append(exercise_dto)
        self.exercises[-1]["exercise_id"] = len(self.exercises) - 1
        self.exercises[-1]["can_delete"] = 1
        return self.exercises[-1]

    def update(self, exercise):
        self.exercises[exercise["exercise_id"]] = exercise
        return self.exercises[exercise["exercise_id"]]

    def delete(self, exercise_id):
        exercise = self.exercises.pop(exercise_id)
        return exercise


if __name__ == "__main__":
    ecrud = ExerciseCRUD()
    print(ecrud.get_all())
    print(ecrud.get_by_id(1))
    print(ecrud.get_by_id(10))
    print(ecrud.delete(2))
    print(ecrud.create({"name": "plansh", "description": None}))
    print(ecrud.update({"exercise_id": 2, "name": "plansh", "description": "eee"}))
    print(ecrud.get_all())
