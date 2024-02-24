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


def create_journal_entry(journal_entry: str, journal_date: str, username: str) -> None:
    """
    Attempts to get user's journal entry, if none, creates new entry, else updates existing entry
    :param username: string, user's discord username
    :param journal_entry: string, user's journal entry
    :param journal_date: string, journal entry date
    :return: None
    """
    journal_entry_from_user_entered_date, identifier = db.reference(f"/journal/{username}").get(journal_date)

    if journal_entry_from_user_entered_date.get(journal_date) is not None:
        db.reference(f"/journal/{username}").child(journal_date).set(journal_entry)
    else:
        db.reference(f"/journal").child(username).update({journal_date: journal_entry})


def read_journal_entry(journal_date: str, username: str) -> str:
    """
    Attempts to get user's existing journal entry, if entry exists returns entry, else returns default statement
    :param journal_date: string, journal entry date
    :param username: string, user's discord username
    :return: String
    """
    journal_entry, identifier = db.reference(f"/journal/{username}").get(journal_date)

    if journal_entry.get(journal_date) is not None:
        return journal_entry[journal_date]
    else:
        return "No journal found for given date"


def update_journal_entry(journal_date: str, updated_journal_entry: str, username: str) -> str:
    """
    Attempts to get user's journal entry, if exists updates entry to new entry, else returns default statement
    :param journal_date: string, journal entry date
    :param username: string, user's discord username
    :param updated_journal_entry: string, new journal entry
    :return: String
    """

    journal_entry, identifier = db.reference(f"/journal/{username}").get(journal_date)

    if journal_entry.get(journal_date) is not None:
        db.reference(f"/journal/{username}").child(journal_date).set(updated_journal_entry)
        return "Journal has been updated"
    else:
        return "No data found for that date, please try again"


def delete_journal_entry(journal_date: str, username: str) -> str:
    """
    Attempts to get user's existing journal entry, if entry exists deletes entry, else returns default statement
    :param journal_date: string, journal entry date
    :param username: string, user's discord username
    :return: String
    """
    journal_entry_todays_date, identifier = db.reference(f"/journal/{username}").get(journal_date)

    if journal_entry_todays_date.get(journal_date) is not None:
        db.reference(f"/journal/{username}").child(journal_date).delete()
        return "Journal has been deleted"
    else:
        return "No data found for that date, please try again"
