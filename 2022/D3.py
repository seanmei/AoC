
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
        
        x = slice(p1)
        y = slice(p2, p3)
        
        r1 = line[x]#get items from first 1st rucksack ie. first half 
        r2 = line[y] #gets items from 2nd rucksack ie. second half
        
        item = ''
        
        for l in range (0, p1):
            temp = r1[l]
            result = r2.find(temp)
            if result >0: 
                item = r2[result]
                print(item)
                break
        if item.islower():
            val = ord(item) - 96
            total += val
        else: 
            val = ord(item) - 13
            total += val

print(total)