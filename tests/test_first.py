import requests
from configuration import SERVICE_URL, NEW_URL, JOKES_URL
from src.enums.global_enums import GlobalErrorMessages
from src.schemas.post import POST_SCHEMA, POST_SCHEMA_OBJECT
from src.pydantic_schemas.Post import Post
from src.baseClasses.Response import Response


def test_getting_posts():
    r = requests.get(url=NEW_URL)
    response = Response(r)
    response.assert_status(200).validate(Post)
