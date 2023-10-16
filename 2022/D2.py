totalScore = 0

guide = open('input2.txt', 'r')
    
while True:

    # Get next line from file
    line = guide.readline()
    if not line:
        break
    p1, p2 = line.split()
    
    if p1 == 'A':
        totalScore += {
            "X": 0 + 3,
            "Y": 3 + 1,
            "Z": 6 + 2
        }[p2]
    elif p1 == 'B': 
        totalScore += {
            "X": 0 + 1,
            "Y": 3 + 2,
            "Z": 6 + 3
        }[p2]
    elif p1 == 'C':
        totalScore += {
            "X": 0 + 2,
            "Y": 3 + 3,
            "Z": 6 + 1
        }[p2]

        
print(totalScore)