import random
import string
import datetime
import json


def generate_custom_id(prefix):
    timestamp = datetime.datetime.now().strftime("%Y%m%d-%H%M%S")
    random_chars = ''.join(random.choices(string.digits, k=8))
    return f"{prefix}-{random_chars}-{timestamp}"


def name_generator():
    return [{
        "use" : "official",
        "family" : "Smith",
        "given" : ["Eve", "Annabella"]
    }]


def address_generator():
    return [{
        "use" : "home",
        "line" : ["2222 Home Street"],
        "postalCode" : "WA316324"
    }]


def generate_patient_data():
    patient_json = {
        "resourceType": "Patient",
        "id": generate_custom_id("Patient"),
        "name": name_generator(),
        "gender": "female",
        "birthDate": "1973-05-31",
        "address": address_generator()
    }
    return patient_json


def generate_practitioner_data():
    practitioner_json = {
        "resourceType": "Practitioner",
        "id": generate_custom_id("Practitioner"),
        "address": address_generator(),
        "qualification": [{
            "code": {
                "coding": [{
                    "system": "http://terminology.hl7.org/CodeSystem/v2-0360/2.7",
                    "code": "DM",
                    "display": "Doctor of Medicine"
                }],
                "text": "Doctor of Medicine"
            },
            "issuer": {
                "display": "Example University"
            }
        }]
    }
    return practitioner_json


def generate_appointment_data():
    appointment_json = {
      "resourceType": "Appointment",
      "id": generate_custom_id("Appointment"),
      "status": "booked",
      "class": "ambulatory",
      "description": "Discussion on the results of your recent MRI",
      "start": "2013-12-10 09:00:00",
      "end": "2013-12-10 11:00:00",
      "created": "2013-10-10"
    }
    return appointment_json


def generate_data(resource_type, data_count):
    output_data = None
    if resource_type == 'Patient':
        generator_function = generate_patient_data
    elif resource_type == 'Practitioner':
        generator_function = generate_practitioner_data
    elif resource_type == 'Appointment':
        generator_function = generate_appointment_data

    generated_data = generator_function()
    if output_data:
        with open("output.txt", 'w') as file:
            json.dump(generated_data, file, indent=2)