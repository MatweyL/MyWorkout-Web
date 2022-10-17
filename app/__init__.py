from flask import Flask

from app.db.base import db
from app.utils.base import get_db_url
from app.web.auth import login_manager


def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'sTTyyVBBBH23837788SafvSF(*hfwh'
    app.config['SQLALCHEMY_DATABASE_URI'] = get_db_url()
    # app.config.from_object(os.environ['APP_SETTINGS'])
    # app.config.from_object('config')
    db.init_app(app)
    with app.test_request_context():
        db.create_all()

    login_manager.init_app(app)

    from app.web.common import common
    from app.web.exercise import exercise
    from app.web.train import train
    from app.web.auth import auth
    # from app.modules.user.routes import user
    app.register_blueprint(common, url_prefix="/")
    app.register_blueprint(exercise, url_prefix="/exercises")
    app.register_blueprint(train, url_prefix="/trains")
    app.register_blueprint(auth, url_prefix="/auth")
    # app.register_blueprint(user, url_prefix="/user")

    return app
