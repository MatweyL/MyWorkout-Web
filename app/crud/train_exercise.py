class TrainExerciseCRUD:

    def __init__(self):
        self.trains_exercises = [
            {
                "sequence_number": 1,
                "user_id": 0,
                "train_id": 0,
                "exercise_id": 0,
                "reps": 10,
                "sets": 5,
                "timeout": 180
            },
            {
                "sequence_number": 2,
                "user_id": 0,
                "train_id": 0,
                "exercise_id": 1,
                "reps": 8,
                "sets": 4,
                "timeout": 180
            },
            {
                "sequence_number": 3,
                "user_id": 0,
                "train_id": 0,
                "exercise_id": 2,
                "reps": 6,
                "sets": 5,
                "timeout": 180
            },
            {
                "sequence_number": 1,
                "user_id": 0,
                "train_id": 1,
                "exercise_id": 0,
                "reps": 10,
                "sets": 5,
                "timeout": 180
            },
            {
                "sequence_number": 1,
                "user_id": 1,
                "train_id": 0,
                "exercise_id": 0,
                "reps": 10,
                "sets": 5,
                "timeout": 180
            },
        ]

    def get_all(self, user_id, train_id):
        train_exercises = []
        for train_exercise in self.trains_exercises:
            if train_exercise["user_id"] == user_id and train_exercise["train_id"] == train_id:
                train_exercises.append(train_exercise)
        return train_exercises

    def get_by_id(self, sequence_number, user_id, train_id):
        for train_exercise in self.trains_exercises:
            if (train_exercise["user_id"] == user_id
                    and train_exercise["train_id"] == train_id
                    and train_exercise["sequence_number"] == sequence_number):
                return train_exercise
        return None

    def create(self, train_exercise_dto):
        self.trains_exercises.append(train_exercise_dto)
        return self.trains_exercises[-1]

    def update(self, train_exercise):
        train_exercise_to_update = self.get_by_id(train_exercise["sequence_number"],
                                                  train_exercise["user_id"],
                                                  train_exercise["train_id"])
        train_exercise_to_update = train_exercise
        return train_exercise_to_update

    def delete(self, user_id, train_id, sequence_number):
        train_exercise_to_delete = self.get_by_id(user_id, train_id, sequence_number)
        self.trains_exercises.remove(train_exercise_to_delete)
        return train_exercise_to_delete
