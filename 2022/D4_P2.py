list = open('input4.txt', 'r')

count = 0 #number of fuly containted pairs 

while True:
    # Get next line from file
    line = list.readline()
    if not line:
        break
    #split each line to the id range of each elf 
    data = line.split(',')
    e1 = data[0]
    e2 = data[1]
    #print(e1, e2)
    
    #split again into each specific ID 
    p1 = e1.split('-')
    p2 = e2.split('-')
    
    
    a1 = p1[0]
    a2 = p1[1]
    b1 = p2[0]
    b2 = p2[1]
    print(a1)
    
    if (a2 >= b1 and a2 <= b2) or (b1 >= a1 and b1 <= a2): 
        count+=1
    
    
    

        
        #check the if p1 in p2 since u only check if p2 in p1 
print(count)
    
  
    
    