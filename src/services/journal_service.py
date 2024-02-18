"""
Placeholder
"""
from ..repositories import journal_repository
from datetime import date


def create_journal_entry(journal_entry: str, year: int, month: int, day: int, username) -> None:
    """

    :param username
    :param journal_entry:
    :param year:
    :param month:
    :param day:
    :return:
    """
    journal_date = date(year=year, month=month, day=day)
    journal_repository.create_journal_entry(journal_entry=journal_entry, journal_date=str(journal_date),
                                            username=username)


def read_journal_entry(year: int, month: int, day: int, username) -> str:
    """

    :param year:
    :param month:
    :param day:
    :param username:
    :return:
    """
    journal_date = date(year=year, month=month, day=day)
    journal = journal_repository.read_journal_entry(journal_date=str(journal_date), username=username)
    return journal


def update_journal_entry(year: int, month: int, day: int, updated_journal_entry: str, username) -> str:
    """

    :param year:
    :param month:
    :param day:
    :param username:
    :param updated_journal_entry:
    :return:
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
