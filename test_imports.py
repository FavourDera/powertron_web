try:
    import flask_socketio
    print("✓ Flask-SocketIO is installed")
except ImportError as e:
    print("✗ Flask-SocketIO error:", e)

try:
    import pymongo
    print("✓ PyMongo is installed")
except ImportError as e:
    print("✗ PyMongo error:", e)

try:
    from pymongo.errors import ConnectionFailure
    print("✓ pymongo.errors is installed")
except ImportError as e:
    print("✗ pymongo.errors error:", e) 