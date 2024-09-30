# import time

# print(time.gmtime())
# print(time.localtime())
# print(time.time())
#
# time_here = time.localtime()
# print(time_here)
# print("Year:",time_here[0])
# print("Month:",time_here[1])
# print("Day:",time_here[2])
# print("Date:",time_here[3],'H',':',time_here[4],'M',':',time_here[5],'S.')
#
# ############## OR ############
# print("Year:",time_here.tm_year)
# print("Month:",time_here.tm_mon)
# print("Day:",time_here.tm_mday)
# print("Date:",time_here.tm_hour,'H',':',time_here.tm_min,'M',':',time_here.tm_sec,'S.')

# import time
# from time import time as my_timer, sleep
# import random
#
#
# input("Press enter to start timer")
#
# wait_time = random.randint(1,5)
# time.sleep(wait_time)
# start_time = my_timer()
# input("press enter to stop")
# end_time = my_timer()
#
# print("Start at " + time.strftime("%X",time.localtime(start_time)))
# print('Ended at' + time.strftime("%X", time.localtime(end_time)))
#
# print(f"Your reaction time is {end_time - start_time} ")

################################### OR Need to validate it is not giving precise time seconds varying ##################################
# import time
# from time import time as my_timer, sleep
# import random
#
#
# start_time = (input("Press enter to start timer"), my_timer())[1]
#
# wait_time = random.randint(1,5)
# time.sleep(wait_time)
# # start_time = my_timer()
# end_time = (input("press enter to stop"), my_timer())[1]
# # end_time = my_timer()
#
# print("Start at " + time.strftime("%A, %B %d, %Y",time.localtime(start_time)))
# print('Ended at' + time.strftime("%A, %B %d, %Y", time.localtime(end_time)))
#
# print(f"Your reaction time is {end_time - start_time} ")

###################### To find the precice count we use pert_counter ####################
import time
# from time import time as my_timer
from time import perf_counter as my_timer
# from time import monotonic as my_timer
# from time import process_time as my_timer       ######## based on the CPU it gives the time
import random


input("Press enter to start timer")

wait_time = random.randint(1,5)
time.sleep(wait_time)
start_time = my_timer()
input("press enter to stop")
end_time = my_timer()

print("Start at " + time.strftime("%X",time.localtime(start_time)))
print('Ended at' + time.strftime("%X", time.localtime(end_time)))

print(f"Your reaction time is {end_time - start_time} ")



# In Python, monotonic time refers to a clock that is guaranteed never to move backward. It continuously increases,
#         regardless of system clock adjustments (e.g., if the system time is changed manually or synchronized via NTP).
#           Monotonic time is useful in scenarios where you need to measure elapsed time without worrying about external time changes.
#
# Usage in Python:
# The time.monotonic() function in Python returns the current value of a monotonic clock, expressed in fractional seconds. It’s ideal for measuring time intervals since it avoids issues with the system clock being adjusted.
#
# Key Points:
# Non-decreasing: The value returned by time.monotonic() will always increase or stay the same; it will never decrease.
# Not tied to the system clock: Unlike time.time() (which can be adjusted), monotonic time is independent of the system clock.
# Ideal for timing and benchmarks: Since it’s not affected by clock changes, it’s perfect for measuring the duration between two events

