import time
import threading
import asyncio
from multiprocessing import Process, Manager


def cal_average(num):  # Average function used for sequential programming, threading, and multiprocessing
  sum_num = 0
  for t in num:
    sum_num = sum_num + t
  avg = sum_num / len(num)
  time.sleep(1)
  return avg

def main_sequential(list1, list2, list3):  # Main wrapper for sequential example
  s = time.perf_counter()
  # Task 2: Calculate each average sequentially
  avg1 = cal_average(list1)
  avg2 = cal_average(list2)
  avg3 = cal_average(list3)

  elapsed = time.perf_counter() - s
  # Task 3: Output results and elapsed time
  print(f"Sequential Programming Averages: {avg1}, {avg2}, {avg3}") #5.5, 6.0, 6.0
  print("Sequential Programming Elapsed Time: {:.2f} seconds".format(elapsed)) # 3.0 sec

async def cal_average_async(num):  # Average function used for asynchronous programming only ( needs await asyncio.sleep() )
  sum_num = 0
  for t in num:
    sum_num = sum_num + t
  avg = sum_num / len(num)
  await asyncio.sleep(1)
  return avg

async def main_async(list1, list2, list3):  # Main wrapper for asynchronous example
  s = time.perf_counter()

  # Task 4: Create async tasks
  tasks = [
    cal_average_async(list1),
    cal_average_async(list2),
    cal_average_async(list3)]

  # Task 5: Run tasks concurrently
  results = await asyncio.gather(*tasks)

  elapsed = time.perf_counter() - s
  # Task 6: Output results and elapsed time
  print(f"Asynchronous Programming Averages: {results[0]}, {results[1]}, {results[2]}") #5.5, 6.0, 6.0
  print("Asynchronous Programming Elapsed Time: {:.2f} seconds".format(elapsed)) # 1.0 sec

# Helper for Task 8a threading
def threading_worker(lst, results, index):
    results[index] = cal_average(lst)

def main_threading(list1, list2, list3):  # Main wrapper for threading example
  s = time.perf_counter()
  
  # Task 7: Create list of lists and threads container
  lists = [list1, list2, list3]
  threads = []
  results = [None] * 3  # Thread-safe for read/write access within threads

  # Task 8a: Create and start threads
  for i in range(len(lists)):
    x = threading.Thread(target=threading_worker, args=(lists[i], results, i))
    threads.append(x)
    x.start()

  # Task 8b: Join threads
  for thread in threads:
    thread.join()

  elapsed = time.perf_counter() - s
  # Task 9: Output results and elapsed time
  print(f"Threading Averages: {results[0]}, {results[1]}, {results[2]}") # 5.5, 6.0, 6.0
  print("Threading Elapsed Time: {:.2f} seconds".format(elapsed)) # 1.0 sec

# Helper for Task 12a multiprocessing
def multiprocessing_worker(lst, results, index):
    avg = cal_average(lst)
    results[index] = avg

def main_multiprocessing(list1, list2, list3):  # Main wrapper for multiprocessing example
  s = time.perf_counter()

  # Task 10: Create list of lists
  lists = [list1, list2, list3]

  # Task 11: Create shared memory list and processes list
  manager = Manager()
  results = manager.list([0] * 3)  # Shared list between processes
  processes = []

  # Task 12a: Create and start processes
  for i in range(len(lists)):
      p = Process(target=multiprocessing_worker, args=(lists[i], results, i))
      processes.append(p)
      p.start()

  # Task 12b: Join processes
  for process in processes:
      process.join()


  elapsed = time.perf_counter() - s
  # Task 13: Output results and elapsed time
  print(f"Multiprocessing Averages: {results[0]}, {results[1]}, {results[2]}") # 5.5, 6.0, 6.0
  print("Multiprocessing Elapsed Time: {:.2f} seconds".format(elapsed)) # 1.02 sec


if __name__ == '__main__':  # Need to use this if-statement so multiprocessing doesn't cause an infinite loop
  l1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
  l2 = [2, 4, 6, 8, 10]
  l3 = [1, 3, 5, 7, 9, 11]

  print("\nSequential:")
  main_sequential(l1, l2, l3)

  print("\nAsynchronous:")
  loop = asyncio.get_event_loop()
  loop.run_until_complete(main_async(l1, l2, l3))
  
  print("\nThreading:")
  main_threading(l1, l2, l3)

  print("\nMultiprocessing:")
  main_multiprocessing(l1, l2, l3)