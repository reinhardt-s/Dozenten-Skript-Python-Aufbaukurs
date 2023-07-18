from datetime import datetime
from typing import Any, Dict, List
from pydantic import BaseModel


class Parameters(BaseModel):
    name: str
    unit: str
    data: List[float]


class Properties(BaseModel):
    parameters: Dict[str, Parameters]
    station: str


class Geometry(BaseModel):
    type: str
    coordinates: List[float]


class Feature(BaseModel):
    type: str
    geometry: Geometry
    properties: Properties


class WeatherData(BaseModel):
    media_type: str
    type: str
    version: str
    timestamps: List[datetime]
    features: List[Feature]

    def __str__(self) -> str:
        return f"{self.media_type} {self.type} {self.version} {self.timestamps} {self.features}"

    @classmethod
    def from_json(cls, json: Dict[str, Any]) -> 'WeatherData':
        return cls(
            media_type=json['media_type'],
            type=json['type'],
            version=json['version'],
            timestamps=[datetime.fromisoformat(ts) for ts in json['timestamps']],
            features=[Feature(**feature) for feature in json['features']]
        )
