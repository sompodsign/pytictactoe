import time

# Display the program instructions
print('Press ENTER to beign. Afterward, press Enter to click the stopwatch. press Ctrl-C to exit')
input() # Press Enter to begin
print('Started')
startTime = time.time()
lastTime = startTime
lapNum = 1

# Start tracking the lap times
try:
    while True:
        input()
        lapTime = round(time.time() - lastTime, 2)
        totalTime = round(time.time() - startTime, 2)
        print(f"Lap {lapNum}: {totalTime} ({lapTime})", end='')
        lapNum += 1
        lastTime = time.time() # Reset the last lap time
except KeyboardInterrupt:
    print('\nDone')