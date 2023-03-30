import threading 
import time 
import pyfiglet 
import socket 
"""                       Scanner Des ports                                     """ 
"""                       Synchronisation entre les threads                     """ 

exitFlag = 0 

threadLock = threading.Lock () 
threads = []

class Mythread (threading.Thread) : 
    def __init__ (self ,name , num_port ) :
        threading.Thread.__init__ (self) 
        self.name = name 
        self.num_port = num_port 
    def run (self) :
        threadLock.acquire ()
        #print ("Starting Scanning port " , self.num_port ) 
        K = scan_port (self.num_port ) 
        if (K):
            print ("Le port {} est ouvert".format (self.num_port))
        print ("Exiting Scanning port  ")
        threadLock.release ()


def scan_port (num_port) : 
    addr = "localhost" 
    s = socket.socket (socket.AF_INET , socket.SOCK_STREAM)
    try : 
        s.connect ((addr,num_port))
        return True 
    except : 
        return False 



def barriere (text): 
    ascii_banner = pyfiglet.figlet_format (text)
    print (ascii_banner)


def main () :
    barriere ("SCAN PORT")
    for k in range (10000,10002): ## Vous pouvez utulisé n'importe quelle port compris entre 0-65553 .
        thread = Mythread ("scanNum" , k) 
        thread.start () 
        threads.append(thread) 

    for t in threads : 
        t.join()
    print ("Quitter tous les threads")


main () 