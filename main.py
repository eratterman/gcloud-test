import re
from fastapi import FastAPI
from tools import DbConnect
from pydantic import BaseModel, validator


RE_TAG = re.compile(r'^[a-z_]+')
DB = DbConnect()


# set up names model
class Tags(BaseModel):
    name: str
    value: int

    @validator('name')
    def validate_name_value(cls, v):
        if not RE_TAG.fullmatch(v):
            raise ValueError('Name must be lowercase a-z to include underscores.')

        if len(v) not in range(3, 15):
            raise ValueError('Name must be 3 to 14 characters long.')

        return v

    @validator('value')
    def validate_integer_value(cls, v):
        if v not in range(0, 10):
            raise ValueError('Value must be positive integer less than 10.')

        return v


app = FastAPI()


@app.get('/')
async def hello():
    return "Hello! Welcome to Eric's Juvi Whale API."


@app.get('/get_tag_stats')
async def get_tag_stats():
    tags = DB.get_documents()
    return tags


@app.post('/increment_tag')
async def increment_tag(new_tag: Tags):
    json_dict = new_tag.dict()
    return DB.add_document(
        json_dict.get('name', ''), json_dict.get('value', 0)
    )
