from django.contrib import admin
from .models import Store, Ticket


class TicketInline(admin.StackedInline):
    model = Ticket
    extra = 3


class StoreAdmin(admin.ModelAdmin):
    inlines = [TicketInline]


admin.site.register(Store, StoreAdmin)
