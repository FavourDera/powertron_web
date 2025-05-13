from pymongo import MongoClient
from pymongo.errors import ConnectionFailure
import os

# Your MongoDB connection string
MONGODB_URI = 'mongodb+srv://FavourDera:6zZzFMM0KsWI4WZ@cluster0.rjrcu3z.mongodb.net/powertron'

try:
    # Initialize MongoDB client with a longer timeout
    client = MongoClient(MONGODB_URI, serverSelectionTimeoutMS=10000)
    
    # Test the connection
    client.admin.command('ping')
    print("Successfully connected to MongoDB!")
    
    # List all databases
    print("\nAvailable databases:")
    for db_name in client.list_database_names():
        print(f"- {db_name}")
        
    # Get the powertron database
    db = client['powertron']
    print("\nCollections in powertron database:")
    for collection in db.list_collection_names():
        print(f"- {collection}")
        
except ConnectionFailure as e:
    print(f"Could not connect to MongoDB: {e}")
    print("\nTroubleshooting steps:")
    print("1. Check your internet connection")
    print("2. Verify your IP is whitelisted in MongoDB Atlas")
    print("3. Try accessing MongoDB Atlas through your web browser")
    print("4. Check if your firewall is blocking the connection")
except Exception as e:
    print(f"An unexpected error occurred: {e}")
finally:
    if 'client' in locals():
        client.close() 