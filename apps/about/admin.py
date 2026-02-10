from django.contrib import admin
from apps.about.models import About, Employee, SocialLink


class SocialLinkInline(admin.TabularInline):
    model = SocialLink
    extra = 1


@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ['fullname', 'position']
    inlines = [SocialLinkInline]
    prepopulated_fields = {'slug':['fullname']}

admin.site.register(About)
# Register your models here.
