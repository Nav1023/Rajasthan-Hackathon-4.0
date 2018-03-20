import serial
import socket
sock=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
port = 9998

sock.bind(('172.26.58.207', port)) 
print ("socket binded to %s" %(port))
print ("Socket created successully.")
sock.listen(5)
print ("Socket is listening")
#arduino = ''   
try:
    arduino = serial.Serial('\\.\COM3',timeout=.1)
except:
    print("Please Check the Port..")

rawdata=[]
count=0
while count<30:
    rawdata.append(str(arduino.readline()))
    count=count+1
    print(rawdata)
    while True:
        c, addr  = sock.accept()
    print ("Got connection from ", addr)
    c.send(rawdata)
    #c.close()
def clean(L):
    newl=[]
    for i in range(len(L)):
        temp=L[i][2:]
        newl.append(temp[:-5])
    return newl
cleandata=clean(rawdata)

def write(L):
    file=open("data_raj.txt",mode='w')
    for i in range(len(L)):
        file.write(L[i]+'\n')
    file.close()

write(cleandata)

