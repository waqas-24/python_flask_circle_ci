from hello_world import first_function


def test_first_function()->None:
    check_hello="Hello"
    assert check_hello == first_function()
