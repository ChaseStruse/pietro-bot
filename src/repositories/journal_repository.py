"""
Placeholder
"""
import firebase_admin
from firebase_admin import credentials, db
import os
from dotenv import load_dotenv

load_dotenv()
cred = credentials.Certificate("../firebase-admin.json")
firebase_admin.initialize_app(cred, {"databaseURL": os.getenv("DB_URL")})

ref = db.reference("/")


def create_journal_entry(journal_entry: str) -> None:
    """

    :param journal_entry:
    :return:
    """
    db.reference("/journal").push().set(journal_entry)
