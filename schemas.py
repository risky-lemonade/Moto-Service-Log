from datetime import datetime
from typing import Optional
from pydantic import BaseModel

class UserCreate(BaseModel):
    username: str
    full_name: str
    password: str

class UserOut(BaseModel):
    id: int
    username: str
    full_name: str

    class Config:
        from_attributes = True

class Token(BaseModel):
    access_token: str
    token_type: str

class VehicleCreate(BaseModel):
    name: str

class VehicleOut(BaseModel):
    id: int
    name: str
    owner_id: int

    class Config:
        from_attributes = True

class ServiceLogCreate(BaseModel):
    name: str
    description: str
    cost: float

class VehicleBasic(BaseModel):
    id: int
    name: str

    class Config:
        from_attributes = True

class ServiceLogOut(BaseModel):
    id: int
    name: str
    description: str
    cost: float
    date: datetime
    vehicle_id: int
    vehicle: VehicleBasic

    class Config:
        from_attributes = True