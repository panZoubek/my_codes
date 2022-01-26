import pyautogui, time
f=open("lyrics.txt","r")
count = 0
print("How many times do you want to reapeat?:")
ttp = input()
trr = int(ttp)
time.sleep(1)
print("5 seconds to proceed")
time.sleep(5)
for x in range(trr):
	count += 1
	for word in f:
		time.sleep(1.6)
		pyautogui.typewrite(word)
		pyautogui.press("enter")
	print("Times done:", count)
