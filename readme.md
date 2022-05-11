# HL7 Implementation 


## Description
This is the implementation of **Application of HL7 FHIR in a Microservice
Architecture for Patient Navigation on Registration and Appointments** . Here we are using MVC model as the implementation of the patient and appointment program. Using MVC has become similr with the structure that given within the paper. 

## Model 
The model divided into Patient and Appointment Model
Patient Model
``` 
class Patient(BaseModel):
    name: str
    navigator: str
    active: bool = False
    last_contact: Optional[str] = None
    description: str = None
    app_list: List[str] = []
```

Appointment Model 
``` 
class Appointment(BaseModel):
    patient_id: str
    status: str
    priority: int
    description: str
    start: str
    end: str
```
The model then use in the `view.py`  which include function that use for database operation. The function include:

`get_all_patients()` : get all patient list 
`post_patient(patient: Patient)` : create new patient data
`post_appointment(appointment: Appointment)` : create new appointment data 
`update_patient_list(res_id, patient_id)` : add appointment id to the patient docs
`get_all_appointments()` : get all appointment 


## Endpoint

here the endpoint is included as `view.py`



### Get all patients list
* Endpoint: `/patient`
* HTTP Method: `GET`
* Request Body: NONE

* Response Body:
```json
 {
    "status": 201,
    "message": [
        {
            "id": "1UHLtW8P9bytVN8aFLQj",
            "navigator": "tdg",
            "name": "ddd",
            "last_contact": "2021-12-06T15:00:10.079060+00:00",
            "app_list": [
                "ffbODMB35n36hdIMBj1k",
                "P50olSLqf1IcBLCtU77N",
                "Huz6wJ7QfsYFvlR1Nnvl",
                "pMUgmEZAO32RfPi2IUJm",
                "vSVwdrmXUN7mNd4AklJs"
            ],
            "description": "sick huge",
            "active": false
        },
        {
            "id": "i9DjqgurVhHZMdVyihnI",
            "active": false,
            "last_contact": "2021-12-06T15:00:10.079060+00:00",
            "description": "sick dam",
            "navigator": "dsk",
            "name": "ari",
            "app_list": []
        }
    ]
}

  ```


### Get all appointments
* Endpoint: `/appointment`
* HTTP Method: `GET`
* Request Body: NONE

* Response Body:
```json 

{
    "status": 201,
    "message": [
        {
            "id": "CK1Mjy2XuzbiEwfkYTET",
            "start": "2022-01-01T02:36:55+0000",
            "priority": 1,
            "patient_id": "1UHLtW8P9bytVN8aFLQj",
            "status": "1",
            "end": "2022-02-01T02:36:55+0000",
            "description": " sick head"
        },
    ]
}

```

### post new appointment 
* Endpoint: `/appointment/new`
* HTTP Method: `POST`
* Request Body:
```json

{
    "patient_id" : "1UHLtW8P9bytVN8aFLQj",
    "description": " sick head",
    "status": 1,
    "priority": 1,
    "start": "2022-01-01T02:36:55+0000",
    "end": "2022-02-01T02:36:55+0000"
}

  ```

* Response Body:
```json

{
    "id": "vSVwdrmXUN7mNd4AklJs",
    "patient_id": "1UHLtW8P9bytVN8aFLQj",
    "status": "1",
    "priority": 1,
    "description": " sick head",
    "start": "2022-01-01T02:36:55+0000",
    "end": "2022-02-01T02:36:55+0000"
}
   
```


### post new patient 
* Endpoint: `/patient/new`
* HTTP Method: `POST`
* Request Body:
```json

{
   "description": "sick huge",
    "name": "ddd",  
    "active": false,
    "navigator": "tdg"
}

  ```

* Response Body:
```json

{
    "status": 201,
    "message": {
        "id": "1UHLtW8P9bytVN8aFLQj",
        "name": "ddd",
        "navigator": "tdg",
        "active": false,
        "last_contact": null,
        "description": "sick huge",
        "app_list": []
    }
}
   
```

## Stack 
Firebase
FastApi
Pydantic

## How to run the program
1. run `pip install requirements.txt`
2. run `uvicorn main:app --reload`


## Resource 
https://drive.google.com/file/u/1/d/1dcIfK5phE0-bTDb7E9XNYbxzcjq1JmQi/view?usp=sharing
