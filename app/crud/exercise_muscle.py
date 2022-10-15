from app.utils.base import Singleton


class ExerciseMuscleCRUD(metaclass=Singleton):

    def __init__(self):
        self.exercise_muscle = [
            {
                "exercise_id": 0,
                "muscle_id": 1
            },
            {
                "exercise_id": 0,
                "muscle_id": 2
            },
            {
                "exercise_id": 1,
                "muscle_id": 0
            },
            {
                "exercise_id": 2,
                "muscle_id": 2
            },
            {
                "exercise_id": 2,
                "muscle_id": 0
            },
            {
                "exercise_id": 2,
                "muscle_id": 1
            }
        ]

    def get_muscles_ids(self, exercise_id):
        muscles_ids = []
        for em in self.exercise_muscle:
            if em["exercise_id"] == exercise_id:
                muscles_ids.append(em["muscle_id"])
        return muscles_ids

    def set_muscle(self, exercise_id, muscle_id):
        mapping = {"exercise_id": exercise_id, "muscle_id": muscle_id}
        self.exercise_muscle.append(mapping)
        return mapping

    def remove_muscle(self, exercise_id, muscle_id):
        index = -1
        for em in self.exercise_muscle:
            if em["exercise_id"] == exercise_id and em["muscle_id"] == muscle_id:
                index = self.exercise_muscle.index(em)
                break
        if index != -1:
            return self.exercise_muscle.pop(index)
        return None

    def __delete_exercise(self, exercise_id):
        index = -1
        for em in self.exercise_muscle:
            if em["exercise_id"] == exercise_id:
                index = self.exercise_muscle.index(em)
                break
        if index != -1:
            return self.exercise_muscle.pop(index)
        return None

    def delete_exercise(self, exercise_id):
        exercise_muscle = []
        while True:
            result = self.__delete_exercise(exercise_id)
            if not result:
                break
            exercise_muscle.append(result)
        return exercise_muscle

    def __delete_muscle(self, muscle_id):
        index = -1
        for em in self.exercise_muscle:
            if em["muscle_id"] == muscle_id:
                index = self.exercise_muscle.index(em)
                break
        if index != -1:
            return self.exercise_muscle.pop(index)
        return None

    def delete_muscle(self, muscle_id):
        exercise_muscle = []
        while True:
            result = self.__delete_muscle(muscle_id)
            if not result:
                break
            exercise_muscle.append(result)
        return exercise_muscle


if __name__ == "__main__":
    emcrud = ExerciseMuscleCRUD()
    print(emcrud.get_muscles_ids(1))
    print(emcrud.set_muscle(1, 1))
    print(emcrud.get_muscles_ids(1))
    print(emcrud.remove_muscle(1, 1))
    print(emcrud.delete_muscle(1))
    print(emcrud.get_muscles_ids(2))
