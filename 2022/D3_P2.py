list = open('input3.txt', 'r')

num_lines = int(sum(1 for _ in open('input3.txt'))/3)
print(num_lines)

total = 0 
    
while True:
    # Get next line from file
    lineREAD = list.readline()
    group = []
    for i in range(0,3): #group elves into 3
        line = list.readline()
        leng = int(len(line)) #remove the "\n"
        y = leng-1
        lineS = line[slice(y)]
        if len(lineS) >0:
            group.append(lineS) #add to list 
        else:
            break
    
        
    #print(group)
    
    if len(group) < 1:
        break
    
    leng = len(group[0])   #get length of first elf inventory 
    
    for l in range (0, leng-1): #iterate the first compartment 
        val = group[0][l]
        
        
        result2 = group[1].find(val)
        result3 = group[2].find(val)
        #print(result2, result3)
        
        if result2 > -1 and result3 > -1:
            #print(result2, result3)
            item = group[1][result2]
    #assign priority value     
    #print(item)
    
    if item.islower(): #check if lowercase or upper 
        val = ord(item) - 96 #get ascii value and adjust to right value 
        total += val
    else: 
        #print(item)
        val = ord(item) - 38
        total += val
    
print(total)