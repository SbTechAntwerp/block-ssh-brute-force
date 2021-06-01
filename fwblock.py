'''
Functions to add rules to the firewall.
'''

import ipaddress

blocked = set()

def block_ip(ip):
    '''
    This function adds a rule to the firewall to block all traffic from
    the given IP address.
    ip: IP address to block traffic from.
    '''
    global blocked

    ipaddress.ip_address(ip) # this will fail if an invalid IP address is passed

    if ip in blocked:
        raise RuntimeError('You\'re making the firewall slow! IP Address %s '
                'has already been blocked' % ip)

    blocked.add(ip)
