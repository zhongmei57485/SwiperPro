import os
import time

from django.core.cache import cache
from django.http import JsonResponse
from django.shortcuts import render,HttpResponse

from common.utils import is_phone_num
from common import errors, cache_keys
from demo import settings
from libs.http import render_json
from user import logics
from user.froms import ProfileForm
from user.models import User


def verify_phone(request):
    """
    #1.验证手机格式
    #2.生成验证码
    #3.保存验证码
    #4.发送验证码

    :param request:
    :return:
    """

    phone_num = request.POST.get('phone_num')

    if is_phone_num(phone_num):
        # 生成验证码
        # 发送验证码
        if logics.send_verify_code(phone_num):
            return render_json()
        else:

            return render_json(code=errors.SMS_SEND_ERR)
    else:
        return render_json(code = errors.PHONE_NUM_ERR)


def login(request):
    """
    登录或注册接口
    如果手机号已经存在，则登录，否则注册
    #1、检测验证码是否正确
    #2、注册或登录
    :param request:
    :return:
    """


    phone_num = request.POST.get('phone_num','')
    code = request.POST.get('code','')

    phone_num = phone_num.strip()
    code=code.strip()

    cached_code = cache.get(cache_keys.VERIFY_CODE_KEY_PREFIX.format(phone_num))
    if cached_code != code:
        return render_json(code=errors.VERIFY_CODE_ERR)

    # try:
    #     user = User.objects.get(pk=1)
    # except User.DoesNotExist:
    #     user = User.objects.create()


    #如果存在记录，则get，否则 create
    user,created = User.objects.get_or_create(phonenum=phone_num)

    #设置登录状态
    request.session['uid'] = user.id


    # token = user.get_or_create_token()
    # data = {'token':token}
    # return render_json(data=data)

    return render_json(data=user.to_dict())



def get_profile(request):

    user = request.user

    return render_json(data=user.profile.to_dict(exclude=['auto_play']))


def set_profile(request):

    user = request.user
    form = ProfileForm(data=request.POST,instance=user.profile)

    if form.is_valid():
        form.save()
        return render_json()

    else:

        return render_json(data=form.errors)



# def upload_avatar(request):
#
#     user = request.user
#
#     avatar = request.FILES.get('avatar')
#
#     file_name = 'avatar-{}'.format(int(time.time()))
#     #
#     # file_path = os.path.join(settings.MEDIA_BOOT,file_name)
#     # with open(file_path,'wb+') as destination:
#     #     for chunk in avatar.chunks():
#     #         destination.write(chunk)
#
#     file_path = logics.upload_avatar(file_name,avatar)
#
#     ret = logics.upload_qiniuyun(file_name,file_path)
#
#     if ret:
#         return render_json()
#
#     else:
#
#         return render_json(code=errors.QINIUYUN_UPLOAD_ERR)


def upload_avatar(request):
    user = request.user
    avatar = request.FILES.get('avatar')

    # file_name = 'avatar-{}'.format(int(time.time()))
    #
    # # 1、先将文件上传到本地服务器
    #
    # # file_path = os.path.join(settings.MEDIA_ROOT, file_name)
    # #
    # # with open(file_path, 'wb+') as destination:
    # #     for chunk in avatar.chunks():
    # #         destination.write(chunk)
    #
    # file_path = logics.upload_avatar(file_name, avatar)
    #
    # # 2、将本地文件上传到七牛云
    # ret = logics.upload_qiniuyun(file_name, file_path)
    #
    # if ret:
    #     return render_json()
    # else:
    #     return render_json(code=errors.AVATAR_UPLOAD_ERR)

    logics.async_upload_avatar.delay(user, avatar)

    return render_json()