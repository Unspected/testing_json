from configuration import SERVICE_URL
from src.baseClasses.Response import Response
from src.schemas.users import User

import requests


def test_gettings_users():
    response = requests.get(SERVICE_URL)
    test_object = Response(response)
    test_object.assert_status(200)
    test_object.validate(User)



