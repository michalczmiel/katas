import json
from dataclasses import dataclass, asdict
from typing import TypedDict, List

from flask import Flask
from werkzeug.exceptions import NotFound


from app.settings import Config


class User(TypedDict):
    id: str
    name: str
    description: str


@dataclass
class UserOutputDto:
    name: str
    description: str

    @classmethod
    def from_dict(cls, user: User) -> "UserOutputDto":
        return cls(name=user["name"], description=user["description"])


def load_users() -> List[User]:
    with open(Config.USERS_PATH, "r") as f:
        return json.load(f)


users = load_users()

app = Flask(__name__)


@app.get("/")
def index():
    return {
        "resources_uris": {
            "users": "/users",
            "user": "/users/<username>",
        },
        "current_uri": "/",
    }


@app.get("/users")
def all_users():
    return users


@app.get("/users/<username>")
def user_data(username: str):
    if username not in users:
        raise NotFound

    return asdict(UserOutputDto.from_dict(users[username]))


@app.get("/users/<username>/something")
def user_something(username: str):
    raise NotImplementedError()


@app.get("/health")
def health():
    return {"status": "ok"}
