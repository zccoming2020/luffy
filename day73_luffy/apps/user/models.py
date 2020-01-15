from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    phone = models.CharField(max_length=11,unique=True)

    # 需要pillow包的支持
    icon = models.ImageField(upload_to='icon',default='icon/default.jpg')  # 文件夹在BASE_DIR下产生

    class Meta:
        db_table = 'luffy_user'
        verbose_name_plural = '用户表'

    def __str__(self):
        return self.username
