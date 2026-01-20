import random
import time
import os
import sys

time.sleep(0.2)
class Dialogue:

    @staticmethod
    def print(string: str, speed=1, end= "\n"):
        for letter in string:
            print(letter, end="")
            sys.stdout.flush()

            if letter in Dialogue.pauses:
                time.sleep(Dialogue.pauses[letter])
            else:
                time.sleep(0.1/speed)
        print("", end=end)
        time.sleep(0.5/speed)

    pauses = {
        "!" : 0.8,
        "." : 0.8,
        "?" : 0.8,
        "," : 0.2,
        " " : 0.18
    }

Dialogue.print("Hi! Just another day in paradise, huh...")
Dialogue.print("Let's get this over with, alright?")

files = os.listdir("ge_cz_wordlist")

for i, file in enumerate(files):
    print(f"[{i}] {file}")


Dialogue.print("Which one will it be? ", 1.3)
index = input()
try:
    index = int(index)
    if 0 > index < len(files):
        raise Exception()
except:
    Dialogue.print("Just, give me the index, please. ", 1.05)
    index = input()

    try:
        index = int(index)
        if 0 > index < len(files):
            raise Exception()
    except:
        Dialogue.print("...", 0.9)
        Dialogue.print("Fuck you", 1.5)
        exit()

Dialogue.print("That one huh.")
Dialogue.print("G o o d  l u c k")
time.sleep(0.2)
os.system("cls")
wordpool = []
with open(f"ge_cz_wordlist/{files[index]}", "r", encoding="utf-8") as f:
    wordpool = [word.split('; ')[::-1] for word in f.read().split('\n')]


czech2germ = True
correct = 0
wrong = 0
groupsize = 5
remaining = 0
last_message = ""
while wordpool:
    random.shuffle(wordpool)
    groups = [wordpool[i:i+groupsize] for i in range(0, len(wordpool), groupsize)]
    remaining = len(wordpool)
    correct = 0
    wrong = 0
    wordpool = []
    last_message = ""
    for group in groups:
        while group:
            word = group.pop()
            if(czech2germ):
                expected_answer = word[0]
                question = word[1]
            else:
                expected_answer = word[1]
                question = word[0]
            print("\n"*100)
            print(f"|{'='*round((40*correct)//remaining)}{' '*(40-round((40*correct)//remaining))}|({correct}/{remaining})")
            print(last_message)
            given_answer = input(question+" : ")
            last_message = ""
            last_message += question+" : "+given_answer+"\n"
            if(expected_answer == given_answer):
                correct += 1
                last_message+= "CORRECT!"
                print("CORRECT!")
            else:
                last_message += f"WRONG! : {expected_answer}"
                print(f"WRONG! : {expected_answer}") 
                wrong += 1
                wordpool.append(word)
                #remaining += 1
                group.insert(0, word)
