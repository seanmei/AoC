sum =0

#read input into a list 
input = open("input.txt","r")

document = input.read().splitlines()  #puts each line to a list as a string without \n

numbers = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']



#get first digit 
def getFirstDigit (val): # 1,2,3 .....
    first =''
    index = 0
    for index, element in enumerate(val): #get index of num
        
        if element.isdigit(): 
            first = element
            index = index
            #print ('first is: ', first)
            break
        else:
            pass

    return [index, first]

    
#get last digit
def getLastDigit (val): #1, 2, 3, 4 ..... 
    last =''
    flag = False
    final_index = 0 

    for current_index, element in enumerate(val):
        #print("this", index, element)
        try:
            int(element)
            flag = True
        except:
            flag = False
            
        if flag == True:
            if current_index >= final_index:
                final_index = current_index
                last = element
            else: 
                flag = False
           
            
            #print ('last is: ', last)
        
        
    return [final_index, last]        

def getFirstLetter(val): # one, two, three .... 
    num_index = len(val)
    num = 0
    
    for index, number in enumerate(numbers): 
        temp = val.find(number)
        if temp >= 0 and  temp < num_index: 
            num_index = val.find(number) #inedx of number
            num = index +1 #value of the writen number     
            
    
    return [num_index, str(num)] 

def getLastLetter(val): # one, two, three .... 
    num_index = -1
    num = 0
    for index, number in enumerate(numbers): 
        temp = val.rfind(number) #find last occurence of number
        if temp >= 0 and temp > num_index :
            num_index = val.rfind(number) #inedx of number
            num = index +1 #value of the writen number     
            
              
    
    return [num_index, str(num)]
    
    
    
for index, i in enumerate(document):
    
    first_digit = getFirstDigit(i)
    last_digit = getLastDigit(i)
    first_letter_digit = getFirstLetter(i)
    last_letter_digit = getLastLetter(i)
    
    final_digit = ''
    
    print('line: ', index+1, i)
    print('last digit', last_digit)
    print('last letter digit', last_letter_digit)
    
    print('first digit', first_digit)
    print('first letter digit', first_letter_digit)
    if first_digit[0] ==0: 
        final_digit += first_digit[1]
    else: 
        if first_digit[0] < 0:
            final_digit += first_letter_digit[1]
        elif first_letter_digit[0] < 0:
            final_digit += first_digit[1]
        else: 
            if first_digit[0] < first_letter_digit[0]:
                final_digit += first_digit[1]
            else: 
                final_digit += first_letter_digit[1]
       
           
    if last_digit[0] < last_letter_digit[0]:
        final_digit += last_letter_digit[1]    
    else:
        final_digit += last_digit[1]
            
    sum += int(final_digit)    
    print(final_digit)
    final_digit = ''
    
print(sum)
    
    #total = str(first_digit)+ str(last_digit)
    #sum += int(total)
    #print('first:', first_letter_digit)
   # print('last: ', last_letter_digit)

