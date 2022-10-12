POST_SCHEMA = {
    "type": "array",
    "properties": {
        "country_id": {"type": "string"},
        "probability": {"type": "integer"},
    },
    "required": ["country_id"]
}

POST_SCHEMA_OBJECT = {
    "type": "object",
    "properties": {
        "country": {"properties": {
            "country_id": {"type": "string"},
            "probability": {"type": "integer"},
        }},
        "name": {"type": "string"},
    },
    "required": []
}
