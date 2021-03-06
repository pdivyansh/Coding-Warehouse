from django.contrib import admin
from . models import Team,Register,Contact
from django.utils.html import format_html
# Register your models here.
class TeamAdmin(admin.ModelAdmin):
    def thumbnail(self,object):
        return format_html('<img src="{}" width="40" style="border-radius:10px;"/>'.format(object.photo.url))
    thumbnail.short_description = 'photo'

    list_display=('id','thumbnail','name','designation','created_date')
    list_display_links=('id','name','designation')
    search_fields=('name','designation')
    list_filter=('designation',)





admin.site.register(Team,TeamAdmin)

admin.site.register(Register)
admin.site.register(Contact)