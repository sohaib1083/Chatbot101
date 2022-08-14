import json
import random

# opening json file and loading it as dictionary
with open('intents.JSON') as f:
    dict1=  json.load(f)
    dictx= dict1['intents']

# initialising input 
qs='None'

print("Hi, I'm SayabiDev's chatbot. Wanna chat? :) \nPlease type in English language to start a conversation. Type quit to leave ")

# infinite loop 
while True:
    # taking input 
    qs = input()

    # terminating condition 
    if (qs == 'quit'):
        break;
    else:
        print("Human: {}".format(qs)) 

    # searching for possible answer in dictionary    
    for i in dictx:
        if(qs in i['patterns']):
            print("Bot: {}".format(random.choice(i['responses'])))
