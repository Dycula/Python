from django.db import models

AREA_CHOICES = (
    (0,'金融'),
    (1,'IT'),
    (2,'体育'),
    (3,'医药'),
    (4,'教育'),
    (5,'餐饮'),
    (6,'娱乐'),
    (7,'影视'),
    (8,'房地产'),
)


# Create your models here.
class Stock(models.Model):
    sto_No = models.CharField(verbose_name="股票代码", max_length=20, null=True)
    sto_name = models.CharField(verbose_name="股票名称", max_length=50, null=True)
    sto_company = models.CharField(verbose_name="股票公司", max_length=200, null=True)
    sto_area = models.IntegerField(verbose_name="股票领域", choices=AREA_CHOICES, default=0)
    sto_update = models.DateField(verbose_name="上市时间")

    def __str__(self):
        return self.sto_No

    class Meta:
        verbose_name = "股票"
        verbose_name_plural = verbose_name

class ADList(models.Model):
    ad_name = models.CharField(verbose_name="广告名称", max_length=50, null=True)
    ad_url = models.URLField(verbose_name="链接")
    ad_img = models.ImageField(verbose_name="图片", upload_to='img/ad', default='normal.png')
    is_delete = models.BooleanField(verbose_name="是否删除", default=False)

    def __str__(self):
        return self.ad_name

    class Meta:
        verbose_name = "广告"
        verbose_name_plural = verbose_name