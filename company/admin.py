from django.contrib import admin

from .models import Business, Card, Page

admin.site.register(Business)
admin.site.register(Card)


class PageAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name",)}


admin.site.register(Page)
