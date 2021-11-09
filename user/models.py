from django.utils import timezone

from django.db import models
from django.contrib.auth.models import AbstractUser

# 创建用户模型类
class BlogUser(AbstractUser):
    nikename = models.CharField('昵称',max_length=20,default='',)  #verbose_name = '昵称'
    class Meta:
        db_table = 'db_user'
        verbose_name = '用户数据模型'
        verbose_name_plural=verbose_name

# 邮箱验证码模型类
class EmailVerifyRecord(models.Model):
    code = models.CharField(max_length=20,verbose_name='验证码')
    email = models.EmailField(max_length=50,verbose_name='邮箱')
    # 下列这种写法多看看
    send_type = models.CharField(choices=(("register","注册"),
                                          ("forget","找回密码"),
                                          ("update_email","修改邮箱")),
                                 max_length=30,verbose_name='验证码类型')
    send_time = models.DateTimeField(default=timezone.now,verbose_name="发送时间")

    class Meta:
        db_table='db_email_verify'
        verbose_name='邮箱验证码'
        verbose_name_plural=verbose_name
    def __str__(self): # 通过format方法直接输出 code(参数)email(参数)--------不够熟悉多去看看
        return '{0}{1}'.format(self.code,self.email)



