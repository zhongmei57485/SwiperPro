"""
业务状态码、错误码
"""

OK = 0



#用户系统   2000-2999

PHONE_NUM_ERR =2001  #手机号码格式错误
SMS_SEND_ERR = 2002   #短信验证码发送失败
VERIFY_CODE_ERR = 2003 #验证码错误
LOGIN_REQUIRED_ERR = 2004 #用户认证错误
QINIUYUN_UPLOAD_ERR = 2005 #七牛云上传失败

#社交系统
SID_ERR = 3001 #SID参数错误
SWIPE_ERR = 3002 #滑动动作错误


class LogicException(Exception):

    """
    自定义逻辑异常类
    调用者通过参数，传递错误码
    """

    def __init__(self,code):
        self.code = code


class LogicError(Exception):
    code = None


def gen_logic_error(name, code):
    return type(name, (LogicError, ), {'code': code})


# class SwipeError(LogicError):
#     code = 3002


SidError = gen_logic_error('SidError', 3001)
SwipeError = gen_logic_error('SwipeError', 3002)
SwipeLimitError = gen_logic_error('SwipeLimitError', 3003)


#VIP系统
VipPermError = gen_logic_error("VipPermError",4001)


"""
raise LogicException(SWIPE_ERR)
raise SwipeError
"""