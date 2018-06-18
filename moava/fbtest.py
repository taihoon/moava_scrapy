import json
import pyrebase
from configs import firebase

FIREBASE_CONFIG = firebase.CONFIG
firebase = pyrebase.initialize_app(FIREBASE_CONFIG)

db = firebase.database()
v = db.child("videos").child("todayhumor14454378GZjt_sA2eso").shallow().get()

if v.val() is None:
    print("new", v.val())
else:
    print("skip", v.val())




# db.child("videos").remove()
