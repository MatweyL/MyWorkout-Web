from flask import Blueprint, render_template

exercise = Blueprint('exercise', __name__, template_folder="templates", static_folder="static")


@exercise.route('/',  methods=["GET"])
def get_exercises():
    exercises = None
    return render_template("exercise/exercises.html", exercises=exercises)


@exercise.route('/<int:exercise_id>',  methods=["GET"])
def get_exercise(exercise_id):
    exercise = None
    return render_template("exercise/exercise.html", exercise=exercise)
