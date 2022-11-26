import pickle
from flask import Flask
from flask import request
from flask import jsonify

model_file = 'model_lr.bin'

with open(model_file, 'rb') as f_in:
    dv, model = pickle.load(f_in)

app = Flask('heartD')

@app.route('/predict', methods=['POST'])
def predict():
    patient = request.get_json()

    X = dv.transform([patient])
    y_pred = model.predict_proba(X)[0, 1]
    disease = y_pred > 0.5

    result = {
        'disease_probability': float(y_pred),
        'disease': bool(disease)
    }

    return jsonify(result)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=9696)