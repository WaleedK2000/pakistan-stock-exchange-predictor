from flask import Flask, request, jsonify
import joblib


# Create Flask application
app = Flask(__name__)

# Load model


model = joblib.load('./model/model.pkl')

# Define endpoint for model prediction


@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json()
    open_price = data['Open']
    high_price = data['High']
    low_price = data['Low']
    volume = data['Volume']
    prediction = model.predict([[open_price, high_price, low_price, volume]])
    return jsonify({'prediction': prediction.tolist()})


# Run Flask application
if __name__ == '__main__':
    app.run(debug=True)
