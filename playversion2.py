#!/usr/bin/python3
# If -h option doesn't exist, make sure your script doesn't contain debug prints.


for option, option_arg in opts:
    if option == '-h':
        print(help(block_ssh_attempts))
    elif option == '-v':
        #first add the print statement into the bad ips
        print(bad_ips(filter_ips_by_session_id(remove_unnecessary_lines(splitsshdlog))))
    elif option == '-d':
        debug += 1
    elif option == ' ':
        if debug:     
        filenames.append(option_arg)
    
    elif option == '-'
        print('\t', sys.argv[0], ' [-d][-f <filename>][-h]', sep='')
        sys.exit(0) # don't execute if user doesn't know how to use this script


'''
This script takes a file and checks if the ip address appears at least 3 times then it blockes that IP in the firewall

-h = print a short help text and the script will not be executed.
-v will print for each IP address that would be blocked to the screen.
-d prints 'debug' output, default no output is shown.
-n read the log file(s) but will not call block_ip()
other option = the script will wrtite the help to stderr and stop immediately.
other args are files [default is ./sshdlog]
Catch exceptions . If a file cannot be read, print a message to stderr and move on to the next file.
'''

