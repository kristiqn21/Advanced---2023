lines = ['Readme', 'This is my first example']

with open('readme.txt', 'w') as file:
    for line in lines:
        file.write(line)
        file.write('\n')
