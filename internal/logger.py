import logging

# created a logger to get all logs in terminal and as a log file
logger = logging.getLogger("saitm")
logger.setLevel(logging.INFO)

file_handler = logging.FileHandler("saitm.log", mode='a')
file_handler.setLevel(logging.INFO)

console_handler = logging.StreamHandler()
console_handler.setLevel(logging.INFO)

formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
file_handler.setFormatter(formatter)
console_handler.setFormatter(formatter)

logger.addHandler(file_handler)
logger.addHandler(console_handler)