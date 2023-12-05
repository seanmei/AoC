sum =0

#read input into a list 
input = open("input.txt","r")

games = input.read().splitlines() 



for index, game in enumerate(games): 
    min_green =0 
    min_blue = 0
    min_red = 0
    power =0 
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
            if num[1] == 'green':
                if  min_green < int(num[0]):
                    min_green = int(num[0])
                    #print("Current Lowest Green is: ", min_green)
               
                
            if num[1] == 'blue':
                if min_blue < int(num[0]):
                    min_blue = int(num[0])
                    #print("Current lowest blue is: ", min_blue)
   
                
            if num[1] == "red":
                if min_red <= int(num[0]):
                    min_red = int(num[0])
                    #print("Current lowest blue is: ", min_red)
  
    print("lowest blue is: ", min_blue) 
    print("lowest red is: ", min_red)  
    print("lowest green is: ", min_green)         
    power = min_red*min_blue*min_green
    sum += power
        
print("The sum of power is: ", sum)
    

