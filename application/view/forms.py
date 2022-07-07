from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField, RadioField
from wtforms.validators import Length, DataRequired, Optional
from ..model import importTickers as TIC

class LookUpForm(FlaskForm):
    #attributes of the form
    #validators constrain the inputs
    ticField = StringField(
        'TickerField',
        validators=[Length(min=1, max=8)],

    )
    tics = TIC.getTickers()
    ticField2 = SelectField(
        'TickerField2',
        choices=tics,
        render_kw={'disabled':''}
    )
    submitButton = SubmitField('Submit')