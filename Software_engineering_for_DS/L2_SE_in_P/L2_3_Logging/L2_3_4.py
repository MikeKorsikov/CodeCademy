import logging
import sys

# step 1 - set logger object
logger = logging.getLogger(__name__)

# step 2 - instruct handler where messages should go
stream_handler = logging.StreamHandler(sys.stdout)

# step 3 - add stream handler to logger object
logger.addHandler(stream_handler)

# step 4 - set the logging level (e.g. DEBUG)
logger.setLevel(logging.DEBUG)

#
def division():
  logger.debug("Starting Division!")
  try:
    dividend = float(input("Enter the dividend: "))
    logger.info(dividend)
    divisor = float(input("Enter the divisor: "))
    logger.info(divisor)
  except SyntaxError:
    logger.log(logging.CRITICAL, "No dividend or divisor value entered!")
    return
  if divisor == 0:
    logger.error("Attempting to divide by 0!")
    return
  else:
      return dividend/divisor
result = division()
if result == None:
  logger.warning("The result value is None!")