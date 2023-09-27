from django.contrib import admin
from .models import Meetup, Address, People


@admin.register(Meetup)
class MeetupAdmin(admin.ModelAdmin):
    prepopulated_fields = {
        "slug": ["title"],
    }


admin.site.register(Address)
admin.site.register(People)
