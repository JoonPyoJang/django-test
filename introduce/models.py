from django.db import models

# Create your models here.
class AccessLog(models.Model):
    class Meta:
        db_table = "logdata"
    
    created_at = models.DateTimeField("접속시간",auto_now_add = True)
    location = models.CharField("접속경로",max_length=256, default='')

    def __str__(self) -> str:
        return f"{self.created_at}/{self.location}"