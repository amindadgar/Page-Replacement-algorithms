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
    	print(i)

def LRU(request,bufferSize):
    BUFFER =[]


bufferSize = input("Please Enter Buffer Size: ")
a= input("Please choose one of the page replacement algorithm\n 1.MRU\n 2.LRU\n 3.Clock\n 4.Random\nenter number for choosing algorithm as you wish :) \n")
print("MRU is doing now")
request = raw_input("please Enter Request pages\n (example: ABHY)\n")
MRU(request,bufferSize)

