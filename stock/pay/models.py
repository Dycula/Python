from django.db import models
from userinfo.models import UserInfo


PAY_STATUS_CHOICES = (
    (0,'支出'),
    (1,'收入'),
    (2,'充值'),
    (3,'提现'),
)
# Create your models here.
class PayList(models.Model):
    money = models.DecimalField(verbose_name="金额", max_digits=8, decimal_places=2)
    pay_status = models.IntegerField(verbose_name="状态", choices=PAY_STATUS_CHOICES, default=0)
    datetime = models.DateTimeField(verbose_name="时间", auto_now_add=True)
    user = models.ForeignKey(UserInfo)

    def __str__(self):
        return self.user.username

    class Meta:
        verbose_name = '支付记录'
        verbose_name_plural= verbose_name