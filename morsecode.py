import random, time

timer = time.time()

def reception():
    print("----> You can get out using CTRL + C or typing end... Idk why you entered this place.")

    time.sleep(1)

    print("\n\n--> Hi stranger or someone... What you do you want to do here?")
    time.sleep(4)

    print("\n\n--> You can do only something with morse code :/")
    time.sleep(3)

    print("\n\n--> I am sure you will choose...")
reception()

the_first_fucking_input = input("\n==> ")

class Morse:
    def __init__(self, p, m):
        self.p = p
        self.m = m #morselist.m = morse code symblos and morselist.p = letter/pismeno

morselist = [Morse("a",".-"),Morse("b","-..."),Morse("c","-.-."),Morse("d","-.."),Morse("e","."),Morse("f","..-."),Morse("g","--."),Morse("h","...."),Morse("i",".."),Morse("j",".---"),Morse("k","-.-"),Morse("l",".-.."),Morse("m","--"),Morse("n","-."),Morse("o","---"),Morse("p",".--."),Morse("q","--.-"),Morse("r",".-."),Morse("s","..."),Morse("t","-"),Morse("u","..-"),Morse("v","...-"),Morse("w",".--"),Morse("x","-..-"),Morse("y","-.--"),Morse("z","--..")]


if the_first_fucking_input == "end":
    print("You are about to left. Your decision. Bye...")
    print("You spent here: ",time.time() - timer,"seconds...")
    exit(0)

if the_first_fucking_input == "practice":

    correct_score = 0
    incorrect_score = 0

    while True:
        i = random.randrange(0,len(morselist))
        ms = morselist[i]
        input_msg = "--> "+ str(ms.m) + "\n==> "
        input_symbol = input(str(input_msg))

        if input_symbol == "end":
            print("\n--> You ended it.","\n--> You have done correct",correct_score,"letters and",incorrect_score,"incorrect")
            break

        if input_symbol == ms.p:
            print("--> correct\n")
            correct_score += 1

        if input_symbol != ms.p:
            print("--> incorrect... it was: ",ms.p,"\n")
            incorrect_score += 1
