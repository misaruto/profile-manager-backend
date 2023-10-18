from src.models.profile_model import ProfileModel
from src.interfaces.profiledb_interface import ProfileDbInterface
from src.interfaces.profile_repository_interface import ProfileRepositoryInterface
import logging

class ProfileRepository(ProfileRepositoryInterface):
    def __init__(self,connection:ProfileDbInterface):
        self.db_connection = connection

    def select_profile(self,user_name:str,profile='default',session_id="",transaction_id=""):
        logging.info(f"Buscando perfil {user_name} {profile}")
        profile =  self.db_connection.select(user_name,profile,session_id,transaction_id)
        if not profile:
            logging.info(f"Perfil {user_name} {profile} no encontrado")
            return None
        logging.info(f"Perfil {user_name} {profile} encontrado")
        return profile
    
    def insert_profile(self,profile:ProfileModel,session_id="",transaction_id=""):
        return self.db_connection.insert(profile, session_id, transaction_id)
    
    def update_profile(self,profile:ProfileModel,session_id="",transaction_id=""):
        return self.db_connection.update(profile, session_id, transaction_id)
    
    def delete_profile(self,user_name:str,profile_name:str,session_id="",transaction_id=""):
        return self.db_connection.delete(user_name, profile_name, session_id, transaction_id)