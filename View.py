import logger
import Model


def division_be_zero():
    print("Деление на ноль!")
    logger.logger("Деление на ноль!")
    exit()

def printResult():
    print(f'{Model.string} = {Model.result}')