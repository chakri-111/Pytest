import pytest
@pytest.fixture()  #for manually using fixture in required tests
def setup_closure():
    print("open browser")
    print("open url")
    yield
    print("logout account")
    print("close browser")


# we write fixture in conftest file and use it in the files where ever we require we don't need to write in all files/ scripts