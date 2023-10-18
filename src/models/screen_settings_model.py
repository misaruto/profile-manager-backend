from pydantic import BaseModel, Field

class ScreenSettingsModel(BaseModel):
  backgroundColor: str
  backgroundImageUrl: str
  fontSize: str
  fontColor: str
  fontFamily: str
  fontWeight: str
