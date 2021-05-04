import PyTest
##I've installed PyTest to VSCode
def func(num):
    return num * 2

def test_answer():
    assert func(5) == 10

test_answer()