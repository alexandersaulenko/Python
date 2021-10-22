from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, Length, Email

class createincident_form(FlaskForm):
    submitter_name = StringField('submitter_name',
                                 validators=[DataRequired(), Length(min=5, max=100)])

    submitter_email =  StringField('submitter_email',
                                   validators=[DataRequired(), Email()])

    incident_name = StringField('incident_name',
                                 validators=[DataRequired(), Length(min=2, max=100)])

    incident_type = StringField('incident_type')

    incident_text = StringField('incident_text',
                                 validators=[DataRequired()])

    submit = SubmitField('submit')