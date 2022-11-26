import requests

host = 'localhost:9696'
url= f'http://{host}/predict'

patient = {"age": 57,
    "sex": "female",
    "cp": "asymtomatic",
    "trestbps": 128,
    "chol": 303,
    "fbs": "false",
    "restecg": "left_ventricular_hypertrophy",
    "thalach": 159,
    "exang": "no",
    "oldpeak": 0.0,
    "slope": "upsloping",
    "ca": "one",
    "thal": "normal"
}

response = requests.post(url, json=patient).json()
print(response)
