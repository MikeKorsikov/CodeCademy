# The Multiprocessing Module

import time
import multiprocessing

def greeting_with_sleep(string):
  s = time.perf_counter()
  print(string)
  time.sleep(2)
  print("says hello!")
  elapsed = time.perf_counter() - s
  print("Multiprocessing Elapsed Time: " + str(elapsed) + " seconds")

p = multiprocessing.Process(target=greeting_with_sleep, args=("Codecademy",))

p.start()

### Using Multiple Processes

import time
import multiprocessing

def greeting_with_sleep(string):
  print(string)
  time.sleep(2)
  print(string + " says hello!")


def main_multiprocessing():
  s = time.perf_counter()
  processes = []
  greetings = ['Codecademy', 'Chelsea', 'Hisham', 'Ashley']
  # add your code here
  for i in range(len(greetings)):
    p = multiprocessing.Process(target=greeting_with_sleep, args=(greetings[i],))
    processes.append(p)
    p.start()

    for p in processes:
      p.join()

  elapsed = time.perf_counter() - s
  print("Multiprocessing Elapsed Time: " + str(elapsed) + " seconds")

main_multiprocessing()
