# coding=utf-8

def tail(filename):
    with open(filename, 'r') as file:
        file.seek(0, 2)
        while True:
            line = file.readline()
            if line:
                print line
tail('123.txt')