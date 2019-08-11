from django.contrib import admin

from .models import Company, Card, Page, Testimony, Contact

admin.site.register(Company)
admin.site.register(Card)
admin.site.register(Testimony)
admin.site.register(Contact)


class PageAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name",)}


admin.site.register(Page)
