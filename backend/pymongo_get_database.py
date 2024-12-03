from pymongo import MongoClient
import os
from dotenv import load_dotenv

load_dotenv()

def get_database():
    
    # Provide the connection string to connect to the database
    
    CONNECTION_STRING = os.getenv('DB_STRING')
    
    
    # Establish a connection using MongoClient
    
    client = MongoClient(CONNECTION_STRING)
    
    # creates a database
    return client ['CRUD_TODO_APP']

# Added for other files to reuse the get_database function
    
if __name__ == '__main__':
        
    dbname = get_database()


