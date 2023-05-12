from fastapi import FastAPI
from pydantic import BaseModel
import pickle

app = FastAPI()

class model_input(BaseModel):
    Age: int
    Gender: int
    CurrentActivity: int
    Clothing: int
    Temperature: float
    Humidity: float
    WindSpeed: float

comfort_prediction = pickle.load(open('comfort_prediction.sav','rb'))

@app.post('/comfort_prediction')
def comfort_pred(input_parameters: model_input):
    age = input_parameters.Age
    gender = input_parameters.Gender
    ca = input_parameters.CurrentActivity
    cl = input_parameters.Clothing
    t = input_parameters.Temperature
    h = input_parameters.Humidity
    w = input_parameters.WindSpeed
    
    input_list = [age, gender, ca, cl, t, h, w]
    prediction = comfort_prediction.predict([input_list])
    
    if prediction[0] == 10:
        return 'Comfortable'
    elif prediction[0] == 20:
        return 'Slightly Uncomfortable'
    elif prediction[0] == 30:
        return 'Uncomfortable'
    elif prediction[0] == 40:
        return 'Very Uncomfortable'
    else:
        return 'Highly Uncomfortable'
