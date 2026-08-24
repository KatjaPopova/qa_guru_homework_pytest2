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
NAMES = ["Иван", "Ольга"]
SURNAMES = ["Иванов", "Петрова"]
AGES = [17, 18, 35]


def id_name(name: str) -> str:
    return f"name={name}"


def id_surname(surname: str) -> str:
    return f"surname={surname}"


def id_age(age: int) -> str:
    return f"age={age}"


@pytest.mark.parametrize("name", NAMES, ids=id_name)
@pytest.mark.parametrize("surname", SURNAMES, ids=id_surname)
@pytest.mark.parametrize("age", AGES, ids=id_age)
def test_registration_form(name, surname, age):
    assert isinstance(name, str)
    assert len(name) > 0

    assert isinstance(surname, str)
    assert len(surname) > 0

    assert age >= 18
