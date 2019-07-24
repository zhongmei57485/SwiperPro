from django.http import JsonResponse
from common import errors
from demo import settings


def render_json(code=errors.OK,data =None):
    """
    json返回格式
    :param code: 错误码
    :param data: 接口数据
    :return:
    """

    result = {
        'code':code
    }

    if data:
        result['data'] = data

    if settings.DEBUG:
        json_dumps_parms = {
            'ensure_ascii': False,
            'indent':4
        }

    else:

        json_dumps_parms = {
            'separators':(',',':')
        }


    return  JsonResponse(data=result,json_dumps_params=json_dumps_parms)

