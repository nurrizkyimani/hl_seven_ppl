from firebase_admin import credentials
import firebase_admin
from fastapi import FastAPI
from pydantic import BaseModel
from firebase_admin import firestore


class Patient(BaseModel):
    name: str
    active: bool = False
    description: str = None


class Appointment(BaseModel):
    status: str
    priority: int
    description: str
    minutes: int


app = FastAPI()

# firebase credential
cred = credentials.Certificate("path/to/scalable-ppl-hlseven-firebase.json")
firebase_admin.initialize_app(cred)
db = firestore.client()


@app.get("/")
async def root():
    return {"message": "Hello fdfd "}


# GET HOME
@app.get("/home")
async def home():
    return {"message": "Hello home "}

# GET patient


@app.get("/patient")
async def patients():
    db.collection("patients").get()
    return {"message": "Hello patient "}

# GET patient JSON FORMAT


@app.get("/patient/json")
async def patients(patient: Patient):
    db.collection("patients").get()
    return {"patient": patient.dict()}


# POST PATIENT NEW
@app.post("/patient/new")
async def patients():
    return {"message": "Hello patients "}

# POST PATIENT JSON


@app.post("/patient/json")
async def patients(patient: Patient):
    db.collection("patients").add(patient.dict())
    return {"message": "Hello patients "}


# GET appointmetns
@app.post("/appointment")
async def appointments():

    return {"message": "Hello appointment"}


# GET appointmetns
@app.get("/appointment/json")
async def appointments(appointment: Appointment):
    db.collection("appointments").add(appointment.dict())
    return {"message": "Hello appointment"}
