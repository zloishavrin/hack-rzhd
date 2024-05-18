from pydantic import BaseModel
from typing import List

class StringsModel(BaseModel):
    strings: List[str]
