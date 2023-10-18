import logging
import os

import boto3
from boto3.dynamodb.conditions import Key
from botocore.config import Config
from src.interfaces.profiledb_interface import ProfileDbInterface
from src.models.profile_model import ProfileModel

class ProfileDb(ProfileDbInterface):
    def __init__(self):
        config = Config(connect_timeout=1, read_timeout=1, retries={"max_attempts": 2})
        self._tabela = boto3.resource(
            "dynamodb", 
            config=config,
            endpoint_url=os.environ.get("AWS_DYNAMO_DB_ENDPOINT",None),
            aws_access_key_id="fakeSecretAccessKey", aws_secret_access_key="fakeMyKeyId"
        ).Table(
            os.environ.get("PROFILE_TABLE", "profile")
        )
    
    def select(
        self,
        user_name:str,
        profile='default',
        session_id="",
        transaction_id=""
    ) -> ProfileModel:
        retorno = self._tabela.query(
            KeyConditionExpression=Key("username").eq(str(user_name))
            & Key("profileName").eq(str(profile)),
            ReturnConsumedCapacity="TOTAL",
        )
        logging.info(
            "Tabela %s, capacityUnits %s, session_id %s, transaction_id %s",
            retorno.get("ConsumedCapacity", {}).get("TableName"),
            retorno.get("ConsumedCapacity", {}).get("CapacityUnits"),
            session_id,
            transaction_id,
        )
        if retorno and retorno.get("Count") > 0:
            retorno = retorno.get("Items")[0]
        else:
            retorno = {}
        return retorno
    
    def insert(
        self,
        profile,
        session_id="",
        transaction_id=""
    ):
        return self.__upsert(profile, session_id, transaction_id)

    def update(
        self,
        profile,
        session_id="",
        transaction_id=""
    ):
        return self.__upsert(profile, session_id, transaction_id)

    def __upsert(
        self, profile, session_id="", transaction_id=""
    ):
        """
        Create or update profile
        """
        retorno = self._tabela.put_item(
            Item=profile, ReturnConsumedCapacity="TOTAL", ReturnItemCollectionMetrics="SIZE"
        )
        logging.info(
            "Tabela %s, capacityUnits %s, session_id %s, transaction_id %s",
            retorno.get("ConsumedCapacity", {}).get("TableName"),
            retorno.get("ConsumedCapacity", {}).get("CapacityUnits"),
            session_id,
            transaction_id,
        )
        return retorno
    
    def delete(
        self,
        user_name,
        profile_name,
        session_id="",
        transaction_id=""
    ):
        retorno = self._tabela.delete_item(
            Key={"userName": str(user_name), "profileName": str(profile_name)},
            ReturnConsumedCapacity="TOTAL",
        )
        logging.info(
            "Tabela %s, capacityUnits %s, session_id %s, transaction_id %s",
            retorno.get("ConsumedCapacity", {}).get("TableName"),
            retorno.get("ConsumedCapacity", {}).get("CapacityUnits"),
            session_id,
            transaction_id,
        )
        return retorno