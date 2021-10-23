from django.db import models

class OcrHist(models.Model):
    ocr_file = models.FileField('OCR 파일명')
    ocr_text = models.TextField('OCR 텍스트', blank=True, null=True)
    created = models.DateTimeField('생성일시', auto_now_add=True, blank=True, null=True)
    modified = models.DateTimeField('수정일시', auto_now=True, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'ocr_hist'
        ordering = ['-modified']
        verbose_name = 'OCR 처리 내역'
        verbose_name_plural = 'OCR 처리 내역'

    def __str__(self):
        return "{} {}".format(self.org_file, self.owner)


