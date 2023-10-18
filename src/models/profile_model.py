from pydantic import BaseModel
from src.models.screen_settings_model import ScreenSettingsModel
from src.models.tag_model import TagModel

class ProfileModel(BaseModel):
  userName: str
  profileName: str 
  userDescription: str
  userTags: list[TagModel]
  screenSettings: ScreenSettingsModel
  createdAt: str
  updatedAt: str
