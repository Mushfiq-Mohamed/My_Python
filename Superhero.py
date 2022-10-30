print('__what is your name?__')

name = input('Enter your name here: ')
print('Hi there ' + name)

print ('___wanna play a game?___')

Answers = input("Type Yes or No\n")

if Answers == 'Yes':
    print ('Lets get started')
elif Answers == 'yes':
    print('Lets Get Started')
elif Answers == 'YES':
    print('Lets Get Started')
else:
     exit()

print("\n")
print("In this game you will be choosing a hero and a villain will be randomly generated for you. Good Luck!\n")
print("\n")

print("1. Batman\n")
print("2. SpiderMan\n")
print("3. Superman\n")
print("4. Flash\n")
print("5. Aquaman\n")
print("6. Wolverine\n")
print("7. Hulk\n")
print("8. GreenLantern\n")
print("9. Scorpion\n")
print("10. Subzero\n")
print("11. Kratos\n")
print("12. Martian-Manhunter\n")
print("13. Wonder Woman\n")
print("14. Green Arrow\n")



your_info = {'1': "Your Batman", '2':"Your SpiderMan", '3':"Your Superman", '4':"Your Flash", '5':"Your Aquaman", '6': "Wolverine", '7': "Hulk", '8': "GreenLantern",
 '9': "Scorpion", '10': "Subzero", '11': "Kratos", '12' : 'Your Martian-Manhunter', '13' : 'Wonder Woman', '14' : 'Green Arrow'}

Number = input("___choose a number within range 1 - 14: \n")

if Number == "1" :
    print(your_info['1'])

elif Number == "2" :
    print(your_info['2'])

elif Number == "3" :
    print(your_info['3'])

elif Number == "4" :
    print(your_info['4'])

elif Number == "5" :
    print(your_info['5'])

elif Number == "6" :
    print(your_info['6'])

elif Number == "7" :
    print(your_info['7'])

elif Number == "8" :
    print(your_info['8'])

elif Number == "9" :
    print(your_info['9'])

elif Number == "10" :
    print(your_info['10'])

elif Number == "11" :
    print(your_info['11'])

elif Number == "12" :
    print(your_info['12'])

elif Number == "13" :
    print(your_info['13'])

elif Number == "14" :
    print(your_info['14'])


import random

your_villian = {'1': ["Joker","Lex Luthor","Darkseid","Reverse Flash","DeathStroke","Homelander","Bizzaro","RedHood","Sinestro","Kotel Kahnth","Batman who Laughs","Magnito",
"Brainiac","Venom","Thanos","Ultron","Doomsday","Trigon","Dr.Doom","Dead Pool","Mr.Freeze","Penguin","Riddler","Rhino","ScareCrow","Gorilla Grodd","Loki","Solomun Grundy","Bane",
"Cheetah","Green Goblin","Harley Quinn", "Poison Ivy", "Savitar", "Carnage", "Black Manta", "Black Adam", "Cyborg Superman", "Electro", "Killer Croc", "Promethueus"], '2': []}

print("Your villian will be :")
random_villan = random.choice(your_villian['1'])
print(random_villan)












