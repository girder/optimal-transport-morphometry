from django.contrib import admin

from optimal_transport_morphometry.core.models import Atlas


@admin.register(Atlas)
class AtlasAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']
    list_display_links = ['id', 'name']
    list_filter = ['name']
    list_select_related = True

    search_fields = ['name']

    fields = ['name', 'blob']
