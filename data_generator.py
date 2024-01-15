import random
import string
import datetime


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
    pass


def generate_appointment_data():
    pass