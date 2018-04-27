import webbrowser
import time

# alarm will go every hour for 5 hours total

current_time = time.ctime()
print('The program has started at:',current_time)

breaks = 5
count_breaks = 0

while count_breaks < breaks:
	time.sleep(60*60)
	webbrowser.open("https://www.youtube.com/watch?v=iNpXCzaWW1s")
	count_breaks += 1
