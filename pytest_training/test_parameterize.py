import pytest

@pytest.mark.parametrize("user,password",[("chakri","rallapalli"),("rallpalli","laxamna"),("rallapalli","chakri")])

def test_parameters(user,password):
    print(user+"-"+password)
