from rest_framework import serializers
from users.models import UserProfileExample, DiretorProfile

class UserProfileExampleSerializer(serializers.ModelSerializer):

    class Meta:
        model = UserProfileExample
        fields = ['id', 'address', 'phone_number', 'birth_date', 'user']


class DiretorSerializer(serializers.ModelSerializer):

    class Meta:
        model = DiretorProfile
        fields = ['sala', 'departamento', 'user']