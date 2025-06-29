import pytest

# @pytest.fixture(autouse=True)  # by if we do not assign scope it considers function by default
@pytest.fixture(autouse=True, scope="function")   # we have also session, module, package and class

def setup_teardown():
    print("open browser")
    print("open url")
    yield
    print("logout")
    print("close browser")
