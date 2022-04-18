
from typing import List, Optional
from pydantic import BaseModel


class Patient(BaseModel):
    name: str
    navigator: str
    active: bool = False
    last_contact: Optional[str] = None
    description: str = None
    app_list: List[str] = []


class Appointment(BaseModel):
    patient_id: str
    status: str
    priority: int
    description: str
    start: str
    end: str
