import pyautogui, time

f=open("lyrics.txt","r") #file named 'lyrics.txt' need to be in the same folder of course
count = 0


print("How many times do you want to reapeat?:")
ttp = input()
trr = int(ttp)

time.sleep(1)


print("How many seconds do I have to wait?")
tmslp = input()
tmslp = int(tmslp)


print(tmslp, "seconds to proceed")

time.sleep(tmslp)


for x in range(trr):
    count += 1
    for word in f:
        time.sleep(1.6)
        pyautogui.typewrite(word)
        pyautogui.press("enter")
    print("Times done:", count)
