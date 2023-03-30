import time 
import socket 
import sys 

def main () : 
    sock = socket.socket (socket.AF_INET , socket.SOCK_STREAM)
    server_addr = ('localhost' , 10001)

    sock.bind (server_addr)

    sock.listen(1)

    while (True): 
        print ("Serveur waiting for connexion")
        conn , client = sock.accept() 
        try : 
            print ("connecetion from " , client) 
            while (True) : 
                data = conn.recieve(16)
                print (data) 
            if (data) : 
                conn.sendall ("hello merci pour connexion")
            else:
                print ("no more data")
            break 
        finally :
            sock.close()     

main ()