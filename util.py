import json
import pickle
import numpy as np
import warnings
warnings.filterwarnings("ignore", category=UserWarning)

__data_columns=None
__locations=None
__model=None

def get_estimated_price(location,sqft,bhk,bath):
    try:
        loc_index=__locations.index(location.lower())
    except:
        loc_index=-1
    x=np.zeros(len(__data_columns))
    x[0]=sqft
    x[1]=bhk
    x[2]=bath
    if loc_index>=0:
        x[loc_index]=1
    return __model.predict([x])[0]
def load_saved_artifacts():

    global __locations
    global __data_columns
    with open('./artifacts/columns.json','r')  as f:
        __data_columns=json.load(f)['data columns']

        __locations=__data_columns[3:]

    global __model
    with open('./artifacts/banglore_house_prices_model.pkl','rb') as f:
        __model=pickle.load(f)

def get_locations():
    if __locations is None:
        load_saved_artifacts()
    return __locations

def get_data_columns():
    load_saved_artifacts()

    return __data_columns

if __name__=='__main__':
    load_saved_artifacts()
    print(get_estimated_price('1st block jayanagar',2500,3,3))
    print(get_locations())