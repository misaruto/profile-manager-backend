from typing import Any
from pydantic import BaseModel
from src.interfaces.response_inteface import ResponseModelAbstract

class ResponseSuccessModel(BaseModel,ResponseModelAbstract):
    ok: bool = True
    status: int
    message: str
    resource: str
    data: Any = None

    def set_response(self, response):
        self.data = response



class ResponseErrorModel(BaseModel,ResponseModelAbstract):
    ok: bool = False
    status: int
    resource: str
    message: str
    transactionId: str
    errors: Any = None

    def set_response(self, response):
        self.errors = response
