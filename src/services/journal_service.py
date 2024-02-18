"""
Placeholder
"""
from ..repositories import journal_repository


def create_journal_entry(journal_entry: str) -> None:
    """

    :param journal_entry:
    :return:
    """
    journal_repository.create_journal_entry(journal_entry=journal_entry)
