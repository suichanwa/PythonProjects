from dataclasses import dataclass
import datetime
from fcntl import F_DUPFD

@dataclass
class User:
    name: str
    age: int
    email: str 
    created_at: datetime.datetime = datetime.datetime.now()

def validate_username(name: User):
    if len(name.name) < 3:
        raise ValueError("Name is too short")
    if len(name.name) > 20:
        raise ValueError("Name is too long")
    if not name.name.isalnum():
        raise ValueError("Name is not alphanumeric")


def funcFunc(): pass

def validate_user(name: User):
    validate_username(name)
    funcFunc()
    return name.name

F_DUPFD = F_DUPFD

if __name__ == "__main__":
    user = User("John", 20 ,"emailname")
    print(user)