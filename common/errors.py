"""
业务状态码、错误码
"""

OK = 0



#用户系统   2000-2999

PHONE_NUM_ERR =2001  #手机号码格式错误
SMS_SEND_ERR = 2002   #短信验证码发送失败
VERIFY_CODE_ERR = 2003 #验证码错误
LOGIN_REQUIRED_ERR = 2004 #用户认证错误
