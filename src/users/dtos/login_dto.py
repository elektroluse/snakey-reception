from dataclasses import dataclass

@dataclass
class LoginServiceResponse:
    user : {}
    refresh : str
    access_token : str
    errors : str