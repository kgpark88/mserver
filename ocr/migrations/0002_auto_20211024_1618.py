# Generated by Django 3.2.8 on 2021-10-24 16:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ocr', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='OcrText',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file', models.FileField(upload_to='', verbose_name='OCR 파일명')),
                ('text', models.TextField(blank=True, null=True, verbose_name='OCR 텍스트')),
                ('created', models.DateTimeField(auto_now_add=True, null=True, verbose_name='생성일시')),
                ('modified', models.DateTimeField(auto_now=True, null=True, verbose_name='수정일시')),
            ],
            options={
                'verbose_name': 'OCR 처리 내역',
                'verbose_name_plural': 'OCR 처리 내역',
                'db_table': 'ocr_text',
                'ordering': ['-modified'],
                'managed': True,
            },
        ),
        migrations.DeleteModel(
            name='OcrHist',
        ),
    ]