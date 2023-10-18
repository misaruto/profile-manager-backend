from src.repository.profile_repository import ProfileRepository
from src.models.profile_model import ProfileModel
from src.interfaces.profile_repository_interface import ProfileRepositoryInterface
from src.interfaces.profiledb_interface import ProfileDbInterface
from src.utils.error_utils import ApiError

class ProfileService():
  def __init__(self,repository:ProfileDbInterface):
    self.profile_repository = ProfileRepository(repository)
  
  def get_profile(self,user_name:str,profile:str,session_id:str,transaction_id:str):
    try:
      profile = self.profile_repository.select_profile(user_name,profile,session_id,transaction_id)
      if not profile:
        raise ApiError(1)
      return profile,None
    except ApiError as e:
      return None,e.message

  def create_profile(self,profile:ProfileModel,session_id:str,transaction_id:str):
    try:
      resp =  self.profile_repository.insert_profile(profile,session_id,transaction_id)
      return resp,None
    except ApiError as e:
      return None,e.message
  
  def update_profile(self,profile:ProfileModel,session_id:str,transaction_id:str):
    try:
      old_profile = self.profile_repository.select_profile(profile.user_name,profile.profile_name,session_id,transaction_id)
      if not old_profile:
        raise ApiError(1)
      new_profile = ProfileModel(**old_profile.dict().update(profile.dict()))
      resp = self.profile_repository.update_profile(new_profile,session_id,transaction_id)
      return resp,None
    except ApiError as e:
      return None,e.message
  
  def delete_profile(self,user_name:str,profile_name:str,session_id:str,transaction_id:str):
    try:
      if profile_name == "default":
        raise ApiError(3)
      res = self.profile_repository.delete_profile(user_name,profile_name,session_id,transaction_id)
      return res,None
    except ApiError as e:
      return None,e.message