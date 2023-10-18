from flask_restful import Api
from src.resources.ProfileResource import ProfileResource

def config_resource_routes(api: Api):
  BASE_PATH_HTTP = ""
  api.add_resource(
    ProfileResource, 
    f"{BASE_PATH_HTTP}/profile/username/<string:user_name>/profilename/<string:profile_name>",
    methods=["GET", "POST", "PUT", "DELETE"],
    endpoint="ProfileResource"
  )
