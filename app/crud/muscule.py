from app.utils.base import Singleton


class MuscleCRUD(metaclass=Singleton):

    def __init__(self):
        self.muscles = [
            {
                "name": "biceps",
                "description": "hahaha"
            },
            {
                "name": "triceps",
                "description": "heheheh"
            },
            {
                "name": "press",
                "description": "hihihi"
            },
        ]
        for muscle in self.muscles:
            muscle["muscle_id"] = self.muscles.index(muscle)

    def get_all(self):
        return self.muscles

    def get_by_name(self, name):
        for muscle in self.muscles:
            if muscle["name"] == name:
                return muscle

    def get_by_id(self, muscle_id):
        if 0 <= muscle_id < len(self.muscles):
            return self.muscles[muscle_id]
        return None
    
    def get_by_ids(self, muscles_ids):
        muscles = []
        for muscle_id in muscles_ids:
            muscles.append(self.get_by_id(muscle_id))
        return muscles

    def create(self, muscle_id):
        self.muscles.append(muscle_id)
        self.muscles[-1]["muscle_id"] = len(self.muscles) - 1
        return self.muscles[-1]

    def update(self, muscle):
        self.muscles[muscle["muscle_id"]] = muscle
        return self.muscles[muscle["muscle_id"]]

    def delete(self, muscle_id):
        muscle = self.muscles.pop(muscle_id)
        return muscle
