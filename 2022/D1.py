
max = 0 #current highest


sum = 0 #total for each elf 

cals = open('input.txt', 'r')

while True:

    # Get next line from file
    line = cals.readline()
    if not line:
        break
    if line == "\n":
        if sum > max: #check for new highest for each elf 
            max = sum
        sum =0 #rest counter 
    else:
        sum += int(line)
print(max)
    
    
