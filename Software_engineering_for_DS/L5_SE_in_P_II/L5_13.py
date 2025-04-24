# concurrent programming 

import time
def sequential():
  s = time.perf_counter()
  print("Codecademy")
  time.sleep(2)
  print("says hello!")
  elapsed = time.perf_counter() - s
  print("Sequential Programming Elapsed Time: " + str(elapsed) + " seconds")

sequential()

### The Threading Module
import threading

t = threading.Thread(target=greeting_with_sleep, args=("Codecademy",))
t.start()

### Using Multiple Threads

import time
import threading
def greeting_with_sleep(string):
  print(string)
  time.sleep(2)
  print("says hello!")


def main_threading():
  s = time.perf_counter()
  greetings = ['Codecademy', 'Chelsea', 'Hisham', 'Ashley']
  # your code goes here
  for i in range(len(greetings)):
    # create thread
    t = threading.Thread(target=greeting_with_sleep, args=(greetings[i],))
    t.start()

  elapsed = time.perf_counter() - s
  print("Threading Elapsed Time: " + str(elapsed) + " seconds")


main_threading()

### Joining a Thread

import time
import threading
def greeting_with_sleep(string):
  print(string)
  time.sleep(2)
  print(string + " says hello!")


def main_threading():
  s = time.perf_counter()
  threads = []
  greetings = ['Codecademy', 'Chelsea', 'Hisham', 'Ashley']
  for i in range(len(greetings)):
    t = threading.Thread    (target=greeting_with_sleep, args=(greetings[i],)) 
    t.start()
    # add append code here
    threads.append(t)
  # add join code here
  for t in threads:
    t.join()



  elapsed = time.perf_counter() - s
  print("Threading Elapsed Time: " + str(elapsed) + " seconds")

main_threading()
