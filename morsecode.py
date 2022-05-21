import random, time

timer = time.time()

def endend():
    print("--> You are about to left. Your decision. Bye...")

def wholetimer():
    ttrr = time.time() - timer
    print("--> You spent in this program:","%3.2f"%ttrr,"seconds...")

def reception():
    print("\n---=> If you want to go back type 'back' and you can get out using CTRL + C or typing end... Idk why you entered this place.")

    #time.sleep(1)

    print("\n--> Hi stranger or someone... What do you want to do here?")
    #time.sleep(4)

    print("\n--> You can do only something with morse code :/")
    #time.sleep(3)

    print("\n--> I am sure you will choose...")
    #time.sleep(2.5)

    print("\n--> You can practice single letter by typing 'practice'...\n    You can let print all letters and numbers from morse code by typing 'print'...")
    #time.sleep(3)
reception()

back_ff_input = 0


the_first_fucking_input = input("\n\n==> ")

class Morse:
    def __init__(self, p, m):
        self.p = p
        self.m = m #morselist.m = morse code symblos and morselist.p = letter/pismeno

morselist = [Morse("a",".-"),Morse("b","-..."),Morse("c","-.-."),Morse("d","-.."),Morse("e","."),Morse("f","..-."),Morse("g","--."),Morse("h","...."),Morse("i",".."),Morse("j",".---"),Morse("k","-.-"),Morse("l",".-.."),Morse("m","--"),Morse("n","-."),Morse("o","---"),Morse("p",".--."),Morse("q","--.-"),Morse("r",".-."),Morse("s","..."),Morse("t","-"),Morse("u","..-"),Morse("v","...-"),Morse("w",".--"),Morse("x","-..-"),Morse("y","-.--"),Morse("z","--..")]
morsenumbers = [Morse("1",".----"),Morse("2","..---"),Morse("3","...--"),Morse("4","....-"),Morse("5","....."),Morse("6","-...."),Morse("7","--..."),Morse("8","---.."),Morse("9","----."),Morse("0","-----"),]

while True:

    if back_ff_input == 1:
        print("---=> You can get out using CTRL + C or typing end... If you later want to go back you can type 'back'...")
        print("\n\n--> You can practice single letter by typing 'practice'...\n    You can let print all letters and numbers from morse code by typing 'print'...")
        the_first_fucking_input = input("\n\n==> ")
        back_ff_input = 0

    if the_first_fucking_input == "end":
        endend()
        wholetimer()
        exit(0)



    if the_first_fucking_input == "practice":
        print("\n\n")
        print("--> If you want to get morse code and type what letter it is type 'letter' and if you want to get letter and type morse type 'morse'.")
        practice_input = input("\n==> ")
        print("\n\n")
        correct_score = 0
        incorrect_score = 0
        special_timer = time.time()
        rtd = 0
        rtd_total = 0
        response_time = 0

        responce_time_diametr = 0
        def response_time_and_diametr_calc():
            global rtd, rtd_total, response_time
            rtd = rtd + 1
            rtd_total = rtd_total + response_time
            response_time = time.time() - input_time

        while True:
            i = random.randrange(0,len(morselist))
            ms = morselist[i]

            if practice_input == "end":
                endend()
                wholetimer()
                exit(0)

            if practice_input == "back":
                print("\n\n--> You went back")
                back_ff_input = 1
                break

            if practice_input == "letter":
                what_student_type = ms.p
                what_student_get = ms.m

            elif practice_input == "morse":
                what_student_get = ms.p
                what_student_type = ms.m

            else:
                print("\n---=> This command doesn't exist or is unvalid here. Try again :]")
                back_ff_input = 1

            input_msg = "--> "+ str(what_student_get) + "\n==> "
            input_time = time.time()
            input_symbol = input(str(input_msg))
            rrr = time.time() - special_timer

            if input_symbol == "end":
                print("\n--> You have ended it.","\n--> You have done correct",correct_score,"letters and",incorrect_score,"incorrect")
                if responce_time_diametr > 0:
                    print("--> Your avarage response time was:","%3.2f"%responce_time_diametr)
                print("--> You were practicing:","%3.2f"%rrr,"seconds")
                wholetimer()
                exit(0)

            if input_symbol == "back":
                print("\n--> You ended it.","\n--> You have done correct",correct_score,"letters and",incorrect_score,"incorrect")
                if responce_time_diametr > 0:
                    print("--> Your avarage response time was:","%3.2f"%responce_time_diametr)
                print("--> You were practicing:","%3.2f"%rrr,"seconds")
                print("\n--> You went back.")
                back_ff_input = 1
                break

            if input_symbol == what_student_type:
                response_time_and_diametr_calc()
                print("--> correct\n")
                print("--> Your responce time was:","%3.2f"%response_time)
                correct_score += 1

            if input_symbol != what_student_type:
                response_time_and_diametr_calc()
                print("--> incorrect... it was: ",what_student_type,"\n")
                print("--> Your responce time was:","%3.2f"%response_time)
                incorrect_score += 1

            


            responce_time_diametr = rtd_total / rtd



    if the_first_fucking_input == "print":
        print("")
        for xx in range(len(morselist)):
            print(morselist[xx].p,morselist[xx].m)
        print("")
        for uu in range(len(morsenumbers)):
            print(morsenumbers[uu].p,morsenumbers[uu].m)
        back_ff_input = 1




    else:
        print("\n---=> This command doesn't exist or is unvalid here. Try again :]")
        back_ff_input = 1

