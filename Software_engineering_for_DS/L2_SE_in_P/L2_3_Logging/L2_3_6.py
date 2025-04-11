# Logging to console and file

import logging
import sys

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

file_handler = logging.FileHandler('Codecademy\Software_engineering_for_DS\L2_SE_in_P\L2_3_Logging\output.log')
stream_handler = logging.StreamHandler(sys.stdout)

logger.addHandler(file_handler)
logger.addHandler(stream_handler)


# example
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