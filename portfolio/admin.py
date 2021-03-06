from django.contrib import admin
from .models import Project, DesktopImage


class ProjectDesktopImageInline(admin.TabularInline):
    model = DesktopImage
    extra = 3


class ProjectAdmin(admin.ModelAdmin):
    inlines = [ProjectDesktopImageInline,]


admin.site.register(Project, ProjectAdmin)
