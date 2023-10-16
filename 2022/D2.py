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
            "X": 3 + 1,
            "Y": 6 + 2,
            "Z": 0 + 3
        }[p2]
    elif p1 == 'B': 
        totalScore += {
            "X": 0 + 1,
            "Y": 3 + 2,
            "Z": 6 + 3
        }[p2]
    elif p1 == 'C':
        totalScore += {
            "X": 6 + 1,
            "Y": 0 + 2,
            "Z": 3 + 3
        }[p2]

        
print(totalScore)