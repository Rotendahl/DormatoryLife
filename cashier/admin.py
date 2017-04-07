""" Specifies which parts of the cashier models are visible in the admin UI """
from django.contrib import admin
from cashier.models import Room, Transaction

admin.site.site_header = "Østervold 1. sal money"
admin.site.index_title = "Benjamin er sej!"


class RoomAdmin(admin.ModelAdmin):
    """ Specifies how the room model should appear """
    list_filter = ('roomNr',)
    fieldsets = [
        ('Room number', {'fields':('name', 'roomNr', 'nickName')}),
        ('Contact Info', {'fields':('mail', 'tlfNumber')}),
        ('Emergency contacts', {
            'fields':('EmergencyName', 'EmergencyRel', 'EmergencyTlfNumber'),
        }),
    ]
    list_display = ('roomNr', 'name')

admin.site.register(Room, RoomAdmin)


class TransactionAdmin(admin.ModelAdmin):
    """ Specifies how the Transaction model should appear """
    list_filter = ('room__roomNr',)
    fieldsets = [
        ('Transaction', {'fields':('date', 'amount', 'description', 'room', 'refunded')}),

    ]
    list_display = ('room', 'date', 'amount', 'description', 'refunded')

admin.site.register(Transaction, TransactionAdmin)
