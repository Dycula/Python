from django.db import models
from stocks.models import Stock
from userinfo.models import UserInfo

ROLE_CHOICES = (
    (0,'买'),
    (1,'卖'),
)

# Create your models here.
class SelfStock(models.Model):
    user = models.ForeignKey(UserInfo)
    stock = models.ForeignKey(Stock)
    is_hold = models.BooleanField(verbose_name="是否持有", default=False)

    def __str__(self):
        return self.user.username

    class Meta:
        verbose_name = "自选股"
        verbose_name_plural = verbose_name

class BOSStock(models.Model):
    user = models.ForeignKey(UserInfo)
    price = models.DecimalField(verbose_name="金额", max_digits=8, decimal_places=2)
    amount = models.IntegerField(verbose_name="数量")
    datetime = models.DateTimeField(verbose_name="挂单时间", auto_now_add=True)
    stock = models.ForeignKey(Stock)
    role = models.IntegerField(verbose_name="买卖角色", choices=ROLE_CHOICES, default=0)

    def __str__(self):
        return self.user.username

    class Meta:
        verbose_name = "挂单表"
        verbose_name_plural = verbose_name

class DealList(models.Model):
    suser = models.ForeignKey(UserInfo, related_name='suser')
    buser = models.ForeignKey(UserInfo, related_name='buser')
    stock = models.ForeignKey(Stock)
    price = models.DecimalField(verbose_name="价格", max_digits=8, decimal_places=2)
    amount = models.IntegerField(verbose_name="数量")
    datetime = models.DateTimeField(verbose_name="交易时间", auto_now_add=True)

    def __str__(self):
        return self.stock.sto_No

    class Meta:
        verbose_name = "交易记录"
        verbose_name_plural = verbose_name