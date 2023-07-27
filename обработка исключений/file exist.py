import os
try:
    os.mkdir('new_folder')
except FileExistsError:
    print('данная папка уже существует')