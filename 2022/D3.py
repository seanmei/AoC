list = open('input3.txt', 'r')

total = 0 
    
while True:
    # Get next line from file
    line = list.readline()
    
    if not line:
        break
    else:
        leng = int(len(line)) #get the total nuber of items in the rucksack 
         #delete one space 
        
        p1 = int((leng/2)-1) #val to slice first half of rusckack 
        p2 = int(leng/2)
        p3 = int(leng-1)
        
        x = slice(p2)
        y = slice(p2, p3)
        
        r1 = line[x]#get items from first 1st compartment ie. first half 
        r2 = line[y] #gets items from 2nd compartment ie. second half
        
        print(r1, r2)
        
        item = '' #var for item in both 
        
        for l in range (0, p2): #iterate the first compartment 
            temp = r1[l] #get each letter 
            result = r2.find(temp) #find the index of the letter in the second compartment 
            if result > -1: #find returns -1 if no match found 
                item = r2[result] #get the letter that match 
                break
            else: 
                print('ERROR')
            
        #assign priority value     
        if item.islower(): #check if lowercase or upper 
            val = ord(item) - 96 #get ascii value and adjust to right value 
            total += val
        else: 
            #print(item)
            val = ord(item) - 38
            total += val

print(total)