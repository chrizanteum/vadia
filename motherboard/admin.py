from django.contrib import admin
from motherboard.models import Motherboard, Usb, Socket

class MotherboardAdmin(admin.ModelAdmin):
    filter_horizontal = ('socket',)


class UsbAdmin(admin.ModelAdmin):
    pass


class SocketAdmin(admin.ModelAdmin):
    pass


admin.site.register(Motherboard, MotherboardAdmin)
admin.site.register(Usb, UsbAdmin)
admin.site.register(Socket, SocketAdmin)