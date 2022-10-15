from flask import Blueprint, render_template

common = Blueprint('common', __name__, template_folder="templates", static_folder="static")


@common.route('/',  methods=["GET"])
def index():
    return render_template("index.html")
