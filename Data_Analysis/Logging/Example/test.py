from logger import logging

def add(a,b):
    logging.debug("addition operation performed")
    return a+b

logging.debug("funcion add is called")
add(3,5)
