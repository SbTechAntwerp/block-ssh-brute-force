#!/usr/bin/python3
import re
#read the log file
with open('./sshdlog') as sshdlog:
    readsshdlog = sshdlog.read()
    splitsshdlog = readsshdlog.splitlines()
#test the splitted lines 
# print(splitsshdlog[0])
def remove_unnecessary_lines(array):
    array_with_invalidUser = []
    for line in array:
        if "Invalid user" in line:
            array_with_invalidUser.append(line)
    return(array_with_invalidUser)

def filter_ips_by_session_id(array):
    array_of_ips = []
    current_session_id = ''
    for line in array:
        session = re.findall(r'\[\d+\]', line)[0]
        ip= 
