from os import path

print(__file__)
print(path.basename(__file__))
print(path.exists(r'/home/vova/PycharmProjects/gda/gda/files/пути.py'))
print(path.exists('/home/vova/PycharmProjects/gda/gda/files/пути123.py'))
dir_name, file_name = path.split(__file__)

full_path = path.join(dir_name, file_name)
print(full_path)
