import datetime
from email import message
from typing import List, Optional
from firebase_admin import credentials
import firebase_admin
from fastapi import FastAPI
from pydantic import BaseModel
from firebase_admin import firestore


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


app = FastAPI()

# firebase credential
cred = credentials.Certificate("scalable-ppl-hlseven-firebase.json")
firebase_admin.initialize_app(cred)
db = firestore.client()


@app.get("/")
async def root():
    return {"message": "Hello fdfd "}


# get all patients from firebase view;
def get_all_patients():
    result = db.collection(u"patients").get()
    pat_l = []
    for doc in result:
        pat_l.append({"id": doc.id, **doc.to_dict()})
    return pat_l

# post patient data to firebase based on Patient Model

# WORKING


def post_patient(patient: Patient):
    doc_ref = db.collection(u"patients").document()

    dt = datetime.datetime(2021, 12, 6, 15, 00, 10, 79060)
    doc_ref.set({
        u"name": patient.name,
        u"navigator": patient.navigator,
        u"active": patient.active,
        u"last_contact": dt,
        u"description": patient.description,
        u"app_list": []
    })
    return {"id": doc_ref.id, **patient.dict()}

# GET patient


@app.get("/patient")
async def patients():
    res = get_all_patients()
    return {
        "status": 201,
        "message": res}


# POST PATIENT JSON
@app.post("/patient/new")
async def patients(patient: Patient):

    # call post_patient function and return the result
    res = post_patient(patient)

    # return the res from post patient
    return {
        "status": 201,
        "message": res
    }


# POST function for appointment from the Appointment Model
def post_appointment(appointment: Appointment):
    doc_ref = db.collection(u"appointments").document()
    doc_ref.set({
        u"patient_id": appointment.patient_id,
        u"status": appointment.status,
        u"priority": appointment.priority,
        u"description": appointment.description,
        u"start": appointment.start,
        u"end": appointment.end
    })
    return {"id": doc_ref.id, **appointment.dict()}


# POST appointmetn
@app.post("/appointment/new")
async def appointments(appointment: Appointment):

    # create appointment with id and know the start and the end
    res = post_appointment(appointment)

    print(res.id)

    # set the patient list in the patient document with the id of the appointment
    # doc_ref = db.collection(u"patients").document(res.id)
    # doc_ref.update({u'app_list': firestore.ArrayUnion([res["id"]])})

    print(res)

    return {
        "status": 201,
        "message": "done"}


# create fucntion for get all appointments from firebase
def get_all_appointments():
    result = db.collection(u"appointments").get()
    app_l = []
    for doc in result:
        app_l.append({"id": doc.id, **doc.to_dict()})
    return app_l

# GET appointmetns


@app.get("/appointment")
async def appointments():
    app_list = get_all_appointments()

    return {
        "status": 201,
        "message": app_list
    }
