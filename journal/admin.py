from django.contrib import admin
from .models import Journal


class JournalAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'poster',
        'title',
        'comment',
        'created'
    )


admin.site.register(Journal, JournalAdmin)
