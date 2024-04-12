from django.contrib import admin
from django.http import HttpRequest

from assignments.models import SocialLink,About

# Register your models here.
class AboutAdmin(admin.ModelAdmin):
    def has_add_permission(self, request):
        count = About.objects.all().count()
        if count == 0:
            return True
        return False
admin.site.register(SocialLink)
admin.site.register(About,AboutAdmin)