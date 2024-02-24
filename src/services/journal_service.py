"""
Placeholder
"""
from ..repositories import journal_repository
from datetime import date


def create_journal_entry(journal_entry: str, year: int, month: int, day: int, username: str) -> None:
    """
    Converts user inputted date integers into a date object, calls repository layer.
    :param username: string, user's discord username
    :param journal_entry: string, user's journal entry
    :param year: integer, journal year
    :param month: integer, journal month
    :param day: integer, journal day
    :return: None
    """
    journal_date = date(year=year, month=month, day=day)
    journal_repository.create_journal_entry(journal_entry=journal_entry, journal_date=str(journal_date),
                                            username=username)


def read_journal_entry(year: int, month: int, day: int, username: str) -> str:
    """
    Converts user inputted date integers into a date object, calls repository layer and returns data from repo layer
    :param year: integer, journal year
    :param month: integer, journal month
    :param day: integer, journal day
    :param username: string, user's discord username
    :return: String
    """
    journal_date = date(year=year, month=month, day=day)
    journal = journal_repository.read_journal_entry(journal_date=str(journal_date), username=username)
    return journal


def update_journal_entry(year: int, month: int, day: int, updated_journal_entry: str, username: str) -> str:
    """
    Converts user inputted date integers into a date object, calls repository layer and returns data from repo layer
    :param year: integer, journal year
    :param month: integer, journal month
    :param day: integer, journal day
    :param username: string, user's discord username
    :param updated_journal_entry: string, new journal entry
    :return: String
    """
    journal_date = date(year=year, month=month, day=day)
    result = journal_repository.update_journal_entry(journal_date=str(journal_date),
                                                     updated_journal_entry=updated_journal_entry,
                                                     username=username)
    return result


def delete_journal_entry(year: int, month: int, day: int, username) -> str:
    """

    :param year:
    :param month:
    :param day:
    :param username:
    :return:
    """
    journal_date = date(year=year, month=month, day=day)
    result = journal_repository.delete_journal_entry(journal_date=str(journal_date), username=username)
    return result
