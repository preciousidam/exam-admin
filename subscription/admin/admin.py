from django.contrib import admin

from subscription.models import Plan, Subscription

# Register your models here.

@admin.register(Subscription)
class SubscriptionAdmin(admin.ModelAdmin):
    list_display = ['user', 'plan', 'pay_ref', 'active', 'created_at', 'last_modified']

@admin.register(Plan)
class PlanAdmin(admin.ModelAdmin):
    list_display = ['title', 'price', 'duration', 'discount', 'created_at', 'last_modified']