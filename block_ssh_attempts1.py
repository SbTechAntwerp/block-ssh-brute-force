'''
read file 
make list from file

find line with invalid user

filter Invalid user,group session, copy ip address to list, 
if ip adrees sx3 in list then call pwblock ip

for loop sesion id to current session id then send ip adrees to ip address array
if session id same as current then continue else newsession to current session id and add ip to array
'''
#!/usr/bin/python3
import re
import fwblock
#read the log file
with open('./sshdlog') as sshdlog:
    readsshdlog = sshdlog.read()
    splitsshdlog = readsshdlog.splitlines()
#test the splitted lines 
# print(splitsshdlog[0])
def remove_unnecessary_lines(array):
    '''
    Returns only the lines from an invalid user.
    '''
    array_with_invalidUser = []
    for line in array:
        if "Invalid user" in line:
            array_with_invalidUser.append(line)
    return(array_with_invalidUser)

def filter_ips_by_session_id(array):
    '''
    Return IP address once per session ID.
    '''
    array_of_ips = []
    current_session_id = ''
    for line in array:
        #this regex is searching for the ip and retund the first one of this line 
        ip= re.findall(r"\b\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}\b", line)[0]
        #this regex get the session ID of current line that has a [] bracket around
        session = re.findall(r'\[\d+\]', line)[0]
        if  current_session_id != session:
            current_session_id = session
            array_of_ips.append(ip)
    return(array_of_ips)

def block_user(array):
    '''
    Block all IP address that tried at least 3 times. 
    '''
    ips_to_block = list(set([x for x in array if array.count(x) > 2]))
    for x in ips_to_block:
        fwblock.block_ip(x)
        print(x)


block_user(filter_ips_by_session_id(remove_unnecessary_lines(splitsshdlog)))


        


