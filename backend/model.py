

from pydantic import BaseModel
from bson import ObjectId

class Todo(BaseModel):
    title: str
    description: str
    
class TodoCreate(Todo):
    id: str
    
    class Config:
        
        json_encoders = {
            ObjectId: str
        }