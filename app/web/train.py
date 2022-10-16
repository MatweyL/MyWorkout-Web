from flask import Blueprint, render_template, request, redirect, url_for

from app.crud.exercise import ExerciseCRUD
from app.crud.exercise_muscle import ExerciseMuscleCRUD
from app.crud.muscule import MuscleCRUD
from app.crud.train import TrainCRUD
from app.crud.train_exercise import TrainExerciseCRUD
from app.web.forms import ExerciseForm, MuscleForm

train = Blueprint('train', __name__, template_folder="templates", static_folder="static")


@train.route('/',  methods=["GET"])
def get_trains():
    t_crud = TrainCRUD()
    user_id = 0
    trains = t_crud.get_all(user_id)
    return render_template("train/trains.html", trains=trains)


@train.route('/<int:train_id>',  methods=["GET"])
def get_train(train_id):
    t_crud = TrainCRUD()
    user_id = 0
    train_ = t_crud.get_by_id(user_id, train_id)
    t_e_crud = TrainExerciseCRUD()
    e_crud = ExerciseCRUD()
    train_exercises = t_e_crud.get_all(user_id, train_id)
    for train_exercise in train_exercises:
        train_exercise.update(e_crud.get_by_id(train_exercise["exercise_id"]))
    train_["train_exercises"] = train_exercises
    print(train_exercises)
    return render_template("train/train.html", train=train_)

