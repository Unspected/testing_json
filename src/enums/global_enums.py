from enum import Enum


class GlobalErrorMessages(Enum):
    WRONG_STATUS_CODE = "Receive status code is not equal to expected"
    WRONG_ELEMENTS_COUNT = "Number of items not equal to expected"
