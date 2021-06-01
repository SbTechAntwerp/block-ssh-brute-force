#!/usr/bin/python3

from os import linesep


with open('./sshdlog') as sshdlog:
    if "dis" in sshdlog:
        print(sshdlog + "disconnected")
    else: 
        print(sshdlog + "not disconnected")

'''
        for line in sshdlog:
            if line == '*dis*':
                print(line + "disconnected")
            
            else:
                print(line + "not disconnected")
                '''