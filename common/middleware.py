from django.utils.deprecation import MiddlewareMixin

from common import errors
from common.errors import LogicException, LogicError
from libs.http import render_json
from user.models import User



class AuthMiddleware(MiddlewareMixin):

    def process_request(self,request):
        """
        自定义认证中间件
        白名单
        request.path
        根据request.session['uid']来判断登录状态

        :param request:
        :return:
        """
        WHITE_LIST =[
            '/apis/user/verify-phone',
            '/apis/user/login',
        ]

        if request.path in WHITE_LIST:
            return

        uid = request.session.get('uid')

        if not uid:
            return render_json(code=errors.LOGIN_REQUIRED_ERR)


        request.user = User.objects.get(pk=uid)

        #
        # token = request.META.get('X-SWIPER-AUTH-TOKEN')
        # if not token:
        #     return render_json(code=errors.LOGIN_REQUIRED_ERR)


class LogicExceptionMiddleware(MiddlewareMixin):

    def process_exception(self,request,exception):
        if isinstance(exception, (LogicException, LogicError)):
            return render_json(code=exception.code)