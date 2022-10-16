


class TrainCRUD:

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

    def get_by_id(self, train_id):
        return self.trains[train_id]

    def create(self, train_dto):
        self.trains.append(train_dto)
        self.trains[-1]["train_id"] = len(self.trains) - 1
        return self.trains[-1]

    def update(self, train):
        self.trains[train["train_id"]] = train
        return self.trains[train["train_id"]]

    def delete(self, train_id):
        train = self.trains.pop(train_id)
        return train