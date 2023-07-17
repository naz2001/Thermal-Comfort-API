# Thermal Comfort Prediction API

This API was created as a part of a final-year project for B.Tech. It uses FastAPI and Render to convert a thermal comfort prediction ML model into an API. The API can be used to predict the thermal comfort level of a person based on their clothing, activity, age, gender, temperature, humidity, and air velocity.

## Features

* Predicts the thermal comfort level of a person in the range of comfortable to highly uncomfortable.
* Scalable and can be deployed on a cloud platform like Render.
* Easy to use and can be accessed through a RESTful API.

## Usage

To use the API, you can send a request with the following data:

* Clothing: The type of clothing the person is wearing.
* Activity: The activity the person is performing.
* Age: The age of the person.
* Gender: The gender of the person.
* Temperature: The ambient temperature.
* Humidity: The ambient humidity.
* Air velocity: The air velocity.

The API will return the predicted thermal comfort level of the person, which can be one of the following:

* Comfortable
* Slightly uncomfortable
* Uncomfortable
* Very uncomfortable
* Highly uncomfortable

## Deployment

The API can be deployed on a cloud platform like Render. To do this, you will need to create a Render account and deploy the API code to Render.

## License

The API is licensed under the MIT License.
