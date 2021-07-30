'''
Firebase service.
:author: Mikey Lau
Website <https://mikeylau.uk>
GitHub <https://github.com/MikeyJL>
'''

import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
cred = credentials.Certificate("firebase-admin.json")
firebase_admin.initialize_app(cred)
db = firestore.client()