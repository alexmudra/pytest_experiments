def read_form_file(filepath):
    with open(filepath , "r") as file_ob:
        return file_ob.readlines()

# print(read_form_file("info_file.txt")) #['one\n', 'twoo\n', 'three\n', 'four\n', 'fife']
