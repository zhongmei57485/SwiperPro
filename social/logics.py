import time

from django.core.cache import cache
from django.test import TestCase
import datetime

from common import cache_keys, errors, config
from social.models import Swiped, Friend
from user.models import User


def recommend_users(user):

    today = datetime.date.today()
    max_year = today.year - user.profile.min_dating_age
    min_year = today.year - user.profile.max_dating_age
    swiped_users = Swiped.objects.filter(uid=user.id).only('sid')
    print(swiped_users.query)
    swiped_sid_list = [s.sid for s in swiped_users]

    rec_users = User.objects.filter(
        location = user.profile.location,
        sex=user.profile.dating_sex,
        birth_day__gte=min_year,
        birth_day__lte=max_year

    ).exclude(id__in = swiped_sid_list)[:20]

    print(rec_users.query)


def like_someone(uid,sid):
    """
    喜欢操作，如果被滑动人，喜欢当前用户，则建立好友关系
    :param uid:
    :param sid:
    :return:
    """

    ret = Swiped.swipe(uid=uid,sid=sid,mark='like')
    if ret and Swiped.is_like(sid,uid):
        _,created = Friend.make_friends(sid,uid)
        #发送 匹配好友成功的 推送消息
        return created
    else:
        return False



def superlike_someone(uid,sid):

    """
    超级喜欢操作，如果被滑动人，喜欢当前用户，则建立好友关系
    :param uid:
    :param sid:
    :return:
    """
    ret = Swiped.swipe(uid=uid, sid=sid, mark='superlike')
    if ret and Swiped.is_like(sid, uid):
        # Friend.make_friends(sid, uid)
        Friend.objects.create(sid, uid)


def dislike_someone(uid,sid):
    Swiped.swipe(uid=uid, sid=sid, mark='dislike')
    if Swiped.is_like(sid, uid):
        # Friend.make_friends(sid, uid)
        Friend.objects.create(sid, uid)


def rewind(user):
    """
    撤销上一次滑动操作记录
    撤销上一次创建的好友关系
    :param user:
    :return:
    """

    key = cache_keys.SWIPE_LIMIT_PREFIX.format(user.id)
    swipe_times = cache.get(key,0)

    if swipe_times >= config.SWIPE_LIMIT:
        raise errors.SwipeLimitError

    swipe = Swiped.objects.filter(uid=user.id).latest('created_at')

    if swipe.mark in ['lke','superlike']:
        Friend.cancel_friends(swipe.uid,swipe.sid)


    swipe.delete()

    now = datetime.datetime.now()

    timeout = (24*60*60) - now.hour*3600 - now.minute*60 -now.second

    # n = int(time.time())
    # timeout = 86400 - (n+ 8*3600) % 86400

    cache.set(key,swipe_times + 1,timetout = timeout)


def like_me(user):
    """
    查看喜欢过的人，过滤掉已经存在的好友
    :param user:
    :return:
    """

    friend_list = Friend.friend_list(user.id)

    swipe_list = Swiped.objects.filter(sid=user.id,mark__in=['like','superlike']).\
        exclude(uid__in = friend_list).only('uid')

    like_me_uid_list = [ s.uid for s in swipe_list]




    return like_me_uid_list