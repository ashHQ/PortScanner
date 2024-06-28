import socket
from _pydatetime import datetime


target = input("Enter the target IP address: ")

def port_scan(target):
    try:
        ip = socket.gethostbyname(target)
        print(f"scanning the target {ip}")
        print("time started: ",datetime.now())
        for port in range(1,65535):
            sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
            sock.settimeout(3)
            result = sock.connect_ex((ip, port))
            if result == 0:
                print("port {} is open".format(port))
            sock.close()
    except socket.gaierror:
        print("hostname could not be resolved")
    except socket.error:
        print("could not connect to the server")
port_scan(target)