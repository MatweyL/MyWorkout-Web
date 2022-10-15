import logging

from flask import Blueprint, render_template, request, redirect, url_for

from app.crud.exercise import ExerciseCRUD
from app.crud.exercise_muscle import ExerciseMuscleCRUD
from app.crud.muscule import MuscleCRUD
from app.web.forms import ExerciseForm, MuscleForm

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
    e_m_crud = ExerciseMuscleCRUD()
    m_crud = MuscleCRUD()
    exercise_["muscles"] = m_crud.get_by_ids(e_m_crud.get_muscles_ids(exercise_id))
    return render_template("exercise/exercise.html", exercise=exercise_)


@exercise.route('/new',  methods=["GET", "POST"])
def create_exercise():
    form = ExerciseForm()
    if request.method == "POST" and form.validate_on_submit():
        e_crud = ExerciseCRUD()
        e_crud.create({"name": form.name.data, "description": form.description.data})
        return redirect("/exercises")

    return render_template("exercise/new.html", form=form)


@exercise.route('/update/<int:exercise_id>',  methods=["GET", "POST"])
def update_exercise(exercise_id):
    e_crud = ExerciseCRUD()
    form = ExerciseForm()
    if request.method == "POST" and form.validate_on_submit():
        e = {"exercise_id": form.exercise_id.data, "name": form.name.data, "description": form.description.data}
        e_crud.update(e)
        return redirect("/exercises")
    e = e_crud.get_by_id(exercise_id)
    form.exercise_id.data = e["exercise_id"]
    form.name.data = e["name"]
    form.description.data = e["description"]
    return render_template("exercise/update.html", form=form)


@exercise.route('/delete/<int:exercise_id>',  methods=["GET"])
def delete_exercise(exercise_id):
    e_crud = ExerciseCRUD()
    e_crud.delete(exercise_id)
    return redirect("/exercise")


@exercise.route('/muscle/<int:exercise_id>', methods=["GET", "POST"])
def add_muscle(exercise_id):
    form = MuscleForm()
    if request.method == "POST" and form.validate_on_submit():
        m_crud = MuscleCRUD()
        muscle_id = m_crud.get_by_name(form.name.data)["muscle_id"]
        e_m_crud = ExerciseMuscleCRUD()
        e_m_crud.set_muscle(exercise_id, muscle_id)
        return redirect(url_for(f'.add_muscle', exercise_id=exercise_id))
    e_crud = ExerciseCRUD()
    e = e_crud.get_by_id(exercise_id)
    e_m_crud = ExerciseMuscleCRUD()
    m_crud = MuscleCRUD()
    e["muscles"] = m_crud.get_by_ids(e_m_crud.get_muscles_ids(exercise_id))
    return render_template("exercise/muscles.html", form=form, exercise=e)


@exercise.route('/muscle/<int:exercise_id>?<int:muscle_id>', methods=["GET"])
def remove_muscle(exercise_id, muscle_id):
    e_m_crud = ExerciseMuscleCRUD()
    e_m_crud.remove_muscle(exercise_id, muscle_id)
    return redirect(f"/exercises/muscle/{exercise_id}")
