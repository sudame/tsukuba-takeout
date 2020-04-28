from django.contrib import admin
from .models import (
    Store,
    Ticket,
    StoreArea,
    StoreGenre,
    StoreOpeningHour,
    StoreTicketHour,
)


class TicketInline(admin.StackedInline):
    model = Ticket
    extra = 3


class TicketHourInline(admin.StackedInline):
    model = StoreTicketHour
    extra = 1


class OpeningHourInline(admin.StackedInline):
    model = StoreOpeningHour
    extra = 1


class StoreAdmin(admin.ModelAdmin):
    inlines = [TicketInline, OpeningHourInline, TicketHourInline]


admin.site.register(Store, StoreAdmin)
admin.site.register(StoreArea)
admin.site.register(StoreGenre)
