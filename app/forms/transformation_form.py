from flask_wtf import FlaskForm
from wtforms import SubmitField, SelectField, FloatField
from wtforms.validators import DataRequired
from wtforms.widgets import NumberInput
from app.utils.list_images import list_images
from config import Configuration

conf = Configuration()


class TransformationForm(FlaskForm):
    color = FloatField(widget=NumberInput(step=0.1, min=-10.0, max=10.0), default=1.0, validators=[DataRequired()])
    brightness = FloatField(widget=NumberInput(step=0.1, min=-10.0, max=10.0), default=1.0, validators=[DataRequired()])
    contrast = FloatField(widget=NumberInput(step=0.1, min=-10.0, max=10.0), default=1.0, validators=[DataRequired()])
    sharpness = FloatField(widget=NumberInput(step=0.1, min=-10.0, max=10.0), default=1.0, validators=[DataRequired()])

    image = SelectField('image', choices=list_images(), validators=[DataRequired()])
    submit = SubmitField('Submit')
