from flask import jsonify, session, redirect, url_for, request
from powertron.extensions import mongo
from passlib.hash import pbkdf2_sha256

class User:
    def signup(self):
        user = {
            "_id": request.form.get('email'),
            "first_name": request.form.get('first_name'),
            "last_name": request.form.get('last_name'),
            "email": request.form.get('email'),
            "password": request.form.get('password'),
            "category": "student",
            "current_level": "100 Level"
        }
        
        # Encrypt password
        user['password'] = pbkdf2_sha256.encrypt(user['password'])
        
        # Check if user exists
        if mongo.db.users.find_one({"email": user['email']}):
            return jsonify({"error": "Email address already in use"}), 400
        
        # Insert user
        if mongo.db.users.insert_one(user):
            return self.start_session(user)
        
        return jsonify({"error": "Signup failed"}), 400
    
    def start_session(self, user):
        del user['password']
        session['logged_in'] = True
        session['user'] = user
        return redirect(url_for('dashboard', user=user['_id'])) 