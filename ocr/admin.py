from import_export.admin import ImportExportModelAdmin
from django.contrib import admin

from ocr.models import OcrText

@admin.register(OcrText)
class OcrTextAdmin(ImportExportModelAdmin):
    list_display = [field.name for field in OcrText._meta.fields]   
    search_fields = ['text']
