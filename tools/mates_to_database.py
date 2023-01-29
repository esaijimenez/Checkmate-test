import firebase_admin
from firebase_admin import credentials, db
import json

# Initialize Firebase Admin SDK with service account credentials
cred = credentials.Certificate("checkmate.json")
firebase_admin.initialize_app(cred, {
    'databaseURL': ''
})


#Grants access to the .json file then creates a channel to the mateIn1 database 
#with open('mateIn1.json', 'r') as json_file:
#    data1 = json.load(json_file)
#ref = db.reference("mateIn1")
#ref.set(data1)

#Grants access to the .json file then creates a channel to the mateIn2 database
#with open('mateIn2.json', 'r') as json_file:
#    data2 = json.load(json_file)
#ref = db.reference("mateIn2")
#ref.set(data2)

#Grants access to the .json file then creates a channel to the mateIn3 database
#with open('mateIn3.json', 'r') as json_file:
#    data3 = json.load(json_file)
#ref = db.reference("mateIn3")
#ref.set(data3)

#Grants access to the .json file then creates a channel to the mateIn4 database
#with open('mateIn4.json', 'r') as json_file:
#    data4 = json.load(json_file)
#ref = db.reference("mateIn4")
#ref.set(data4)

#Grants access to the .json file then creates a channel to the mateIn5 database
#with open('mateIn5.json', 'r') as json_file:
#    data5 = json.load(json_file)
#ref = db.reference("mateIn5")
#ref.set(data5)