import enum


class UserRole(str, enum.Enum):
    STUDENT = "student"
    ADMIN = "admin"
