'''
This script takes a file and checks if the ip address appears at least 3 times then it blockes that IP in the firewall

-h = print a short help text and the script will 'not' be executed.
-v will print for each IP address the 'IP address + blocking'  that would be blocked to the screen .
-d prints 'debug' output, default no output is shown.
-n read the log file(s) but will not call block_ip()
other option = the script will wrtite the help to stderr and stop immediately.
other args are files [default is ./sshdlog]
Catch exceptions . If a file cannot be read, print a message to stderr and move on to the next file.
'''
#!/usr/bin/python3
from block_ssh_attempts1 import block_user
import re
import fwblock
import getopt
import sys


script_args = sys.argv[1:] 

option_string = 'dhvn'
opts, extra_args = getopt.getopt(script_args, option_string)


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

def bad_ips(array):
    '''
    Returns all IP address that tried at least 3 times. 
    '''
    return list(set([x for x in array if array.count(x) > 2]))

def block_ips(array, printIPS = False):
    '''

    '''
    for x in array:
        fwblock.block_ip(x)
        if printIPS:
            print("blocking" + x)
    
    

# block_ips(
#     bad_ips(
#         filter_ips_by_session_id(
#             remove_unnecessary_lines(
#                 splitsshdlog
#     ))))



#settings
block_users = True
show_help_text = False
print_bad_ips = False
print_debug = False

#!/usr/bin/python3
# If -h option doesn't exist, make sure your script doesn't contain debug prints.


for option, option_arg in opts:
    if option == '-h':
        
        # break
        show_help_text = True
    elif option == '-v':
        print_bad_ips = True
    elif option == '-d':
        print_debug =True
    elif option == "-n":
        block_users = False
    # else option == '-'
    #     print('\t', sys.argv[0], ' [-d][-f <filename>][-h]', sep='')
    #     sys.exit(0) # don't execute if user doesn't know how to use this script



files = []
if extra_args == []:
    files.append("./sshdlog")
else:
    files = extra_args

for x in files:
#read the log file
    with open(x) as sshdlog:
        readsshdlog = sshdlog.read()
        splitsshdlog = readsshdlog.splitlines()
    if show_help_text:
        #the same as the help text of the module.
        print("This script takes a file and checks if the ip address appears at least 3 times"
        +"then it blockes that IP in the firewall\n-h = print a short help text and the script"
        +"will 'not' be executed.\n-v will print for each IP address the 'IP address + blocking'"
        +" that would be blocked to the screen .\n-d prints 'debug' output, default no output is shown."
        +"\n-n read the log file(s) but will not call block_ip()\nother option = the script will wrtite "
        +"the help to stderr and stop immediately.\nother args are files [default is ./sshdlog]\nCatch exceptions ."
        +"If a file cannot be read, print a message to stderr and move on to the next file.")
        break
    elif print_bad_ips and block_users:
        block_ips(
            bad_ips(
                filter_ips_by_session_id(
                    remove_unnecessary_lines(
                        splitsshdlog
            ))), True)
    elif print_bad_ips and  not block_users:
        print(
            bad_ips(
                filter_ips_by_session_id(
                    remove_unnecessary_lines(
                        splitsshdlog
            ))))
    elif not print_bad_ips and  not block_users:
        bad_ips(
            filter_ips_by_session_id(
                remove_unnecessary_lines(
                    splitsshdlog
        )))



