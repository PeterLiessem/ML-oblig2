from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, FloatField, SelectField, SelectField, RadioField, BooleanField, SubmitField
from wtforms.validators import DataRequired, NumberRange


class DataForm(FlaskForm):

    """
    The form for entering values during patient encounter. Feel free to add additional 
    fields for the remaining features in the data set (features missing in the form 
    are set to default values in `predict.py`).
    """

    budget = IntegerField('Budget', validators=[DataRequired()])
    popularity = IntegerField('Popularity', validators=[NumberRange(min=0, max=20)])
    runtime = IntegerField('Runtime', validators=[NumberRange(min=0, max=1000)])
    release_year = IntegerField('Release year.', validators=[NumberRange(min=1900, max=2021)])
    release_month = IntegerField('Release month.', validators=[NumberRange(min=1, max=12)])
    release_day = IntegerField('Release day of the month.', validators=[NumberRange(min=1, max=31)])
    release_wd = IntegerField('Release weekday.', validators=[NumberRange(min=1, max=7)])
    release_quarter = IntegerField('Release quarter.', validators=[NumberRange(min=1, max=4)])

    #bmi = FloatField('Average BMI during encounter')
    #sodium = FloatField('Average sodium level during encounter')

    homepage = BooleanField(label='homepage')
    genre_Comedy = BooleanField(label='genre_Comedy')
    genre_Drama = BooleanField(label='genre_Drama')
    genre_Thriller = BooleanField(label='genre_Thriller')
    genre_Action = BooleanField(label='genre_Action')
    genre_Animation = BooleanField(label='genre_Animation')
    genre_Horror = BooleanField(label='genre_Horror')
    genre_Documentary = BooleanField(label='genre_Documentary')
    genre_Adventure = BooleanField(label='genre_Adventure')
    genre_Crime = BooleanField(label='genre_Crime')
    genre_Mystery = BooleanField(label='genre_Mystery')
    genre_Fantasy = BooleanField(label='genre_Fantasy')
    genre_War = BooleanField(label='genre_War')
    genre_SF = BooleanField(label='genre_SF')
    genre_Romance = BooleanField(label='genre_Romance')
    genre_Music = BooleanField(label='genre_Music')
    genre_Western = BooleanField(label='genre_Western')
    genre_Family = BooleanField(label='genre_Family')
    genre_History = BooleanField(label='genre_History')
    genre_Foreign = BooleanField(label='genre_Foreign')
    genre_TM = BooleanField(label='genre_TM')
    in_collection = BooleanField(label='in_collection')
    has_tagline = BooleanField(label='has_tagline')




    submit = SubmitField('Submit')

