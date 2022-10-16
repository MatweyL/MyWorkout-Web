from app.utils.base import Singleton


class TrainCRUD(metaclass=Singleton):

    def __init__(self):
        self.trains = [
            {"user_id": 0,
             "name": "Тренирока 1",
             "description": "Описание тренировки 1"
             },
            {"user_id": 0,
             "name": "Тренирока 2",
             "description": "Описание тренировки 2"
             }
        ]
        for train in self.trains:
            train["train_id"] = self.trains.index(train)

    def get_all(self, user_id):
        return [train for train in self.trains if train["user_id"] == user_id]

    def get_by_id(self, user_id, train_id):
        for train in self.trains:
            if train["user_id"] == user_id and train["train_id"] == train_id:
                return train

    def create(self, train_dto):
        self.trains.append(train_dto)
        self.trains[-1]["train_id"] = len(self.trains) - 1
        return self.trains[-1]

    def update(self, train):
        train_to_update = self.get_by_id(train["user_id"], train["train_id"])
        train_to_update.update(train)
        return train_to_update

    def delete(self, user_id, train_id):
        train_to_delete = self.get_by_id(user_id, train_id)
        self.trains.remove(train_to_delete)
        return train_to_delete
