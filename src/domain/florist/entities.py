from pydantic import BaseModel


class Florist(BaseModel):
    florist_id: str
    title: str
    genres: str
    link: str
