import pickle
import json
import pandas as pd
import numpy as np
from flask import Flask
from flask import request
from flask import jsonify

output_file = 'model_V1.0.bin'


with open(output_file, 'rb') as f_in:
    model, dv, columns = pickle.load(f_in)

def read_data(house_detail_raw):
    house_df = pd.DataFrame(house_detail_raw)
    house_df = house_df[columns]
    house_df.fillna(0, inplace=True)
    house_df['age'] = 2023 - house_df['YearBuilt']
    house_detail_dict = house_df.to_dict(orient='records')
    return house_detail_dict


app = Flask('house_price')

@app.route('/predict', methods=['POST'])
def predict():
    house_detail_raw = request.get_json()
    house_detail_raw = json.loads(house_detail_raw)
    house_detail_dict = read_data(house_detail_raw)
    X_test = dv.transform(house_detail_dict)
    y_pred = np.expm1(model.predict(X_test)).tolist()

    result =  {
        'house_price_prediction': y_pred
    }

    return jsonify(result)

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=9696)