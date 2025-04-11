import logging
import sys

# step 1 - set logger object
logger = logging.getLogger(__name__)

# step 2 - instruct handler where messages should go
stream_handler = logging.StreamHandler(sys.stdout)

# step 3 - add stream handler to logger object
logger.addHandler(stream_handler)

# Values of logging levels
print(logging.NOTSET)
print(logging.DEBUG)
print(logging.INFO)
print(logging.WARNING)
print(logging.ERROR)
print(logging.CRITICAL)

# methods to log messages at different levels
logger.debug("This is a DEBUG message!")
logger.log(logging.DEBUG, "This is an DEBUG message!")

#
def division():
  try:
    dividend = float(input("Enter the dividend: "))
    logger.info(dividend)
    divisor = float(input("Enter the divisor: "))
    logger.info(divisor)
  except ValueError:
    logger.log(logging.CRITICAL, "No dividend or divisor value entered!")
    return None
  if divisor == 0:
    logger.log(logging.ERROR, "Attempting to divide by 0!")
    return None
  else:
    return dividend/divisor
result = division()

if result == None:
  logger.info(logging.WARNING, "The result value is None!")