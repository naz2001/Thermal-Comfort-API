# -*- coding: utf-8 -*-
"""
Created on Thu May 11 14:23:56 2023

@author: Nazeeya
"""

from fastapi import FastAPI
from pydantic import BaseModel
import pickle
import json

app=FastAPI()

class model_input(BaseModel):
  Age:int
  Gender: int
  CurrentActivity: int
  Clothing:int
  Temperature:float
  Humidity:float
  WindSpeed:float

comfort_prediction = pickle.load(open('comfort_prediction.sav','rb'))

@app.post('/comfort_prediction')
def comfort_pred(input_parameters: model_input):
  input_data= input_parameters.json()
  input_dictionary= json.loads(input_data)
  age= input_dictionary['Age']
  gender= input_dictionary['Gender']
  ca= input_dictionary['CurrentActivity']
  cl= input_dictionary['Clothing']
  t= input_dictionary['Temperature']
  h= input_dictionary['Humidity']
  w= input_dictionary['WindSpeed']

  input_list=[age,gender,ca,cl,t,h,w]
  prediction = comfort_prediction.predict([input_list])

  if prediction[0] ==10:
    return 'Comfortable'
  elif prediction[0] ==20:
    return 'Slightly Uncomfortable'
  elif prediction[0] ==30:
    return 'Uncomfortable'
  elif prediction[0] ==40:
    return 'Very Uncomfortable'
  else:
    return 'Highly Uncomfortable'
