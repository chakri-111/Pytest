def test_assert_greater():
    a=20
    b=15
    assert a >b,"this message under quotes does not print as it is passed" # it does not print anything as it is passes


def test_assert_equal():
    a=10
    b=20
    assert a.__eq__(b) ,("a is less than b. So fail.")

def test_three():
    a=set("101")
    b=set("102")
    assert a==b,"a is not equals to b"  # it prints only failed method's comment and ignores the passed method's comment

