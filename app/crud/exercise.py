

class ExerciseCRUD:

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
            exercise["id"] = self.exercises.index(exercise)

    def get_all(self):
        return self.exercises

    def get_by_id(self, exercise_id):
        if 0 <= exercise_id < len(self.exercises):
            return self.exercises[exercise_id]
        return None

    def create(self, exercise_dto):
        self.exercises.append(exercise_dto)
        self.exercises[-1]["id"] = len(self.exercises) - 1
        return  self.exercises[-1]

    def update(self, exercise):
        self.exercises[exercise["id"]] = exercise
        return self.exercises[exercise["id"]]

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
    print(ecrud.update({"id": 2, "name": "plansh", "description": "eee"}))
    print(ecrud.get_all())
