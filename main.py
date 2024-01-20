# For showing banner
import pyfiglet
# For handling exceptions
import sys
# For handling the connections
import socket
# To get the date and time
from datetime import datetime

# Now Create Banner
ascii_banner = pyfiglet.figlet_format("Scan the Ports")
print(ascii_banner)

# Get Target
target = input(str("Target IP: "))

# Descriptions
print("_" * 50)
print("Scanning Target: " + target)
print("Scanning started at: " + str(datetime.now()))
print("_" * 50)

# Get Connections
try:
    # Scan every port on the given ip
    for port in range(1,65535):
        # creates a new socket object using the given address family, socket type, and protocol number
        # AF_INET parameter specifies the address family, which is used to identify the type of addresses that the socket can communicate with. In this case, AF_INET indicates that the socket can communicate with IPv4 addresses.
        # SOCK_STREAM indicates that the socket provides a reliable, stream-oriented connection
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        # This means that if a socket operation takes longer than 0.5 seconds to complete, a socket.timeout exception will be raised
        socket.setdefaulttimeout(0.5)

        # Result open ports
        result = s.connect_ex((target,port))    # It attempts to establish a connection to a remote server using the connect_ex() method of a socket object
        if result == 0:
            print("[*] Port {} is open".format(port)) # The format() method is used to substitute the value of the port variable into the string.
        s.close()

except KeyboardInterrupt: # raised when the user presses Ctrl+C or Ctrl+Z on their keyboard
    print("\n Exit")
    sys.exit()

except socket.error:  # This exception is raised when a socket operation fails.
    print("\ Host is not Responding:(")
    sys.exit()
