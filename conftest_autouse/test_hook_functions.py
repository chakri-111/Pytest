import pytest


def setup_function(function):
    print("setup_function")

def teardown_function(function): # setup and teardown is keywords. instead of function we can use module eg : teardown_module(module)
    print("closure")

def test_one():
    print("one")

def test_two():
    print("two")

def test_three():
    print("three")