"""
Placeholder
"""
from ..repositories import journal_repository


def create_journal_entry(journal_entry: str, username) -> None:
    """

    :param username
    :param journal_entry:
    :return:
    """
    journal_repository.create_journal_entry(journal_entry=journal_entry, username=username)
