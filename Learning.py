import random

def print_character():
    print("    _______      ")
    print("   ( 0 - 0 )     ")
    print("   \\|     |/     ")
    print("     -----      ")
    print("     |   |       ")
def variable_examples():
    greeting = "hello" # This creates a new string Variable
    height_inches = 69 # This creates a new integer Variable
    cost_of_sandwich = 5.46 # This creates a new float Variable

    height_inches += 5
    print(height_inches)

    say = "How are you doing?"
    movie_length_hours = 2
    ticket_price = 11.22
    
##### INPUTTING FROM USERS #####
    
def nice_name():
    name = input("what's your name? ")
    print(" Your name is", name )
    print("hello,", name)
    print("\"", name, "\" is a nice name")

#madlib
def madlib_game():
    adjective1 = input("Enter a adjective: ")
    adjective2 = input("Enter a adjective ")
    print("It was a", adjective1, "cold December morning ")
    adjective3 = input("Enter a adjective: ")
    verb1 = input("Enter a verb: ")
    print("I woke up to the", adjective3, "smell of my neighbor's dog", verb1)
    verb2 = input("Enter a verb:")
    print("Downstairs I could", verb1, "the toast in the toaster.")
    adjective4 = input("Enter a adjective: ")
    noun1 = input("Enter a noun: ")
    print("The day begins to feel, like a", adjective4, "summer day, in a couple of seconds. The" , noun1, "began to feel so different.")

def amountspent():
    percent_tax = 9
    percent_tip = 15
    amountspent = 25

# SUBTOTAL = HOW MUCH WE SPEND + OUR TAX
# we can multiply by doing 2 * 8

    tax = percent_tax/100 * amountspent
    print(tax)
    subtotal = tax+ amountspent
    print(subtotal)

#I will not buy a pie unless it's less than 40 cents per square inch
    radius = 8
# area of a circle/pie is pi r squared
    area = 3.14 * radius ** 2
    print(subtotal / area < 0.40)

#BOOLEAN: True or False

##print(3 < 5)
##print(3 > 5)

#example
def totalmealprice ():
    costofmeal = float(input("How much did your meal cost?  "))
    print(costofmeal)
    percent_tax = 9
    tax = percent_tax/100 * costofmeal
    subtotal = tax + Costofmeal
    print(subtotal)
    percent_tip = 15
    tip = percent_tip/100 * Costofmeal
    total = subtotal + tip
    print(total)

    costofmeal = float(input("How much did your meal cost? "))
    taxrate = float(input("What is the tax rate? "))
    tiprate = float(input("What is the tip rate? "))
    tax = taxrate/100 * costofmeal
    tip = tiprate/100 * costofmeal
    total = tax + tip + costofmeal
    print(total)

def whospaying():
    amountspent =float(input("How much did you spend on your meal?"))
    print(type(amountspent))
    ans = input('Are you splitting the bill today? (Y/N)')
    print(ans)
    if (ans == 'Y'):
        print("You're splitting the bill today!") 
    if (ans == 'N'):
        print("Hope you got money in yout wallet!")

### KEYWORDS AND FUNCTION ###
# special words for that language
# Each keyword preforms a diffrent kind of task
# the IDE will color in special color
#cannot be used as identifiers -- words you choose for variables
# and other stuff
# parenthesis are optional
def xequals ():
    x =2
    if x == 2:
        print("X equals 2!!!!!")

#class
#while
#is
#for
#and 
#or 
#not
#def
#return
#global

#### Functions ####
# code that you can run to preform a specific task,
# You say the name of function + infro to work on, and it does the work
#Example: print(), input(), float()
def hi_class():
    print("Hi, Class")

####### IF/ ELIF/ ELSE #######
#'if' by itslef
#'if' with 'else'
#'if' with 'elif' and 'else'
#Use of 'and' in if statement
def age ():
    age = int(input("What is your age? "))
    if (0 < age and age < 4):
        print("You are a toddler")
    elif (3 < age and age < 13):
        print("You are a child")
    elif (12 < age and age < 20):
        print("You are a teenager")
    else:
        print("You are getting old")
#use an IF STATEMENT when you have to make a decision
#CONDITION- something you check for either true or false
#BOOLEAN - Only can be true or false

#######Random Number##########
#At the top of the file put "import random"
        
def random_number ():
    random_number = random.randint(0,250)
    print (random_number)

######Activity: Insult/ Compliment game#######
def insultcompliment ():
    random_number = random.randint(0,10)
    if random_number == 0 or random_number == 1:
        print("You look nice")
    elif random_number == 3 or random_number == 2:
        print("You suck")
    elif random_number == 5 or random_number == 4:
        print(" You smell")
    elif random_number == 6 or random_number == 7:
        print(" Your nice")
    else:
        print("Nice eyes")

############LOOPS##############
# Use loops when:
#    Repeat some code
#    Get rid of duplicate code
#There is various kinds of loops:
#     while loops
#     for loops
#     other loops
#######COMPARISON BETWEEN IF AND LOOPS######
# If statement and LOOPS
#both(Use Conditions)(Need code to run)
#if(check once)(IF/ELIF/ELSE)
#Loops(check repeatedly)(while only)
#If statement and LOOPS are not the same

def loop():
    counter = 99
    while counter > 10:
        counter -= 5
        print(counter)
    print("done")

    number = 1
    while number < 1000:
        number += 1
        print(number)

    countdown= 1000000
    while countdown > 1:
        countdown -= 1
        print(countdown)
    print("Blast off")

    while True:
        answer = input( "Am I cooler than you? ")
        if (answer == "yes"):
            break
    print("I'm glad you admit it")

    number = 1
    while True:
        number +=1
        if  number > 1000:
            break
        print(number)
                        
    number =1000000
    while True:
        number -=1
        if number < 0:
            break
    print("Blast Off")

#for [variable} in range(num,num)
    for i in range(0,1001): #repeat __ times
        print(i)

    for doggie in range(1000000, 0, -1):
        pass
    print("Blastoff!")
     
def guessingnumbergame ():
    print("This is a guessing game. Guess a number from 0 to 100.")
    number = random.randint(0,100) 
    while True:
        guess = int(input("Choose a random number "))
        if guess > number:
            print("Too high")
        elif guess < number:
            print("Too low")
        elif guess == number:
            print("correct")
            break

################# FUNCTIONS #################
#Super Awesome
#Almost all code should be infunctions
#Arguements are info you give the function 
#flexibale
#Reusable
#Do nothing until you run ("execute","Call")
#return exits the function immediately
#A function is a just a name for a se of code

'''
How it is suppose to look
def functionname (arg1, arg2):
    code
    code
    return (information)
'''

def addnumbers():  
    def add(number1, number2):
        result = number1 + number2
        return result
    total = add(34, 43)
    print(total)

    print( add(766666, 87877.3434) )

def localglobalvariable ():
    health = 10 ######Global Variable######
    def fight():
        global health
        health -= 8####Local Variable####
        print(health)
        
    fight()
    fight()
    print(health)
    
def CtoF(centigrade):
    fahrenheit = (9/5 * cent) + 32
    return fahrenheit

cent = int( input("What's the temp (in centigrade)? "))
print( CtoF(cent))
