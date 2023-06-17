from pydantic import BaseModel
from typing import List, Dict, Any, Optional
from datetime import datetime


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

    def __str__(self):
        return f"{self.media_type} {self.type} {self.version} {self.timestamps} {self.features}"

    @staticmethod
    def from_json(json):
        return WeatherData(media_type=json['media_type'],
                           type=json['type'],
                           version=json['version'],
                           timestamps=json['timestamps'],
                           features=json['features'])
