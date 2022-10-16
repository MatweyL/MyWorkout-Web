from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, IntegerField, FieldList, FormField, \
    SelectField
from wtforms.validators import DataRequired

from app.crud.exercise import ExerciseCRUD
from app.crud.muscule import MuscleCRUD


class MuscleForm(FlaskForm):
    name = SelectField('Задействованные мышцы')
    submit = SubmitField('Добавить')


class ExerciseForm(FlaskForm):
    id = IntegerField('id')
    name = StringField('Название', validators=[DataRequired()])
    description = StringField('Описание', validators=[DataRequired()])
    submit = SubmitField('Сохранить')


class TrainExerciseForm(FlaskForm):
    name = SelectField('Упражнение')
    sequence_number = IntegerField('Номер упражнения')
    reps = IntegerField('Повторения', validators=[DataRequired()])
    sets = IntegerField('Подходы', validators=[DataRequired()])
    timeout = IntegerField('Отдых', validators=[DataRequired()])
    submit = SubmitField('Добавить')


class TrainExerciseUpdateForm(FlaskForm):
    name = SelectField('Упражнение')
    sequence_number = IntegerField('Номер упражнения', validators=[DataRequired()])
    reps = IntegerField('Повторения', validators=[DataRequired()])
    sets = IntegerField('Подходы', validators=[DataRequired()])
    timeout = IntegerField('Отдых', validators=[DataRequired()])
    submit = SubmitField('Добавить')


class TrainForm(FlaskForm):
    id = IntegerField('id')
    name = StringField('Название', validators=[DataRequired()])
    description = StringField('Описание', validators=[DataRequired()])
    submit = SubmitField('Сохранить')


class LoginForm(FlaskForm):
    email = StringField("Почта", validators=[DataRequired()])
    password = PasswordField("Пароль", validators=[DataRequired()])
    submit = SubmitField('Войти')


class RegisterForm(FlaskForm):
    nickname = StringField("Имя", validators=[DataRequired()])
    email = StringField("Почта", validators=[DataRequired()])
    password = PasswordField("Пароль", validators=[DataRequired()])
    submit = SubmitField('Войти')
