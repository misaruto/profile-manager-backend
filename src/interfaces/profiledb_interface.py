from abc import ABC, abstractmethod
from src.models.profile_model import ProfileModel

class ProfileDbInterface(ABC):
  
  @abstractmethod
  def select(self,user_name:str,profile:str,session_id:str,transaction_id:str) -> ProfileModel:
    raise NotImplementedError
  
  @abstractmethod
  def insert(self,profile:ProfileModel,session_id:str,transaction_id:str):
    raise NotImplementedError
  
  @abstractmethod
  def update(self,profile:ProfileModel,session_id:str,transaction_id:str):
    raise NotImplementedError

  @abstractmethod
  def delete(self,user_name:str,profile_name:str,session_id:str,transaction_id:str):
    raise NotImplementedError