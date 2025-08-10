import logging

#logging configs
logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S',
    handlers=[
        logging.FileHandler("app1.log"), #can also use the filename='app.log',filemode='w'
        logging.StreamHandler()
    ]
)

logger = logging.getLogger("ArithmeticAPP")

def add(a,b):
    result = a+b
    logger.debug(f"adding {a}+{b} = {result}")
    return result

def sub(a,b):
    result = a-b
    logger.debug(f"doing {a}-{b} = {result}")
    return result

def mul(a,b):
    result = a*b
    logger.debug(f"doing {a}*{b} = {result}")
    return result

def div(a,b):
    try:
        result = a/b
        logger.debug(f"dividing {a}/{b} = {result}")
        return result
    except ZeroDivisionError:
        logger.error("zero division error")
        return None

add(10,14)
sub(120,12)
mul(12,23)
div(129,0)