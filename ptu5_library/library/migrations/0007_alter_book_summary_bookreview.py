# Generated by Django 4.1.3 on 2022-11-17 10:05

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('library', '0006_bookinstance_reader'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='summary',
            field=tinymce.models.HTMLField(verbose_name='summary'),
        ),
        migrations.CreateModel(
            name='BookReview',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='created at')),
                ('content', models.TextField(max_length=10000, verbose_name='content')),
                ('book', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='reviews', to='library.book', verbose_name='book')),
                ('reader', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='book_reviews', to=settings.AUTH_USER_MODEL, verbose_name='reader')),
            ],
        ),
    ]
