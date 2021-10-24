from django.db import models

class OcrText(models.Model):
    file = models.FileField('이미지 파일')
    text = models.TextField('텍스트 인식결과', blank=True, null=True)
    created = models.DateTimeField('생성일시', auto_now_add=True, blank=True, null=True)
    modified = models.DateTimeField('수정일시', auto_now=True, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'ocr_text'
        ordering = ['-modified']
        verbose_name = '텍스트 인식'
        verbose_name_plural = '텍스트 인식'

    def __str__(self):
        return "{} {}".format(self.org_file, self.owner)


