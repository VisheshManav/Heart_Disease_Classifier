import requests

host = 'localhost:9696'
url= f'http://{host}/predict'

patient = {"age": 0.125,
    "sex": "male",
    "cp": "asymtomatic",
    "trestbps": 0.30188679245283023,
    "chol": 0.35616438356164376,
    "fbs": "false",
    "restecg": "left_ventricular_hypertrophy",
    "thalach": 0.648854961832061,
    "exang": "yes",
    "oldpeak": 0.0,
    "slope": "upsloping",
    "ca": "zero",
    "thal": "reversable_defect"
 }

response = requests.post(url, json=patient).json()
print(response)
