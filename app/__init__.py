from flask import Flask


def create_app():
    app = Flask(__name__)
    # app.config.from_object(os.environ['APP_SETTINGS'])
    # app.config.from_object('config')
    # db.init_app(app)
    # with app.test_request_context():
    #     db.create_all()
    #
    # login_manager.init_app(app)
    #
    from app.web.common import common
    from app.web.exercise import exercise
    # from app.modules.user.routes import user
    app.register_blueprint(common, url_prefix="/")
    app.register_blueprint(exercise, url_prefix="/exercises")
    # app.register_blueprint(user, url_prefix="/user")

    return app
