from django.db import models

# Create your models here.


class UserMessage(models.Model):
    name = models.CharField(max_length=20, verbose_name=u'用户名')
    email = models.EmailField(verbose_name=u'邮箱')
    address = models.CharField(max_length=100, verbose_name=u'联系地址')
    message = models.TextField(verbose_name="留言信息")

    class Meta:
        verbose_name = u'用户留言信息'