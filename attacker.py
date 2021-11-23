from socket import *
import pyautogui
from io import StringIO
from time import sleep
def return_print(*message):
	io=StringIO()
	print(*message,file=io,end="")
	return io.getvalue()
def main():
	port = 5555
	serverSock = socket(AF_INET, SOCK_STREAM)
	serverSock.bind(('', port))
	serverSock.listen(1)


	connectionSock, addr = serverSock.accept()

	print(str(addr), '')

	while True:
	    value=return_print(pyautogui.position())
	    value=value.split("(")
	    value=value[1].split(")")
	    value=value[0]#x=300,y=300
	    xpandyp=value.split(",")
	    xp=xpandyp[0].split("=")
	    xp=xp[1]
	    yp=xpandyp[1].split("=")
	    yp=yp[1]
	    pos=xp+","+yp
	    print(pos)
	    
	    sendData=pos
	    print(sendData)
	    connectionSock.send(sendData.encode('utf-8'))#300,300
	    sleep(0.1)
  
print("""
______  _____ ______   ___    _   _  _____ ______  _   _  _____ 
| ___ \|  ___|| ___ \ / _ \  | | | ||_   _|| ___ \| | | |/  ___|
| |_/ /| |__  | |_/ // /_\ \ | | | |  | |  | |_/ /| | | |\ `--. 
|  __/ |  __| |    / |  _  | | | | |  | |  |    / | | | | `--. \
| |    | |___ | |\ \ | | | | \ \_/ / _| |_ | |\ \ | |_| |/\__/ /
\_|    \____/ \_| \_|\_| |_/  \___/  \___/ \_| \_| \___/ \____/ 
                                                                
""")
start=int(input("""
Enter 1 if you want to run
Enter 2 to exit
:
"""))
if start == 1:
	main()
elif start==2:
	quit()
else:
	quit()
