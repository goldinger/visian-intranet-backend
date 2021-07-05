from rest_framework import serializers
from app.models import *


class PersonSerializer(serializers.ModelSerializer):
    profile_picture = serializers.SerializerMethodField()
    first_name = serializers.SerializerMethodField()
    last_name = serializers.SerializerMethodField()
    email = serializers.SerializerMethodField()

    class Meta:
        model = Person
        fields = 'id', 'first_name', 'last_name', 'email', 'phone_number', 'profile_picture', 'hiring_date', 'birthday'

    def get_profile_picture(self, obj: Person):
        if obj.profile_picture:
            return obj.profile_picture.name
        return "profile_pictures/no-pic.jpg"

    def get_first_name(self, obj: Person):
        return obj.user.first_name

    def get_last_name(self, obj: Person):
        return obj.user.last_name

    def get_email(self, obj: Person):
        return obj.user.email
