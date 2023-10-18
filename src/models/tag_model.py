from pydantic import BaseModel
class TagModel(BaseModel):
  tagId: str
  tagName: str
  tagDescription: str
