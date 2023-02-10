#https://www.youtube.com/watch?v=MIHXRF6YMN4&t=614s
from my_funcs.file_worker import read_form_file

def test_read_fom_file():
    expect_res = ['one\n', 'twoo\n', 'three\n', 'four\n', 'fife']
    assert  expect_res == read_form_file('tests/info_file_copied.txt')

def test_read_fom_file_2():
    expect_res = ['one\n', 'twoo\n', 'three\n', 'four\n', 'fife']
    assert  expect_res == read_form_file('tests/info_file_copied.txt')

def test_read_fom_file_append_data():
    with open('tests/test_for_append_data.txt', 'w'):
        pass #витремо наді в файлі. Цей код можна перенести в якості фікстури
    test_data = ['one\n', 'twoo\n', 'three\n', 'four\n', 'fife'] #підготуємо тестові дані
    with open('tests/test_for_append_data.txt', 'a') as f_ob:
        f_ob.writelines(test_data)
    assert  test_data == read_form_file('tests/test_for_append_data.txt')