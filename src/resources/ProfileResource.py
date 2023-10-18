from flask import request
from flask_restful import Resource
from src.services.profile_service import ProfileService
from src.infra.db.profile_dynamodb_conection import ProfileDb
from src.utils.response_utils import resp_error, resp_ok
from src.models.profile_model import ProfileModel

RESOURCE_NAME = "ProfileResource"

class ProfileResource(Resource):
  """
    Profile Resource
  """
  def __init__(self):
    self.profile_service = ProfileService(ProfileDb())
    self.session_id = request.headers.get("session_id")
    self.transaction_id = request.headers.get("transaction_id")

  def get(self,user_name,profile_name) -> tuple:
    """
      Get profile by user name and profile name
    """
    profile,error = self.profile_service.get_profile(user_name,profile_name,self.session_id,self.transaction_id)
    if error:
      return resp_error(resource=RESOURCE_NAME,errors=error,transaction_id=self.transaction_id)
    return resp_ok(resource=RESOURCE_NAME, data=profile.dict())

  def post(self,user_name,profile_name) -> tuple:
    """
      Create profile by user name and profile name
    """
    
    request_data = request.get_json()
    profile = ProfileModel(**request_data)

    profile.user_name = user_name
    profile.profile_name = profile_name

    profile,error = self.profile_service.create_profile(profile,self.session_id,self.transaction_id)
    
    if error:
      return resp_error(resource=RESOURCE_NAME,errors=error,transaction_id=self.transaction_id)
    return resp_ok(status=201, resource=RESOURCE_NAME, data=profile.dict())

  def put(self,user_name,profile_name) -> tuple:
    """
      Update profile by user name and profile name
    """
    
    request_data = request.get_json()
    
    profile = ProfileModel(**request_data)

    profile.user_name = user_name
    profile.profile_name = profile_name

    profile,error = self.profile_service.update_profile(profile,self.session_id,self.transaction_id)
    
    if error:
      return resp_error(resource=RESOURCE_NAME,errors=error,transaction_id=self.transaction_id)
    return resp_ok(resource=RESOURCE_NAME, data=profile.dict())

  def delete(self,user_name,profile_name) -> tuple:
    """
      Delete profile by user name and profile name
    """

    profile,error = self.profile_service.delete_profile(user_name,profile_name,self.session_id,self.transaction_id)

    if error:
      return resp_error(resource=RESOURCE_NAME,errors=error,transaction_id=self.transaction_id)
    return resp_ok(resource=RESOURCE_NAME, data=profile.dict())


