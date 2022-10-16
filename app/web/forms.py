from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, IntegerField, FieldList, FormField, \
    SelectField
from wtforms.validators import DataRequired

from app.crud.exercise import ExerciseCRUD
from app.crud.muscule import MuscleCRUD


class MuscleForm(FlaskForm):
    name = SelectField('Задействованные мышцы')
    submit = SubmitField('Добавить', render_kw={"class": "btn btn-primary"})


class ExerciseForm(FlaskForm):
    id = IntegerField('id', render_kw={"class": "d-none"})
    name = StringField('Название', validators=[DataRequired()], render_kw={"class": "form-control"})
    description = StringField('Описание', validators=[DataRequired()], render_kw={"class": "form-control"})
    submit = SubmitField('Сохранить', render_kw={"class": "btn btn-primary"})


class TrainExerciseForm(FlaskForm):
    name = SelectField('Упражнение')
    sequence_number = IntegerField('Номер упражнения', render_kw={"class": "d-none"})
    reps = IntegerField('Повторения', validators=[DataRequired()], render_kw={"class": "form-control"})
    sets = IntegerField('Подходы', validators=[DataRequired()], render_kw={"class": "form-control"})
    timeout = IntegerField('Отдых', validators=[DataRequired()], render_kw={"class": "form-control"})
    submit = SubmitField('Добавить', render_kw={"class": "btn btn-primary"})


class TrainExerciseUpdateForm(FlaskForm):
    name = SelectField('Упражнение')
    sequence_number = IntegerField('Номер упражнения', validators=[DataRequired()], render_kw={"class": "d-none"})
    reps = IntegerField('Повторения', validators=[DataRequired()], render_kw={"class": "form-control"})
    sets = IntegerField('Подходы', validators=[DataRequired()], render_kw={"class": "form-control"})
    timeout = IntegerField('Отдых', validators=[DataRequired()], render_kw={"class": "form-control"})
    submit = SubmitField('Добавить', render_kw={"class": "btn btn-primary"})


class TrainForm(FlaskForm):
    id = IntegerField('id', render_kw={"class": "d-none"})
    name = StringField('Название', validators=[DataRequired()], render_kw={"class": "form-control"})
    description = StringField('Описание', validators=[DataRequired()], render_kw={"class": "form-control"})
    submit = SubmitField('Сохранить', render_kw={"class": "btn btn-primary"})


class LoginForm(FlaskForm):
    email = StringField("Почта", validators=[DataRequired()], render_kw={"class": "form-control"})
    password = PasswordField("Пароль", validators=[DataRequired()], render_kw={"class": "form-control"})
    submit = SubmitField('Войти', render_kw={"class": "btn btn-primary"})


class RegisterForm(FlaskForm):
    nickname = StringField("Имя", validators=[DataRequired()], render_kw={"class": "form-control"})
    email = StringField("Почта", validators=[DataRequired()], render_kw={"class": "form-control"})
    password = PasswordField("Пароль", validators=[DataRequired()], render_kw={"class": "form-control"})
    submit = SubmitField('Зарегистрироваться', render_kw={"class": "btn btn-primary"})
