class DatabaseException(Exception):
    """Base class for database exceptions"""


class RecordNotFound(DatabaseException):
    """Requested record in database was not found"""


class DuplicateRecordException(DatabaseException):
    """Duplicate pkey while inserting data"""


class UserDoesNotExistsException(DatabaseException):
    """User does not exists in the database"""
