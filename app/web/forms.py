from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, IntegerField, FieldList, FormField, \
    SelectField
from wtforms.validators import DataRequired

from app.crud.muscule import MuscleCRUD


class MuscleForm(FlaskForm):
    name = SelectField('Задействованные мышцы', choices=[muscle["name"] for muscle in MuscleCRUD().get_all()])
    submit = SubmitField('Добавить')


class ExerciseForm(FlaskForm):
    exercise_id = IntegerField('id')
    name = StringField('Название', validators=[DataRequired()])
    description = StringField('Описание', validators=[DataRequired()])
    submit = SubmitField('Сохранить')
