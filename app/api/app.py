from flask import Flask, request, jsonify
from vision_model.inference.trash_classifier import classify_waste
from blockchain.web3_integration import RecyclingManager
import cv2
import numpy as np

app = Flask(__name__)
recycling_manager = RecyclingManager()

@app.route('/classify', methods=['POST'])
def classify():
    file = request.files['image']
    img = cv2.imdecode(np.frombuffer(file.read(), np.uint8), cv2.IMREAD_COLOR)
    prediction = classify_waste(img)
    return jsonify(prediction)

@app.route('/reward', methods=['POST'])
def reward_user():
    data = request.json
    tx_hash = recycling_manager.award_points(data['address'], data['amount'])
    return jsonify({'tx_hash': tx_hash.hex()})