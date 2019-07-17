
import requests
from django.conf import settings
from common import config

def send_verify_code(phone,code):

    if settings.DEBUG:

        print("send verify code:", phone, code)
        return True

    parms = config.YZX_SMS_PARAMS.copy()

    parms['mobile'] = phone
    parms['param'] = code



    resp = requests.post(config.YZX_SMS_URL,json=parms)

    if resp.status_code == 200:
        ret = resp.json()
        if ret.get('code') == '000000':
            return  True
        return False

    print()


