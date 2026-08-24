from pathlib import Path

import pytest


@pytest.fixture
def auth_data(request):
    role = request.param  # "User" / "Admin" / "Guest"

    if role == "Admin":
        return {"role": "Admin", "token": "admin-token"}
    if role == "User":
        return {"role": "User", "token": "user-token"}
    if role == "Guest":
        return {"role": "Guest", "token": None}

    raise ValueError("Unknown role")


def pytest_generate_tests(metafunc):
    if "data_file" in metafunc.fixturenames:
        test_data_dir = Path(__file__).resolve().parent.parent / "test_data"

        files = sorted(list(test_data_dir.glob("*.txt")) + list(test_data_dir.glob("*.json")))

        ids = [f.name for f in files]

        metafunc.parametrize("data_file", files, ids=ids)
