from sqlalchemy.orm import declarative_base, relationship
from sqlalchemy import Column, Integer, String, Float, Boolean, ForeignKey, DateTime, func

Base = declarative_base()

class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True)
    username = Column(String, unique=True)
    full_name = Column(String)
    hashed_password = Column(String)

class Vehicle(Base):
    __tablename__ = "vehicles"
    id = Column(Integer, primary_key=True)
    name = Column(String)
    owner_id = Column(Integer, ForeignKey("users.id", ondelete="CASCADE"), nullable=False)
    service_logs = relationship("ServiceLog", back_populates="vehicle")

class ServiceLog(Base):
    __tablename__ = "service_logs"
    id = Column(Integer, primary_key=True)
    name = Column(String)
    description = Column(String)
    cost = Column(Float)
    date = Column(DateTime(timezone=True), server_default=func.now())
    vehicle_id = Column(Integer, ForeignKey("vehicles.id", ondelete="CASCADE"), nullable=False)
    vehicle = relationship("Vehicle", back_populates="service_logs")