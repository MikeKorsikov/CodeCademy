# The Asyncio Module
# allow tasks to be paused and resumed to mimic multitasking

import time
import asyncio

# add async in front of function
async def greeting_with_sleep_async(string):
  s = time.perf_counter()
  print(string)
  # add await
  await asyncio.sleep(2)
  print("says hello!")
  elapsed = time.perf_counter() - s
  print("Asyncio Elapsed Time: " + str(elapsed) + " seconds")

# trigger
loop = asyncio.get_event_loop()
loop.run_until_complete(greeting_with_sleep_async("Codecademy"))


### Multiple Asynchronous Tasks

import time
import asyncio

async def greeting_with_sleep_async(string):
  print(string)
  await asyncio.sleep(2)
  print(string + " says hello!")


async def main_async():
  s = time.perf_counter()
  greetings = [greeting_with_sleep_async('Codecademy'), greeting_with_sleep_async('Chelsea'), greeting_with_sleep_async('Hisham'), greeting_with_sleep_async('Ashley')]
  # your code goes here
  await asyncio.gather(*greetings)

  elapsed = time.perf_counter() - s
  print("Asyncio Elapsed Time: " + str(elapsed) + " seconds")

# save your current event loop to the variable loop
loop = asyncio.get_event_loop()
loop.run_until_complete(main_async())
