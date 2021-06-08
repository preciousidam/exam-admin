from rest_framework import serializers

from subscription.models import Plan, Subscription

class PlanSerializer(serializers.ModelSerializer):

    class Meta:
        model=Plan
        fields='__all__'


class SubscriptionSerializer(serializers.ModelSerializer):
    active = serializers.IntegerField(read_only=True)
    class Meta:
        model=Subscription
        fields='__all__'
        extra_kwargs={
            'user': {'read_only': True},
            'plan': {'read_only': True},
            'pay_ref': {'read_only': True},
        }