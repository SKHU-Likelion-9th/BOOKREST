# Generated by Django 3.2.5 on 2021-08-10 09:03

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BookClassInfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=45, verbose_name='책제목')),
                ('image', models.ImageField(blank=True, null=True, upload_to='', verbose_name='책표지')),
                ('author', models.CharField(max_length=45, verbose_name='저자')),
                ('price', models.IntegerField(null=True, verbose_name='가격')),
                ('publisher', models.CharField(max_length=45, verbose_name='출판사')),
                ('pubdate', models.DateField(null=True, verbose_name='출판일')),
                ('stock', models.SmallIntegerField(default=5, verbose_name='재고')),
                ('department', models.CharField(max_length=30, verbose_name='수업개설학과')),
                ('class_name', models.CharField(max_length=30, verbose_name='수업명')),
                ('professor', models.CharField(max_length=30, verbose_name='교수')),
            ],
            options={
                'ordering': ['title'],
            },
        ),
        migrations.CreateModel(
            name='BookWhere',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('book_status', models.CharField(choices=[('보관', '보관'), ('대출', '대출')], max_length=5)),
            ],
        ),
        migrations.CreateModel(
            name='UserBook',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rent_start', models.DateField(verbose_name='대출일')),
                ('rent_end', models.DateField(verbose_name='실제 반납일')),
                ('return_status', models.BooleanField(verbose_name='반납여부')),
                ('return_date', models.DateField(blank=True, null=True, verbose_name='반납일')),
                ('book', models.ManyToManyField(to='category.BookClassInfo')),
            ],
        ),
    ]
