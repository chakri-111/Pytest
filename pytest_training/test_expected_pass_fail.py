import pytest

@pytest.mark.xfail
def test_fail_case():
    a=10
    b=2
    assert a==b

@pytest.mark.xfail
def test_pass_case():
    a=10
    b=10
    assert a==b

@pytest.mark.xfail
@pytest.mark.smoke
def test_multiple_markers():
    a=10
    b=20
    assert a==b

# we can use multiple markers also for same function
# same markers for both expected pass and fail