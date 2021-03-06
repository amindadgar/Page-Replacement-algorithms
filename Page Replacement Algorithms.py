import time
import random 


def MRU(request,bufferSize):
    BUFFER=["/"]*bufferSize
    characterCounter = 0

    index = 0
    while (characterCounter<len(request)):
        if(request[characterCounter] in BUFFER):
    	    index=BUFFER.index(request[characterCounter])
    	    print("'"+request[characterCounter]+"' is available in buffer")
    	    characterCounter+=1
        else:
            BUFFER[index]=request[characterCounter]
            if "/" in BUFFER:
                index+=1
                if(index == bufferSize):
                    index = bufferSize - 1
            print("'"+request[characterCounter]+"' is added and Page Fault")
            characterCounter+=1
    print("\n\nFinished and now showing buffer")
    for i in BUFFER:
    	print(i+" "),
    print("\n\n\n")

def LRU(request,bufferSize):
    BUFFER=["/"]*bufferSize
    BUFFER_TIMER = [0]*bufferSize
    number = -1
    index=-1   #number and index are variables for our timer
    characterCounter=0

    while characterCounter<len(request):
        if (request[characterCounter] not in BUFFER):   #if the page was not in buffer
            for j in range(len(BUFFER_TIMER)):
            	if number < BUFFER_TIMER[j]:
            	    number = BUFFER_TIMER[j]
            	    index = j                      #Find the biggest number in timer
            BUFFER[index] = request[characterCounter]
            print("'"+request[characterCounter]+"' is added and Page Fault")
            BUFFER_TIMER[index]=0
            for i in range(len(BUFFER_TIMER)):
                if(i!=index):
                    BUFFER_TIMER[i]+=1    #increase timer for other pages in buffer
            characterCounter+=1
        else:                   #if the page was in buffer
            index = BUFFER.index(request[characterCounter])
            BUFFER_TIMER[index]=0
            print("'"+request[characterCounter]+"' is available in buffer")
            for i in range(len(BUFFER_TIMER)):
                if(i!=index):
                    BUFFER_TIMER[i]+=1            ##increase timer for other pages in buffer
            characterCounter+=1

    print("\n\nFinished and now showing buffer")
    for i in BUFFER:
    	print(i+" "),
    print("\n\n\n")
    
def Clock(request,bufferSize):
    BUFFER=["/"]*bufferSize   # / is sth that would never be in page requests
    characterCounter=0
    BUFFER_REF_BIT=[False]*bufferSize

    CurrentBit = 0
    while characterCounter<len(request):
        if request[characterCounter] in BUFFER:
            print("'"+request[characterCounter]+"' is available in buffer")
            BUFFER_REF_BIT[BUFFER.index(request[characterCounter])] = True
            characterCounter+=1
        else:
            while BUFFER_REF_BIT[CurrentBit] == True:
                BUFFER_REF_BIT[CurrentBit] = False
                CurrentBit+=1
                if(CurrentBit==bufferSize):
                    CurrentBit=0
            BUFFER[CurrentBit]=request[characterCounter]
            BUFFER_REF_BIT[CurrentBit]=True
            print("'"+request[characterCounter]+"' is added and Page Fault")
            characterCounter+=1
    print("\n\nFinished and now showing buffer")
    for i in BUFFER:
        print(i+" "),

    print("\n\n\n")    



def Random(request,bufferSize):
    BUFFER = ["/"]*bufferSize
    i=0
    bufferChoice = [i]
    while "/" in BUFFER:
        if request[i] in BUFFER:
            print("'"+request[i]+"' is available in buffer")
        else:
            BUFFER[i] = request[i]
            print("'"+request[i]+"' is added and Page Fault")
            j=random.randrange(0,bufferSize,1)
            while j in bufferChoice:
                j=random.randrange(0,bufferSize,1)
                if len(bufferChoice) == bufferSize:
                    break
            i=j
            bufferChoice.append(i)
            

    characterCounter = i
    while characterCounter < len(request) :
        if request[characterCounter] not in BUFFER:
            BUFFER[random.randrange(0,bufferSize,1)] = request[characterCounter]
            print("'"+request[characterCounter]+"' is added and Page Fault")
            characterCounter+=1
        else:
            print("'"+request[characterCounter]+"' is available in buffer")
            characterCounter+=1

    print("\n\nFinished and now showing buffer")
    for i in BUFFER:
        print(i+" "),

    print("\n\n\n")    

        





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
    	Clock(request,bufferSize)
    elif(a==4):
    	Random(request,bufferSize)
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
        
