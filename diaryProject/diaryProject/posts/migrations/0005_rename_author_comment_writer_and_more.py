# Generated by Django 4.2.3 on 2023-07-06 18:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("posts", "0004_remove_comment_article_comment_author_post_author"),
    ]

    operations = [
        migrations.RenameField(
            model_name="comment",
            old_name="author",
            new_name="writer",
        ),
        migrations.RenameField(
            model_name="post",
            old_name="author",
            new_name="writer",
        ),
        migrations.RemoveField(
            model_name="comment",
            name="date",
        ),
        migrations.RemoveField(
            model_name="comment",
            name="photo",
        ),
    ]
