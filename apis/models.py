from datetime import datetime
from django.db import models
from django.contrib.auth.models import User
from uuid import uuid4

class CMC(models.Model):
   id = models.UUIDField(primary_key = True,default = uuid4, editable = False)
   inserted_at = models.DateTimeField(default=datetime.utcnow)
   last_updated = models.DateField(default=datetime.utcnow)
   name = models.CharField(max_length=30, default="")
   symbol = models.CharField(max_length=30, default="")
   price = models.FloatField(null=True, default=0.0)
   market_cap = models.BigIntegerField(null=True, default=0.0)
   market_cap_dominance = models.BigIntegerField(null=True, default=0.0)
   fully_diluted_market_cap = models.BigIntegerField(null=True, default=0.0)
   percent_change_1h = models.FloatField(null=True, default=0.0)
   percent_change_24h = models.FloatField(null=True, default=0.0)
   percent_change_30d = models.FloatField(null=True, default=0.0)
   percent_change_60d = models.FloatField(null=True, default=0.0)
   percent_change_7d = models.FloatField(null=True, default=0.0)
   percent_change_90d = models.FloatField(null=True, default=0.0)
   volume_24h = models.FloatField(null=True, default=0.0)
   volume_change_24h = models.FloatField(null=True, default=0.0)

   class Meta:
    unique_together = ('symbol', 'inserted_at',)

   def __str__(self):
        return self.name

