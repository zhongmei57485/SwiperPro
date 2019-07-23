from django.db import models



class FriendManager(models.Manager):
    """
    Friend模型，自定义管理器
    """

    def make_friends(self,uid1,uid2):
        uid1, uid2 = (uid1, uid2) if uid1 < uid2 else (uid2, uid1)
        return self.objects.get_or_create(uid1=uid1, uid2=uid2)