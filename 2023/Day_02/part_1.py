sum =0

#read input into a list 
input = open("input.txt","r")

games = input.read().splitlines() 



for index, game in enumerate(games): 
    #remove game number from string and use index instead 
    new_game = game.split(':')
    new_game = new_game[1]
    
    hands = new_game.split(';')
    #print(hands)
    flag = True
    for colors in hands: 
        color = colors.split(',')
        
        for vals in color: 
            #print("this:", vals)
            val = vals.strip()
            
            num = val.split(' ')
            print(num)
            flag = True
            if num[1] == 'green':
                if int(num[0]) <= 13:
                    pass
                else:
                    flag = False
                    break
                
            if num[1] == 'blue':
                if int(num[0]) <= 14:
                    pass
                else:
                    flag = False
                    break
                
            if num[1] == "red":
                if int(num[0]) <= 12:
                    pass
                else:
                    flag = False
                    break
        if flag == False: 
            break
            
    if flag == True:
        print('valid')
        sum += index+1
        
print("The sum is:", sum)
    

