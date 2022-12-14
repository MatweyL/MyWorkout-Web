from app import db
from app.models.base import Muscle
from app.utils.base import Singleton, get_path_to_muscles


class MuscleCRUD(metaclass=Singleton):

    def __init__(self):
        self.__setup()

    def get_all(self):
        return db.session.execute(db.select(Muscle)).scalars()

    def get_by_name(self, name):
        return db.session.execute(db.select(Muscle).filter(Muscle.name == name)).scalar()

    def get_by_id(self, muscle_id):
        return db.session.execute(db.select(Muscle).filter(Muscle.id == muscle_id)).scalar()
    
    def get_by_ids(self, muscles_ids):
        muscles = [self.get_by_id(muscle_id) for muscle_id in muscles_ids]

        return muscles

    def get_names(self):
        names = [muscle.name for muscle in self.get_all()]
        return names

    def __setup(self):
        if not db.session.execute(db.select(Muscle)).all():
            with open(get_path_to_muscles(), encoding='utf-8') as file:
                names = file.read().split('\n')
            if '' in names:
                names.remove('')
            for name in names:
                db.session.add(Muscle(name=name))
                db.session.commit()
