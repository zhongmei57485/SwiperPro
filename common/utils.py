import random
import re


PHONE_PATTTERN = re.compile(r'^1[3-9]\d{9}$')

def is_phone_num(phone_num):

    # if PHONE_PATTTERN.match(phone_num.strip()):
    #     return True
    #
    # else:
    #     return False

    #三目表达式
    return True if PHONE_PATTTERN.match(phone_num.strip()) else False


def gen_rendom_code(length=4):

    if not isinstance(length,int):
        length = 1

    if length <= 0:
        length = 1

    code = random.randrange(10 ** (length-1),10 ** (length))
    return str(code)