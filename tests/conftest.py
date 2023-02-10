import pytest

@pytest.fixture(autouse=True)
def clean_data_before_write():
    with open('tests/test_for_append_data.txt', 'w'):
        pass #витираємо із файла

@pytest.fixture(autouse=True)
def clean_data_in_copiedtxt_write():
    with open('tests/info_file_copied.txt', 'w'):
        pass #витираємо із файла