import pytest


@pytest.fixture()  # for set up and closure of every test case
def setup_and_teardown():
    print("open browser")
    print("open url")
    yield  # to separate setup and closure
    print("logout")
    print("close browser")

def test_login_correct(setup_and_teardown):
    print("provide valid credentials")

def test_login_incorrect(setup_and_teardown):
    print("provide invalid credentials")

# the code before yield will perform before every def and  code after yield will perform after every def
# yield is to separate fixture like  setup ( runs before test cases) and closure (runs after test cases)  for every test case
# fixture to make setup and closure