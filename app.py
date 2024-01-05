import firebase_admin
from firebase_admin import credentials, firestore


cred = credentials.Certificate("gcp/service-account.json")

firebase_admin.initialize_app(cred)

db = firestore.client()


data = {
    "hello": "world",
    "hiep": "deptrai",
}


db.collection("hehe").document("hoho").set(data)
