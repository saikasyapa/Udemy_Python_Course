import time
from time import perf_counter, timezone

print(time.get_clock_info('time'))
print(time.get_clock_info('perf_counter'))
print(time.get_clock_info('monotonic'))
print(time.get_clock_info('process_time'))

print(time.localtime())
print(time.perf_counter())
print(time.monotonic())
print(time.process_time())
