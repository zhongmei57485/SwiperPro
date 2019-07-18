from django.core.cache import cache
from django.db import models
import datetime

from libs.orm import ModelToDicMixin

SEXS = (
    (0, '未知'),
    (1, '男'),
    (2, '女')
)

LOCATIONS = (
    ('gz', '广州'),
    ('sz', '深圳'),
    ('bj', '北京'),
    ('sh', '上海'),
    ('hz', '杭州'),
    ('cd', '成都')

)




# Create your models here.
class User(models.Model):

    '''
    phonenum ⼿机号
    nickname 昵称
    sex 性别
    birth_year 出⽣年
    birth_month 出⽣⽉
    birth_day 出⽣⽇
    avatar 个⼈形象
    location 常居地
    '''





    phonenum = models.CharField(max_length=11,unique=True)
    nickname = models.CharField(max_length=32)
    sex = models.IntegerField(choices=SEXS,default=0)
    birth_year = models.IntegerField(default=2000)
    birth_month = models.IntegerField(default=1)
    birth_day = models.IntegerField(default=1)
    avatar = models.CharField(max_length=256)
    location = models.CharField(max_length=16,choices=LOCATIONS,default='gz')

    @property
    def age(self):
        today = datetime.date.today()
        year = self.birth_year
        mon = self.birth_month
        day = self.birth_day
        birthday = datetime.date(year,mon,day)
        return (today-birthday) // 365

    @property
    def profile(self):

        if not hasattr(self,'_profile'):

            self._profile,_ = Profile.objects.get_or_create(pk=self.id)
        return self._profile


    def to_dict(self):
        return {

            'uid':self.id,
            'phonenum':self.phonenum,
            'nickname':self.nickname,
            'sex':self.sex,
            'avatar':self.avatar,
            'location':self.location,
            'age':self.age

        }

    # def get_or_create_token(self):
    #     '''
    #     为用户生成唯一的token
    #     :return:
    #     '''
    #     key = 'token:{}'.format(self.id)
    #     token = cache.get(key)
    #
    #     if not token:
    #
    #         token = 'token......1234323dsghkjfgedgd'
    #         cache.set(key,token,24*60*60)
    #
    #     return token


    class Meta:
        db_table = 'users'



class Profile(models.Model,ModelToDicMixin):
    """

    location ⽬标城市
    min_distance 最⼩查找范围
    max_distance 最⼤查找范围
    min_dating_age 最⼩交友年龄
    max_dating_age 最⼤交友年龄
    dating_sex 匹配的性别

    auto_play 视频⾃动播放
    """
    location = models.CharField(choices=LOCATIONS,max_length=16,default="gz")
    min_distance = models.IntegerField(default=0)
    max_distance = models.IntegerField(default=10)
    min_dating_age = models.IntegerField(default=18)
    max_dating_age = models.IntegerField(default=81)
    dating_sex = models.IntegerField(default=0,choices=SEXS)
    auto_play = models.BooleanField(default=True)


    class Meta:
        db_table = 'profiles'