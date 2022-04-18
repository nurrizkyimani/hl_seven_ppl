
import datetime
from firebase_admin import firestore
from model import Appointment, Patient
from firebase_admin import firestore

from email import message
from firebase_admin import credentials
import firebase_admin

# firebase credential
cred = credentials.Certificate("scalable-ppl-hlseven-firebase.json")
firebase_admin.initialize_app(cred)
db = firestore.client()

# get all patients


def get_all_patients():
    result = db.collection(u"patients").get()
    pat_l = []
    for doc in result:
        pat_l.append({"id": doc.id, **doc.to_dict()})
    return pat_l


# post patient data to firebase based on Patient Model
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

# post appointment


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


# update the patient list in patient doc with the id of the post appointment
def update_patient_list(res_id, patient_id):
    doc_ref = db.collection(u"patients").document(patient_id)
    res_d = doc_ref.update({
        u"app_list": firestore.ArrayUnion([res_id])
    })

    return res_d

# create fucntion for get all appointments from firebase


def get_all_appointments():
    result = db.collection(u"appointments").get()
    app_l = []
    for doc in result:
        app_l.append({"id": doc.id, **doc.to_dict()})
    return app_l
