from flask import Blueprint
from flask import redirect, render_template, request, url_for
from flask_login import login_required, login_user, logout_user, LoginManager
from werkzeug.security import check_password_hash, generate_password_hash

from app.db.base import db
from app.models.base import MyworkoutUser
from app.web.forms import LoginForm, RegisterForm

login_manager = LoginManager()


@login_manager.user_loader
def load_user(user_id):
    return MyworkoutUser.query.get(user_id)


auth = Blueprint('auth', __name__, template_folder="templates", static_folder="static")


@auth.route("/login", methods=["GET", "POST"])
def login():
    form = LoginForm()

    if request.method == "POST" and form.validate_on_submit():
        user = MyworkoutUser.query.filter_by(email=form.email.data).first()

        if user and check_password_hash(user.password_hash, form.password.data):
            login_user(user)
            next_page = request.args.get('next')
            if not next_page:
                next_page = url_for("train.get_trains", user_id=user.id)
            return redirect(next_page)
    return render_template('auth/login.html', form=form)


@auth.route("/logout", methods=["GET", "POST"])
@login_required
def logout():
    logout_user()
    return redirect(url_for('auth.login'))


@auth.route("/register", methods=("GET", "POST"))
def register():
    form = RegisterForm()
    if request.method == 'POST' and form.validate_on_submit():

        password_hash = generate_password_hash(form.password.data)
        new_user = MyworkoutUser(nickname=form.nickname.data, email=form.email.data, password_hash=password_hash)
        db.session.add(new_user)
        db.session.commit()

        return redirect(url_for('auth.login'))

    return render_template('auth/register.html', form=form)

