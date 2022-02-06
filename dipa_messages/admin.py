from django.contrib import admin

from .models import MessageModel


class MessageModelAdmin(admin.ModelAdmin):
    fieldsets = [
        ("Sender email", {"fields": ["email"]}),
        ("The message", {"fields": ["message"]}),
    ]

admin.site.register(MessageModel, MessageModelAdmin)
