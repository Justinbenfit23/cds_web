from rest_framework import serializers
from .models import CMC
#
class CMCSerializer(serializers.ModelSerializer):
    class Meta:
        model = CMC
        fields = ('id','inserted_at', 'name', 'symbol', 'volume_24h', 'volume_change_24h', 'percent_change_1h', 'percent_change_24h','percent_change_7d', 'percent_change_30d', 'percent_change_90d', 'market_cap', 'market_cap_dominance', 'fully_diluted_market_cap')


