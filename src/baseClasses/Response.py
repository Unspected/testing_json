from jsonschema import validate
from src.enums.global_enums import GlobalErrorMessages


class Response:

    def __init__(self, response):
        self.response = response
        self.response_json = response.json()
        self.response_status = response.status_code

    # method for validation
    def validate(self, schema):
        if isinstance(self.response_json, object):
            schema.parse_obj(self.response_json)
        else:
            print(f"something wrong {type(self.response_json)}")
        return self

    # check current status from server
    def assert_status(self, status_code):
        if isinstance(status_code, list):
            assert self.response_status in status_code, GlobalErrorMessages.WRONG_STATUS_CODE.value
        else:
            assert self.response_status == status_code, GlobalErrorMessages.WRONG_STATUS_CODE.value
        return self
