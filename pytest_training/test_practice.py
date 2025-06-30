import pytest

@pytest.mark.skip
def test_skip_marker():
    print("marker")


@pytest.mark.xfail
def test_xfail_testcase():
    assert 10>12
    print("xfail")

@pytest.mark.parametrize("username,password",[("chakri","ramana"),("ramana","rallapalli")])
def test_parameterize(username,password):
    print(username+"'"+password)

#@pytest.mark.parametrize("user,password",[("chakri","rallapalli"),("rallpalli","laxamna"),("rallapalli","chakri")])

@pytest.fixture()
def setup_teardown():
    print("open browser")
    print("open link")
    print("login")
    yield
    print("logout")
    print("quit browser")

@pytest.mark.smoke
def test_place_order(setup_teardown):
    print("placing order")

def setup_function(function):
    print("setup_function")

def teardown_function(function):
    print("tear down funtion")

def setup_module(module):
    print("moduile")
def teardown_module(module):
    print("module")