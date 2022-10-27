from .models import SlackPerson
from rest_framework import serializers

class SlackPersonSerializer(serializers.ModelSerializer):
    class Meta:
        model = SlackPerson
        fields = ['slackUsername', 'backend', 'age', 'bio']

        