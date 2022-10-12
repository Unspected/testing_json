from pydantic import BaseModel, Field


# model data from array
class CountryModel(BaseModel):
    country_id: str
    probability: int = Field(le=1)


# base model for object and contains array with another model
class Post(BaseModel):
    country: list[CountryModel]
    name: str
