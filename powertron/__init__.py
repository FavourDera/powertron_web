from flask import Flask
from powertron.extensions import mongo, socketio
import os
from dotenv import load_dotenv

load_dotenv()  # Load environment variables

app = Flask(__name__)
app.config['SECRET_KEY'] = os.getenv('SECRET_KEY', 'your-secret-key')
app.config['MONGO_URI'] = os.getenv('MONGODB_URI')

# Initialize extensions
mongo.init_app(app)
socketio.init_app(app)

# Import routes after app is created to avoid circular imports
from powertron import routes 