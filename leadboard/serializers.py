from rest_framework import serializers
from .models import Leader

class LeaderSerializer(serializers.ModelSerializer):
	class Meta:
		model = Leader
		fields = ('id', 'first_name','last_name','email', 'gender', 'track', 'language', 'points')
