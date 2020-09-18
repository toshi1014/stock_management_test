from django.db import models


class Item(models.Model):

    c1 = (                              ## change & add
        ("MISUMI", "MISUMI"),
        ("電気系", "電気系"),
    )

    C1 = models.TextField(choices=c1, null=True)
    C2 = models.CharField(null=True, max_length=30)
    name = models.CharField(null=True, max_length=30)
    image = models.ImageField(upload_to="images/", null=True)
    sum = models.IntegerField(null=True)
    stock = models.IntegerField(default=0)
    using = models.IntegerField(default=0)
    location = models.CharField(null=True, max_length=30)

    user = models.TextField(null=True, default="hoge$#@#$")
    number = models.TextField(null=True, default="hoge$#@#$")
    bo_date = models.TextField(null=True, default="hoge$#@#$")
    re_date = models.TextField(null=True, default="hoge$#@#$")
    back_or_not = models.TextField(null=True, default="hoge$#@#$")


    def __str__(self):
        return self.C1 + " - " + self.C2 + "-" + self.name