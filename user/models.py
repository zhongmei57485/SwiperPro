from django.db import models

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


    SEXS =(
        (0, '未知'),
        (1,'男'),
        (2, '女')
    )

    LOCATIONS = (
        ('gz','广州'),
        ('sz','深圳'),
        ('bj','北京'),
        ('sh','上海'),
        ('hz','杭州'),
        ('cd','成都')

    )


    phonenum = models.CharField(max_length=11,unique=True)
    nickname = models.CharField(max_length=32)
    sex = models.IntegerField(choices=SEXS,default=0)
    birth_year = models.IntegerField(default=2000)
    birth_month = models.IntegerField(default=1)
    birth_day = models.IntegerField(default=1)
    avatar = models.CharField(max_length=256)
    location = models.CharField(max_length=16,choices=LOCATIONS,default='gz')


    class Meta:
        db_table = 'users'