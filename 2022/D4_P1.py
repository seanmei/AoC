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
    
    print(p1, p2)
    
    if int(p1[0]) <= int(p2[0]) and int(p1[1]) >= int(p2[1]):
        count +=1 
    elif int(p2[0]) <= int(p1[0]) and int(p2[1]) >= int(p1[1]):
        count +=1
        
print(count)
    
  
    
    