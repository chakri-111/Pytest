import pytest


@pytest.mark.smoke
def test_smoke1():
    print("this is smoke 1")

@pytest.mark.regression
def test_regression1():
    print("this is regression1")

@pytest.mark.regression
def test_regression2():
    print("this is 2nd regression test case")

@pytest.mark.regression
def test_regression3():
    print("this is 3rd regression test case")


# grouping tests means assigning the same marker to multiple tests.
# when we run particular marker then all the tests having that marker will run.