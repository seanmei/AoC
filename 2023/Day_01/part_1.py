sum =0

#read input into a list 
input = open("input.txt","r")

document = input.read().splitlines()  #puts each line to a list as a string without \n

#get first digit 
def getFirst (val):
    first =''
    for element in val:
        if element.isdigit(): 
            first = element
            print ('first is: ', first)
            break
        else:
            pass

    return first

    
#get last digit
def getLast (val):
    last =''
    flag = False
    for element in reversed(val):
        try:
            int(element)
            flag = True
        except:
            flag = False
            
        if flag == True:
            last = element
            print ('last is: ', last)
            break
        
    return last        
    
    
for i in document: 
    first = getFirst(i)
    last = getLast(i)
    total = str(first)+ str(last)
    sum += int(total)

print(sum)

