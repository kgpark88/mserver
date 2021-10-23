from import_export.admin import ImportExportModelAdmin
from django.contrib import admin

from ocr.models import OcrHist

@admin.register(OcrHist)
class OcrHistAdmin(ImportExportModelAdmin):
    list_display = [field.name for field in OcrHist._meta.fields]   
    search_fields = ['ocr_text']
