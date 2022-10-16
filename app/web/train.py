from flask import Blueprint, render_template, request, redirect, url_for

from app.crud.exercise import ExerciseCRUD
from app.crud.exercise_muscle import ExerciseMuscleCRUD
from app.crud.muscule import MuscleCRUD
from app.crud.train import TrainCRUD
from app.crud.train_exercise import TrainExerciseCRUD
from app.web.forms import ExerciseForm, MuscleForm, TrainForm, TrainExerciseForm, TrainExerciseUpdateForm

train = Blueprint('train', __name__, template_folder="templates", static_folder="static")


def get_train_verbose(user_id, train_id):
    t_crud = TrainCRUD()
    train_ = t_crud.get_by_id(user_id, train_id)
    t_e_crud = TrainExerciseCRUD()
    e_crud = ExerciseCRUD()
    train_exercises = t_e_crud.get_all(user_id, train_id)
    for train_exercise in train_exercises:
        train_exercise.update(e_crud.get_by_id(train_exercise["exercise_id"]))
    train_["train_exercises"] = train_exercises
    return train_


@train.route('/', methods=["GET"])
def get_trains():
    t_crud = TrainCRUD()
    user_id = 0
    trains = t_crud.get_all(user_id)
    return render_template("train/trains.html", trains=trains)


@train.route('/<int:train_id>', methods=["GET"])
def get_train(train_id):
    user_id = 0
    train_ = get_train_verbose(user_id, train_id)
    return render_template("train/train.html", train=train_)


@train.route('/new', methods=["GET", "POST"])
def create_train():
    form = TrainForm()
    if request.method == "POST" and form.validate_on_submit():
        t_crud = TrainCRUD()
        user_id = 0
        t_crud.create({"user_id": user_id, "name": form.name.data, "description": form.description.data})
        return redirect(url_for(".get_trains"))
    return render_template("train/new.html", form=form)


@train.route('/update/<int:train_id>', methods=["GET", "POST"])
def update_train(train_id):
    t_crud = TrainCRUD()
    user_id = 0
    form = TrainForm()
    if request.method == "POST" and form.validate_on_submit():
        t = {"train_id": form.train_id.data, "user_id": user_id, "name": form.name.data,
             "description": form.description.data}
        t_crud.update(t)
        return redirect(url_for(".get_trains"))
    t = t_crud.get_by_id(user_id, train_id)
    form.train_id.data = t["train_id"]
    form.name.data = t["name"]
    form.description.data = t["description"]
    return render_template("train/update.html", form=form)


@train.route('/train/<int:train_id>', methods=["GET"])
def delete_train(train_id):
    t_crud = TrainCRUD()
    user_id = 0
    t_crud.delete(user_id, train_id)
    return redirect(url_for(".get_trains"))


@train.route('/train_exercise/<int:train_id>', methods=["GET", "POST"])
def add_train_exercise(train_id):
    form = TrainExerciseForm()
    user_id = 0
    if request.method == "POST" and form.validate_on_submit():
        t_e_crud = TrainExerciseCRUD()
        e_crud = ExerciseCRUD()
        exercise_id = e_crud.get_by_name(form.name.data)["exercise_id"]
        sequence_number = t_e_crud.get_max_sequence_number(user_id, train_id) + 1
        t_e_crud.create({
            "sequence_number": sequence_number,
            "user_id": user_id, "train_id": train_id,
            "exercise_id": exercise_id,
            "reps": form.reps.data,
            "sets": form.sets.data,
            "timeout": form.timeout.data
        })
        return redirect(url_for(".add_train_exercise", train_id=train_id))

    train_ = get_train_verbose(user_id, train_id)
    return render_template("train/train_exercises.html", form=form, train=train_)


@train.route('/train_exercise/<int:train_id>?<int:sequence_number>', methods=["GET", "POST"])
def remove_train_exercise(train_id, sequence_number):
    user_id = 0
    t_e_crud = TrainExerciseCRUD()
    t_e_crud.delete(user_id, train_id, sequence_number)
    return redirect(url_for(".add_train_exercise", train_id=train_id))


@train.route('/train_exercise/update/<int:train_id>?<int:sequence_number>', methods=["GET", "POST"])
def update_train_exercise(train_id, sequence_number):
    form = TrainExerciseForm()
    user_id = 0
    t_e_crud = TrainExerciseCRUD()
    e_crud = ExerciseCRUD()
    if request.method == "POST" and form.validate_on_submit():
        exercise_id = e_crud.get_by_name(form.name.data)["exercise_id"]
        t_e = {"user_id": user_id, "sequence_number": form.sequence_number.data,
               "train_id": train_id, "exercise_id": exercise_id, "reps": form.reps.data, "sets": form.sets.data,
               "timeout": form.timeout.data}
        t_e_crud.update(t_e)
        return redirect(url_for(".add_train_exercise", train_id=train_id))
    t_e = t_e_crud.get_by_id(sequence_number, user_id, train_id)
    name = e_crud.get_by_id(t_e["exercise_id"])["name"]
    form.name.data = name
    form.sequence_number.data = t_e["sequence_number"]
    form.reps.data = t_e["reps"]
    form.sets.data = t_e["sets"]
    form.timeout.data = t_e["timeout"]
    return render_template("train/train_exercise_update.html", form=form)
