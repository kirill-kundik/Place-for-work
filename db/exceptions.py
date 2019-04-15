class DatabaseException(Exception):
    """Base class for database exceptions"""


class RecordNotFound(DatabaseException):
    """Requested record in database was not found"""
