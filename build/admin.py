from django.contrib import admin
from .models import *
# Register your models here.
admin.site.register(SoftwareProduct)
# admin.site.register(SoftwareImage)
admin.site.register(RepoSync)
admin.site.register(KernelCompilation)
admin.site.register(BuildCompilation)
admin.site.register(SuperImage)

class KernelCompilationInline(admin.TabularInline):
    model = KernelCompilation
    extra = 1

@admin.register(SoftwareImage)
class SoftwareImageAdmin(admin.ModelAdmin):
    inlines = [KernelCompilationInline]
    list_display = ('name', 'product', 'kernel_compilation_flag')