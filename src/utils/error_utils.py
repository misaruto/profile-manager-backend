DEFAULT_ERRORS = {
  1: "Profile not found",
  2: "Profile already exists",
  3: "Profile default can't be deleted",
}


class ApiError(Exception):
  @staticmethod
  def get_error_json(code,*args):
    return{
      "errorCode":code,
      "errorMessage":DEFAULT_ERRORS[code].format(*args)
    }
  def __init__(self, code=0, *args) -> None:
    self.message = self.get_error_json(code,*args)
    super().__init__(self.message)