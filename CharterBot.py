# PyChat 2K17

import random
import time

def start():
    pass

def end():
    pass

def confirm(question):
    while True:
        answer = input(question + " (y/n)")
        answer = answer.lower()

        if answer in ["y" , "yes", "yup"]:
            return True
        elif answer in ["n", "no", "nope"]:
            return False
   
def has_keyword(statement, keywords):
    for word in keywords:
        if word in statement:
            return True

    return False

def get_random_response():
    responses = ["I understand",
                 "Mhm",
                 "Well... could you please elaborate?",
                 "I'm sorry, this is out of my field, please press 3 to be connected with another one of our representative."
                 ]

    return random.choice(responses)

def get_random_name():
    responses = ["Vinny",
                 "Danny",
                 "Mark",
                 "Finn",
                 "Noah",
                 "Will",
                 "Desmond",
                 "Bill",
                 "Ajit"]

    return random.choice(responses)

def get_response(statement):
    statement = statement.lower()
    
    service_words = ["phone", "internet", "vision"]
    problem_words = [" not ", "broken", "hate", "isn't"]
    competitor_words = ["at&t", "verizon", "comcast", "dish"]

    if statement == "1":
        response = "We provide the nation's fastest internet, highest quality phone service, and the best selection of channels. Press 3 to get connected to a representative"
    elif statement == "2":
        response = "We're sorry that you are having problems with our products. Please press '3' to be connected with one of our representatives"
    elif statement == "3":
        response = "Hello my name is " + get_random_name() + ". How may I be of service to you?"       

    elif has_keyword(statement, service_words):
        response = "Our products are of optimum quality. Please visit out website charter.com or spectrum.com for more information."
    elif has_keyword(statement, problem_words):
        response = "So sorry to hear that, have you tried turning it off and back on?"
    elif has_keyword(statement, competitor_words):
        response = "Stay with us and we'll add $100 in credit to your account for loyalty."
    else:
        response = get_random_response()

    return response

def play():
    talking = True

    print("""+-+-+-+-+-+-+-+
|C|H|A|R|T|E|R|
+-+-+-+-+-+-+-+""")
    print("Hello! Welcome to Charter customer service. ")
    print("We are always happy to help you with your Charter services or products.")
    print("Please wait for some time while we get you connected")
    time.sleep(1)
    print("*elevator music*")
    time.sleep(10)
    print("Thank you for waiting")
    print("Please press 1 for more information on our services.")
    print("Please press 2 if you have a problem with one of our services.")
    print("Please press 3 to be connected to a representative.")

    while talking:
        statement = input(">> ")

        if statement == "Goodbye":
            talking = False
        else:
            response = get_response(statement)
            print(response)

    print("Goodbye. It was nice talking to you.")

start()

playing = True

while playing:
    play()
    playing = confirm("Would you like to chat again?")

end()
