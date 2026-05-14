# Owner: Maitreya Sapariya
# Project: Crest Training

from pydantic import BaseModel


class EvaluationModel(BaseModel):
    authenticity: int
    accuracy: int
    tone: int
    helpfulness: int
    conversion_handling: int