from colorama import * # To change font colors (https://github.com/tartley/colorama)
from random import randint

width = 25 # Tree width
body_height = 25 # Height without stand
full_height = 31 # Total height

tree = ''
for x in range(1, full_height, 2):
    s = ''
    center = int((width-1)/2)
    padding = center-int((x-1)/2)
    
    print('\n', end='') 
    
    if x == 1 :
        print(' '*padding, end='') 
        print(Fore.RED + '*', end='') 
    elif x < body_height:   
        print(' '*padding, end='')
        for y in range(0,x):
            b = randint(0, width) # Location to add random decoration 1
            a = randint(0, width) # Add random decoration 2
            c = randint(0, width) # Add random decoration 3
            if y==b:
                print(Fore.YELLOW + 'o', end='') 
            elif y==a:
                print(Fore.CYAN + '@', end='') 
            elif y==c:
                print(Fore.RED + '+', end='') 
            else:
                print(Fore.GREEN + '^', end='')  
        
        
    elif x == body_height:
        print(' '*padding, end='') 
        print(Fore.BLUE + '#'*width, end='') 
    elif x > body_height and x < full_height:
        print(' '*center, end='') 
        print(Fore.MAGENTA + 'II', end='')  
        
print('\n', end='') 
print(('~'*width).center(width))  
print(Fore.RED + 'MERRY CHRISTMAS 2022'.center(width)) 
print(Fore.RED + 'AND'.center(width))
print(Fore.RED + 'HAPPY HOLIDAYS !'.center(width))
print(('~'*width).center(width)) 