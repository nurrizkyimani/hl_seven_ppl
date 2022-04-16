from firebase_admin import credentials
import firebase_admin
from fastapi import FastAPI
from pydantic import BaseModel
from firebase_admin import firestore


class Patient(BaseModel):
    name: str
    navigator: str
    active: bool = False
    last_contact: int
    description: str = None
    app_list : List[str] = []


class Appointment(BaseModel):
    status: str
    priority: int
    description: str
    start: str
    end: str


app = FastAPI()

# firebase credential
cred = credentials.Certificate("scalable-ppl-hlseven-firebase.json")
firebase_admin.initialize_app(cred)
db = firestore.client()


@app.get("/")
async def root():
    return {"message": "Hello fdfd "}


# GET patient
@app.get("/patient")
async def patients():
    result = db.collection(u"patients").get()
    pat_l = []
    for doc in result:
        pat_l.append({"id": doc.id, **doc.to_dict()})
    return {
        "status": 201,
        "message": pat_l}


# POST PATIENT JSON
@app.post("/patient/new")
async def patients(patient: Patient):
    res = db.collection("patients").add(patient.dict())
    x = res

    return {
        "status": 201,
        "time": x,
        "message": "done"}


# POST appointmetns
@app.post("/appointment/new")
async def appointments(appointment: Appointment):
    res = db.collection("appointments").add(appointment.dict())

    return {
        "status": 201,
        "message": "done"}


# GET appointmetns
@app.get("/appointment")
async def appointments():
    apps = db.collection("appointments").get()
    app_list = []
    for app in apps:
        app_list.append({"id": app.id, **app.to_dict()})

    return {
        "status": 201,
        "message": app_list
    }
