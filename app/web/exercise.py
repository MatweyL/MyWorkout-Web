from flask import Blueprint, render_template

from app.crud.exercise import ExerciseCRUD

exercise = Blueprint('exercise', __name__, template_folder="templates", static_folder="static")


@exercise.route('/',  methods=["GET"])
def get_exercises():
    e_crud = ExerciseCRUD()
    exercises = e_crud.get_all()
    return render_template("exercise/exercises.html", exercises=exercises)


@exercise.route('/<int:exercise_id>',  methods=["GET"])
def get_exercise(exercise_id):
    e_crud = ExerciseCRUD()
    exercise_ = e_crud.get_by_id(exercise_id)
    return render_template("exercise/exercise.html", exercise=exercise_)


@exercise.route('/<int:exercise_id>/update',  methods=["PUT"])
def update_exercise(exercise_id):
    e_crud = ExerciseCRUD()
    exercise_ = e_crud.get_by_id(exercise_id)
    return render_template("exercise/exercise.html", exercise=exercise_)


@exercise.route('/<int:exercise_id>',  methods=["DELETE"])
def delete_exercise(exercise_id):
    e_crud = ExerciseCRUD()
    exercise_ = e_crud.get_by_id(exercise_id)
    return render_template("exercise/exercise.html", exercise=exercise_)
