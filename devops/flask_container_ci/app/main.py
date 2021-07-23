import json
from dataclasses import dataclass, asdict
from typing import TypedDict

from flask import Flask
from flask import make_response
from werkzeug.exceptions import NotFound


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


app = Flask(__name__)

with open("./users.json", "r") as f:
    users = json.load(f)


@app.get("/")
def index():
    return pretty_json(
        {
            "resources_uris": {
                "users": "/users",
                "user": "/users/<username>",
            },
            "current_uri": "/",
        }
    )


@app.get("/users")
def all_users():
    return pretty_json(users)


@app.get("/users/<username>")
def user_data(username):
    if username not in users:
        raise NotFound

    return asdict(UserOutputDto.from_dict(users[username]))


@app.get("/users/<username>/something")
def user_something(username):
    raise NotImplementedError()


@app.get("/health")
def health():
    return {"status": "ok"}


def pretty_json(arg):
    response = make_response(json.dumps(arg, sort_keys=True, indent=4))
    response.headers["Content-type"] = "application/json"
    return response


if __name__ == "__main__":
    app.run(port=5000)
