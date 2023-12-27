
import socket, sys
from datetime import datetime as dt

margin = ' ' * 30
print('-'* 100)
print()
print(f'{margin} Welcome to this ports\' scan program!')
print()
print('-'* 100)

# Target definition

if len(sys.argv) == 2:
    try:
        socket.inet_aton(sys.argv[1])
        if sys.argv[1] == '0.0.0.0':
            print('This a default IP Address')
            print('Please enter a valid host\'s IP Address')
            sys.exit() 
        else:
            print('Valid IP Address!')
    except OSError:
        print('Invalid IP Address')
        sys.exit()
    target = socket.gethostbyname(sys.argv[1])
else:
    print('Please enter 02 arguments as follow: "python3 <filename.py> <IP Address>"')
# Socket setup with IPv4 Familly and TCP as transport protocol

try:
    for port in range (1, 1025):
        print(f'Connection with {target} through port {port}')
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(1)
        c = s.connect_ex((target, port))
        print(f'Connection with {target} through port {port} established!')

        if c == 0:
            print(f'Port {port} is open!')
        else:
            print(f'Port {port} is closed!')
    sys.exit()
except socket.error:
    print(f'Connection not set up successfully!')
    sys.exit()
except socket.gaierror:
    print(f'Host name not resolved successfully!')
    sys.exit()
except KeyboardInterrupt:
    print(f'Exciting the program!')
    sys.exit()
