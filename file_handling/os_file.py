import os

# print(os.getcwd()) -> gets current directory
# print(os.mkdir('C:/Users/kris/PycharmProjects/pythonProject/Advanced/Workshop')) --> creates new directory
# os.remove('kris.txt') --> removes files

try:
    os.remove('kris.txt')
    print('File successfully removed!')

except FileNotFoundError:
    print('File cannot be found!')

