import numpy as np
import pandas as pd
import joblib

####### 
## Get the model trained in the notebook 
# `../nbs/1.0-asl-train_model.ipynb`
#######

model = joblib.load('models/LinSVR.joblib')


def preprocess(data):
    """
    Returns the features entered by the user in the web form. 

    To simplify, we set a bunch of default values. 
            For bools and ints, use the most frequent value
            For floats, use the median value

    Note that this represent some major assumptions that you'd 
    not want to make in real life. If you want to use default 
    values for some features then you'll have to think more 
    carefully about what they should be. 

    F.ex. if the user doesn't provide a value for BMI, 
    then one could use a value that makes more sense than 
    below. For example, the mean for the given gender would 
    at least be a bit more correct. 
    
    Having _dynamic defaults_ is important. And of course, if 
    relevant, getting some of the features without asking the user. 
    E.g. if the user is logged in and you can pull information 
    form a user profile. Or if you can compute or obtain the information 
    thorugh other means (e.g. user location if shared etc).
    """


    feature_values = {
        'budget' : 1000, #TODO
        'homepage' : 0, 
        'popularity' : 10,
        'runtime' : 0,
        'genre_Comedy' : 0,
        'genre_Drama' : 0,
        'genre_Thriller' : 0,
        'genre_Action' : 0,
        'genre_Animation' : 0,
        'genre_Horror' : 0,
        'genre_Documentary' : 0,
        'genre_Adventure' : 0,
        'genre_Crime' : 0,
        'genre_Mystery' : 0,
        'genre_Fantasy' : 0,
        'genre_War' : 0,
        'genre_SF' : 0,
        'genre_Romance' : 0,
        'genre_Music' : 0,
        'genre_Western' : 0,
        'genre_Family' : 0,
        'genre_History' : 0,
        'genre_Foreign' : 0,
        'genre_TM' : 0,
        'in_collection' : 0,
        'has_tagline' : 0,
        'release_year' : 2000,
        'release_month' : 1,
        'release_day' : 1,
        'release_wd' : 1,
        'release_quarter' : 1
    }


    # Parse the form inputs and return the defaults updated with values entered.
    print()
    print("keys: ",data.keys())
    print()
    for key in [k for k in data.keys() if k in feature_values.keys()]:
        feature_values[key] = data[key]

    return feature_values



####### 
## Now we can predict with the trained model:
#######


def predict(data):
    """
    If debug, print various useful info to the terminal.
    """
 
    # Store the data in an array in the correct order:

    column_order = ['budget', 'homepage', 'popularity', 'runtime', 'genre_Comedy',
       'genre_Drama', 'genre_Thriller', 'genre_Action', 'genre_Animation',
       'genre_Horror', 'genre_Documentary', 'genre_Adventure', 'genre_Crime',
       'genre_Mystery', 'genre_Fantasy', 'genre_War', 'genre_SF',
       'genre_Romance', 'genre_Music', 'genre_Western', 'genre_Family',
       'genre_History', 'genre_Foreign', 'genre_TM', 'in_collection',
       'has_tagline', 'release_year', 'release_month', 'release_day',
       'release_wd', 'release_quarter']
    #data = np.array([data[feature] for feature in column_order], dtype=object)
    
    
    
    for i, e in enumerate(column_order):
        if type(data[e]) == type(True):
            if data[e]:
                data[e] = 1
            else:
                data[e] = 0
        #data2[e] = data[i]
    #data2 = pd.json_normalize(data)
    #print(data2)
    data = np.array([data[feature] for feature in column_order], dtype=object)
    #data = np.array(data, dtype=object)

    # NB: In this case we didn't do any preprocessing of the data before 
    # training our random forest model (see the notebool `nbs/1.0-asl-train_model.ipynb`). 
    # If you plan to feed the training data through a preprocessing pipeline in your 
    # own work, make sure you do the same to the data entered by the user before 
    # predicting with the trained model. This can be achieved by saving an entire 
    # sckikit-learn pipeline, for example using joblib as in the notebook.
    print(data)
    pred = model.predict(data.reshape(1,-1))
    print(str(pred[0]))
    #white = "\033[1;37;40m"
    #print("\033[1;32;40m    ",pred,white)
    #uncertainty = model.predict_proba(data2)#.reshape(1,-1))
    #print("\033[1;32;40m    ",uncertainty,white)
    return pred


def postprocess(prediction):
    """
    Apply postprocessing to the prediction. E.g. validate the output value, add
    additional information etc. 
    """

    pred = prediction

    # Validate. As an example, if the output is an int, check that it is positive.
    """try: 
        int(pred[0]) > 0
    except:
        pass
    """
    # Make strings
    pred = str(pred[0])


    # Return
    return_dict = {'pred': pred}

    return return_dict