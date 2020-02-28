import time

def MRU(request,bufferSize):
    BUFFER = []
    characterCounter = 0
    for i in range(bufferSize):  #At first just put characters in buffer
        if i<len(request):
    	    BUFFER.append(request[i])
    	    characterCounter = i
    	    print("'"+request[i]+"' is added and Page Fault")
    characterCounter+=1
    index = bufferSize-1
    while (characterCounter<len(request)):
        if(request[characterCounter] in BUFFER):
    	    index=BUFFER.index(request[characterCounter])
    	    print("'"+request[characterCounter]+"' is available in buffer")
    	    characterCounter+=1
        else:
    	    BUFFER[index] = request[characterCounter]
    	    print("'"+request[characterCounter]+"' is added and Page Fault")
    	    characterCounter+=1
    print("\n\nFinished and now showing buffer")
    for i in BUFFER:
    	print(i+" "),
    print("\n\n\n")

def LRU(request,bufferSize):
    BUFFER =[]
    BUFFER_TIMER = [0]*bufferSize
    for i in range(bufferSize):  #At first just put characters in buffer
    	if i<len(request):
    		BUFFER.append(request[i])
    		BUFFER_TIMER[i] = bufferSize-i-1
    
    






print("WARINING: This code in written in python version 2 So if you have python 3 you maybe have an error for raw_input\n")
bufferSize = input("Please Enter Buffer Size: ")
request = raw_input("please Enter Request pages\n (example: ABHY)\n")
while(True):
    a=input("Please choose one of the page replacement algorithm\n 1.MRU\n 2.LRU\n 3.Clock\n 4.Random\n 5.To insert page request again\n 6.To quit the application\nenter number for choosing algorithm as you wish :) \n")
    if(a==1):
    	MRU(request,bufferSize)
    elif(a==2):
    	LRU(request,bufferSize)
    elif(a==3):
    	print("Unfortunatly clock algorithm is not done yet please choose another one")
    	#CLOCK(request,bufferSize)
    elif(a==4):
    	print("Unfortunatly Random algorithm is not done yet please choose another one")
    	#Random(request,bufferSize)
    elif(a==5):
        request = raw_input("please Enter Request pages\n (example: ABHY)\n")
    elif(a==6):
        print("\nExiting application ."),
        time.sleep(0.4)
        print("."),
        time.sleep(0.4)
        print(".")
        time.sleep(0.4)
        break
    else:
        print("Wrong input!\n Please try again")
        
