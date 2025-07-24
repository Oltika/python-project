import pytest


@pytest.mark.regression
def test_one_is_one(separator):
    print('Before separatpr test')
    print(separator)
    assert 1 == 1

@pytest.mark.smoke
def test_two_is_two(all_tests):
    assert 2 == 2

@pytest.mark.skip('Bug #57')
def test_with_unresolved_bug(separator):
    print('skip unresolved bug')
    print(separator)
    assert 3 == 2
