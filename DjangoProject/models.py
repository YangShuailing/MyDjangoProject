from django.db import models


class DjangoProject(models.Model):
    username = models.CharField('用户名', max_length=30)
    password = models.CharField('密码', max_length=30)
    email = models.CharField('电子邮件', blank=True)
    desc = models.CharField('描述', max_length=500, blank=True)

    def __unicode__(self):
        return self.username
