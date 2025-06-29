import pytest

@pytest.mark.smoke
def test_first_mark():
    print("smoke test")

@pytest.mark.skip
def test_second_mark():
    print("regression1")

@pytest.mark.regression
def test_third_mark():
    print("regression2")


# pytest -rA -m smoke           to run markers having smoke only
# pytest -rA -m, regression     to run markers having regression only
# pytest -rA -m "smoke or regression"     to run either some or regression
# skip is a predefined function which is used for skipping a function/ functions