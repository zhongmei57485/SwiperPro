from common import utils
from libs import sms



def send_verify_code(phone_num):
    """
    发送验证码逻辑
    :param python_num: 手机号
    :return:
    """
    code = utils.gen_rendom_code(6)

    sms.send_verify_code(phone_num,code)
    return None