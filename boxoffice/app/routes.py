from app import app
from flask import render_template, session, redirect, url_for, request
import pickle

from app.forms import DataForm
from app.predict import preprocess, predict, postprocess


app.config['SECRET_KEY'] = 'DAT158'


@app.route('/', methods=['GET', 'POST'])
@app.route('/index', methods=['GET', 'POST'])

def index():

    """
    We grab the form defined in `forms.py`. 
    If the form is submitted (and passes the validators) 
    then we grab all the values entered by the user and 
    predict. 
    """


    # Handle request from form
    form = DataForm()
    if form.validate_on_submit():

        # If the form is submitted and validated, store all the 
        # inputs in session
        for fieldname, value in form.data.items():
            session[fieldname] = value

        session['csrf_token'] = ''
        # Get additional user data
        user_info = request.headers.get('User-Agent')
        white = "\033[1;37;40m"
        print("\033[1;32;40m Preprocess  \n",white)
        # Preprocess data
        print(f"Pre preprocess: {session}")
        data = preprocess(session)
        print(f"Post preprocess: {data}")
        print("\033[1;32;40m Predict  \n",white)
        # Get model outputs 
        pred = predict(data)
        print("\033[1;32;40m Postprocess  \n",white)
        # Postprocess results
        pred = postprocess(pred)

        # Create the payload (we use session)
        session['user_info'] = user_info
        session['pred'] = pred


        return redirect(url_for('index'))

    return render_template('index.html', form=form)



@app.route('/dashboard')

def dashboard():
    return render_template('dashboard.html')
