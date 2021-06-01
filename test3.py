import ssl   
import socket

# Using the deprecated ssl.wrap_socket method





ssl.wrap_socket(socket.socket(),ssl_version=ssl.PROTOCOL_SSLv2,ca_certs="rr")
#s.wrap_socket(socket.socket())
#ssl.wrap_socket(socket.socket())
# Using SSLContext
context = ssl.SSLContext()


