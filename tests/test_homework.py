import json

import pytest


# TODO №1
@pytest.mark.parametrize("auth_data", ["User", "Admin", "Guest"], indirect=True)
def test_auth_data(auth_data):
    if auth_data["role"] in ["User", "Admin"]:
        assert auth_data["token"] is not None
    else:
        assert auth_data["token"] is None


# TODO №2
def test_each_file(data_file):
    text = data_file.read_text(encoding="utf-8").strip()

    assert text != ""

    if data_file.suffix == ".json":
        json.loads(text)


# TODO №3

@pytest.mark.parametrize(
    "name",
    [
        pytest.param("Иван", id="name=Иван"),
        pytest.param("Ольга", id="name=Ольга"),
    ],
)
@pytest.mark.parametrize(
    "surname",
    [
        pytest.param("Иванов", id="surname=Иванов"),
        pytest.param("Петрова", id="surname=Петрова"),
    ],
)
@pytest.mark.parametrize(
    "age",
    [
        pytest.param(27, id="age=27"),
        pytest.param(18, id="age=18"),
        pytest.param(35, id="age=35"),
    ],
)
def test_registration_form(name, surname, age):
    assert isinstance(name, str)
    assert len(name) > 0

    assert isinstance(surname, str)
    assert len(surname) > 0

    assert age >= 18
