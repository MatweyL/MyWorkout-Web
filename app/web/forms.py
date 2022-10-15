from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, IntegerField, FieldList, FormField, \
    SelectField
from wtforms.validators import DataRequired


class MuscleForm(FlaskForm):
    muscle_id = IntegerField('id')
    name = SelectField(choices=["e", "2", "d"])


class ExerciseForm(FlaskForm):
    exercise_id = IntegerField('id')
    name = StringField('Название', validators=[DataRequired()])
    description = StringField('Описание', validators=[DataRequired()])
    muscles = FieldList(FormField(MuscleForm), min_entries=1, max_entries=2)
    submit = SubmitField('Сохранить')
