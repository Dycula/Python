from django.db import models
from django.contrib.auth.models import AbstractUser
from stocks.models import Stock

BANK_CHOICES = (
    (0,'ICBC'),
    (1,'BC'),
    (2,'CBC'),
    (3,'ABC'),
    (4,'CCB'),
    (5,'ALIPAY'),
    (6,'WXPAY'),
)

BANK_STATUS_CHOICES = (
    (0,'未激活'),
    (1,'激活'),
    (2,'冻结'),
    (3,'注销'),
)


# Create your models here.
class UserInfo(AbstractUser):
    real_name = models.CharField(verbose_name="真实姓名", max_length=50, null=True)
    uemail = models.EmailField(verbose_name="邮箱")
    uphone = models.CharField(verbose_name="手机号", max_length=14, null=True)
    uidentify = models.CharField(verbose_name="身份证号", max_length=50, null=True)

    def __str__(self):
        return self.username

    class Meta:
        # db_table = "user"
        verbose_name = '用户'
        verbose_name_plural = verbose_name


class BankCard(models.Model):
    bank_name = models.IntegerField(verbose_name="银行名", choices=BANK_CHOICES, default=0)
    bank_No = models.CharField(verbose_name="银行卡号", max_length=50, null=True)
    bank_status = models.IntegerField(verbose_name="卡状态", choices=BANK_STATUS_CHOICES, default=0)
    user = models.ForeignKey(UserInfo)

    def __str__(self):
        return self.user.username

    class Meta:
        verbose_name = "银行卡"
        verbose_name_plural = verbose_name


class Wallet(models.Model):
    money = models.DecimalField(verbose_name="金额", max_digits=8, decimal_places=2)
    pay_pwd = models.CharField(verbose_name="支付密码", max_length=200, null=True)
    frozen_money = models.CharField(verbose_name="冻结资金", max_length=200, null=True)
    user = models.OneToOneField(UserInfo)

    def __str__(self):
        return self.user.username

    class Meta:
        verbose_name = "钱包表"
        verbose_name_plural = verbose_name

class HoldStock(models.Model):
    user = models.ForeignKey(UserInfo)
    stock = models.ForeignKey(Stock)
    hold_stock = models.IntegerField(verbose_name="持有数量")
    frozen_stock = models.IntegerField(verbose_name="冻结")

    def __str__(self):
        return self.user.username

    class Meta:
        verbose_name = "持仓"
        verbose_name_plural = verbose_name