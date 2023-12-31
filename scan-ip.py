#!/bin/python3

import socket
import sys

try:
    if len(sys.argv) == 2:

        ip_address = sys.argv[1]
        if ip_address == '0.0.0.0':
            print('You provided a default IP Address')
            print('Please provide a valid host IP Address')
            sys.exit()
        
        ip_check = socket.inet_aton(sys.argv[1])
        if ip_check:
            print('Valid IP Address!')


    target = socket.gethostbyname(sys.argv[1])
    for port in range (20, 500):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(1)
        c = s.connect_ex((target, port))
   
        if c == 0:
           print(f'Port {port} is open')
        s.close()

except OSError:
    print('Illegal IP address string')       
    sys.exit()
     
except socket.error:
    print('Connection to target failed!')
    sys.exit()
    
except socket.gaierror:
    print('Host name resolution failed!')
    sys.exit()

except IndexError:
    print('Enter an IP Address please')
    
except KeyboardInterrupt:
    print('Exciting the system!')
    sys.exit()
