from flask import Blueprint, render_template

common = Blueprint('user', __name__, template_folder="templates", static_folder="static")


@common.route('/',  methods=["GET"])
def user_profile():
    return render_template("index.html")
