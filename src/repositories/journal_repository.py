"""
Placeholder
"""
import firebase_admin
from firebase_admin import credentials, db
import os
from dotenv import load_dotenv
from datetime import date

load_dotenv()
cred = credentials.Certificate("../firebase-admin.json")
firebase_admin.initialize_app(cred, {"databaseURL": os.getenv("DB_URL")})

ref = db.reference("/")


def create_journal_entry(journal_entry: str, username) -> None:
    """

    :param username:
    :param journal_entry:
    :return:
    """
    data = {
        str(date.today()): journal_entry
    }
    if db.reference("/journal").get(username) is not None:
        db.reference("/journal").child(username).update(data)
    db.reference("/journal").child(username).set(data)
