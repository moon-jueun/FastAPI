from typing import Optional
from fastapi import FastAPI

from dbconn import DBconn
from models import DCM

app = FastAPI()
@app.get("/users/")
def read_root():
    return {"Hello": "World"}

@app.get("/items/{item_id}")
def read_item(item_id: int, q: Optional[str] = None):
    return {"item_id": item_id, "q": q}

class DataLoader:
    def __init__(self):
        self.dbconn = DBconn()
        self.engine = self.dbconn.get_db_engine()

if __name__ == '__main__':
    data = DataLoader()
    data.load_data()