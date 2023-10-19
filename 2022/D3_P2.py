list = open('input3.txt', 'r')

content = list.readlines() 

total = 0 

numLines = len(content)

print(numLines)

for i in range(0, 300, 3): #for loop in range 0-299 and incremnet by 3 
    # Get next line from file
    lineREAD = list.readline()
    group = []
    
    for j in range(3):
        group.append(content[i+j])
   
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