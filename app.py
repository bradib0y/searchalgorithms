import time
import math

def recursivebinarysearch(list, target):
    if len(list) == 0:
        return False
    else: 
        midpoint = (len(list))//2

        if list[midpoint] == target:
            return True
        else:
            if list[midpoint] < target:
                return recursivebinarysearch(list[midpoint+1:], target)
            else:
                return recursivebinarysearch(list[:midpoint], target)

def binarysearch(list, target):
    """
    Return the index position of the target if found, else returns None
    """
    first = 0
    last = len(list) -1    

    while first <= last:
        midpoint = (first + last)//2
        if list[midpoint] == target:            
            return midpoint
        elif list[midpoint]<target:
            first = midpoint +1
        else:
            last = midpoint -1
    
    return None

def linearsearch(list, target):
    """
    Return the index position of the target if found, else returns None
    """   
    for i in range(0, len(list)):
        if target == list[i]:            
            return i
    return None

def testlog():
    for i in range(10, 19):
        numbers = range(0, int(math.pow(10, i)))
        number = (int(math.pow(10, i)) - 3)

        datastring = ""
        datastring += (str)(len(numbers))
        datastring += ";"

        print("")
        message = '-> Quantity: %s (10 to the power of %s)' % (number + 3, i)
        print(message)


        # log_start = time.time()
        # print(linearsearch(numbers, number))
        # result = time.time() - log_start
        print("Linear search: " , "null") # result)
        datastring += "null" # (str)(result)
        datastring += ";"


        log_start = time.time()
        print(binarysearch(numbers, number))
        result = time.time() - log_start
        print("Binary search: " , result)
        datastring += (str)(result)
        datastring += ";"

        log_start = time.time()
        print(recursivebinarysearch(numbers, number))
        result = time.time() - log_start
        print("Recursive binary search: " , result)
        datastring += (str)(result)
        
        
        file = open("data.csv", "a")
        file.write(datastring + "\n")
        file.close()

testlog()

