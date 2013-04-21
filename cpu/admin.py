from django.contrib import admin
from cpu.models import Cpu

class CpuAdmin(admin.ModelAdmin):
    pass

admin.site.register(Cpu, CpuAdmin)