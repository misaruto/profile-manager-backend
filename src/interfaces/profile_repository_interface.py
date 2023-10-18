from abc import ABC, abstractmethod
from src.models.profile_model import ProfileModel

class ProfileRepositoryInterface(ABC):
  
  @abstractmethod
  def select_profile(self,user_name:str,profile:str,session_id:str,transaction_id:str):
    raise NotImplementedError
  
  @abstractmethod
  def insert_profile(self,profile:ProfileModel,session_id:str,transaction_id:str):
    raise NotImplementedError
  
  @abstractmethod
  def update_profile(self,profile:ProfileModel,session_id:str,transaction_id:str):
    raise NotImplementedError

  @abstractmethod
  def delete_profile(self,user_name:str,profile_name:str,session_id:str,transaction_id:str):
    raise NotImplementedError