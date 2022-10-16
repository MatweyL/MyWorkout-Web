from app import db
from app.models.base import Train
from app.utils.base import Singleton


class TrainCRUD(metaclass=Singleton):

    def get_all(self, user_id):
        trains = db.session.execute(db.select(Train)).scalars()
        return trains  # [train for train in self.trains if train["user_id"] == user_id]

    def get_by_id(self, user_id, train_id):
        return db.session.execute(db.select(Train).filter(Train.myworkout_user_id == user_id,
                                                          Train.id == train_id)).scalar()

    def create(self, train):
        db.session.add(train)
        db.session.commit()
        return train

    def update(self, train):
        user_id = train.myworkout_user_id
        train_id = train.id
        train_to_update = db.session.execute(db.select(Train).filter(Train.myworkout_user_id == user_id,
                                                                     Train.id == train_id)).scalar()

        train_to_update.name = train.name
        train_to_update.description = train.description
        db.session.commit()
        return train

    def delete(self, user_id, train_id):
        train_to_delete = db.session.execute(db.select(Train).filter(Train.myworkout_user_id == user_id,
                                                                     Train.id == train_id)).scalar()

        db.session.delete(train_to_delete)
        db.session.commit()
        return train_to_delete
