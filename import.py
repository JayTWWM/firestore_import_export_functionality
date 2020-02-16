import firebase_admin as fb
from firebase_admin import firestore
import json

cred = fb.credentials.Certificate('xxxxxx-xxxxxxxxx-xxxxxx-firebase-adminsdk-xxxxx-xxxxxxxxxx.json')
default_app = fb.initialize_app(cred)
db = firestore.client()

df_file = open("./firestore.json")
df = df_file.read() 
dict = json.loads(df)

# add your collections manually
my_doc_ref = db.collection('my_collection').document('my_document')
my_doc_ref.set(dict)