

class MuscleCRUD:

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
            muscle["id"] = self.muscles.index(muscle)

    def get_all(self):
        return self.muscles

    def get_by_id(self, muscle_id):
        if 0 <= muscle_id < len(self.muscles):
            return self.muscles[muscle_id]
        return None

    def create(self, muscle_id):
        self.muscles.append(muscle_id)
        self.muscles[-1]["id"] = len(self.muscles) - 1
        return self.muscles[-1]

    def update(self, muscle):
        self.muscles[muscle["id"]] = muscle
        return self.muscles[muscle["id"]]

    def delete(self, muscle_id):
        muscle = self.muscles.pop(muscle_id)
        return muscle
