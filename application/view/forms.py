from flask_wtf import FlaskForm
from wtforms import SearchField, SubmitField, SelectField, RadioField
from wtforms.validators import Length, DataRequired
from ..model import importTickers as TIC

class LookUpForm(FlaskForm):
    #attributes of the form
    #validators constrain the inputs
    ticField = SearchField(
        'TickerField',
        validators=[Length(min=1, max=8)],

    )
    tics = TIC.getTickers()
    ticField2 = SelectField(
        'TickerField2',
        choices=tics,
        render_kw={'disabled':''},
        validators=[DataRequired()]
    )
    choiceField = RadioField('optionField')
    submitButton = SubmitField('Submit')