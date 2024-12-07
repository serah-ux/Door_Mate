from django.contrib.postgres import serializers

from application.models import Appointment


class AppointmentSerializer(serializers.BaseSerializer):
    class Meta:
        model = Appointment
        fields = 'name','gender','date','rate','email','message'