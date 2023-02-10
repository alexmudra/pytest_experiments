import pytest

@pytest.fixture()
def clean_data_before_write():
    with open('tests/test_for_append_data.txt', 'w'):
        pass #витираємо із файла