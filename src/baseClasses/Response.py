from src.enums.global_enums import GlobalErrorMessages


class Response:

    def __init__(self, response):
        self.response = response
        self.response_json = response.json().get("data")
        self.response_status = response.status_code

    # method for validation
    def validate(self, schema):
        if isinstance(self.response_json, list):
            for item in self.response_json:
                schema.parse_obj(item)
        else:
            schema.parse_obj(self.response_json)

    # check current status from server
    def assert_status(self, status_code):
        if isinstance(status_code, list):
            assert self.response_status in status_code, self
        else:
            assert self.response_status == status_code, self

    def __str__(self):
        return \
            f"Status code {self.response_status}" \
            f"\nRequested url {self.response.url}" \
            f"\nResponse body {self.response_json}"