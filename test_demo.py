import pytest

@pytest.fixture()
def before_after():
    print('\nBefore test')
    yield None
    print('\nAfter test')

def test_demo1(before_after):
    assert 1==2

def test_demo2():
    assert 2==2
