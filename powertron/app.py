from flask import render_template, url_for, session, redirect, request, jsonify
import requests
from datetime import datetime, timezone
import cloudinary.uploader
import os
from passlib.hash import pbkdf2_sha256
from werkzeug.exceptions import RequestEntityTooLarge
from powertron.extensions import mongo, socketio
from powertron.decorators import login_required, is_lecturer
import powertron.models as models
from dotenv import load_dotenv
from powertron.power_bot import get_power_bot_response

load_dotenv()

# Get the app instance from extensions
from powertron import app

@app.route('/test_db')
def test_db():
    try:
        # Attempt to fetch documents from users collection
        users = mongo.db.users.find_one()
        return jsonify({"message": "Successfully connected to MongoDB!", "status": "success"})
    except Exception as e:
        return jsonify({"message": f"Failed to connect to MongoDB: {str(e)}", "status": "error"})

@app.route('/')
def home():
    return "Hello, Powertron!"

@app.route('/powerbot/chat', methods=['POST'])
def powerbot_chat():
    user_message = request.json.get('message')
    bot_response = get_power_bot_response(user_message)
    return jsonify({'response': bot_response})

@app.route('/powerbot')
def powerbot_page():
    return render_template('powerbot.html') 