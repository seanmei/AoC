max = [0,0,0] #current 3 highest

sum = 0 #total for each elf 


cals = open('input.txt', 'r')

def calCheck(sum): 
    max.sort()
    if sum > max[0]:
        max[0]=sum   

while True:

    # Get next line from file
    line = cals.readline()
    if not line:
        break
    if line == "\n":
        calCheck(sum)
        sum =0 #rest counter 
    else:
        sum += int(line)

print(max)
total = 0
for x in max: 
    total += x #total of all 3 elves 
print(total)

    
    