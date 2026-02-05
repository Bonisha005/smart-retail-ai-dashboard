from flask import Flask, jsonify
from flask_cors import CORS
from model import predict_demand, inventory_recommendation

app = Flask(__name__)
CORS(app)

@app.route("/forecast", methods=["GET"])
def forecast():
    predicted = predict_demand(7)
    return jsonify({
        "day": 7,
        "predicted_demand": predicted
    })

@app.route("/inventory", methods=["GET"])
def inventory():
    current_stock = 150
    predicted = predict_demand(7)
    recommendation = inventory_recommendation(current_stock, predicted)

    return jsonify({
        "current_stock": current_stock,
        "predicted_demand": predicted,
        "recommendation": recommendation
    })

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
