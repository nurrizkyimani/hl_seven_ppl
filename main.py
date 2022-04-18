
from fastapi import FastAPI
from model import Appointment, Patient
from view import get_all_appointments, get_all_patients, post_appointment, post_patient, update_patient_list

app = FastAPI()


# HOME
@app.get("/")
async def root():
    return {"message": "Hello fdfd "}

# GET ALL PATIENTS


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
@app.post("/appointment/new")
async def appointments(appointment: Appointment):

    # create appointment with id and know the start and the end
    app_res = post_appointment(appointment)

    # update patient list after posting the appointment to the firebase
    res_d = update_patient_list(app_res["id"], appointment.patient_id)

    return {"id": app_res["id"], **appointment.dict()}

# GET appointmetns


@app.get("/appointment")
async def appointments():
    app_list = get_all_appointments()

    return {
        "status": 201,
        "message": app_list
    }
