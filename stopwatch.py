import time

start = input("Please enter to start the timer = ")
print("The timer has started...")
begin = time.time()

end_timer = input("Please enter to stop the timer = ")
end = time.time()

elapsed = end - begin
elapsed = int(elapsed)
print("The time elapsed is ", elapsed, "seconds")