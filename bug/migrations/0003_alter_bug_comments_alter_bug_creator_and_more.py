# Generated by Django 4.2.2 on 2023-07-01 19:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('bug', '0002_profile'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bug',
            name='comments',
            field=models.ManyToManyField(related_name='bug_comments', through='bug.BugComment', to='bug.profile'),
        ),
        migrations.AlterField(
            model_name='bug',
            name='creator',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bug.profile'),
        ),
        migrations.AlterField(
            model_name='bug',
            name='primary_owner',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='created_bugs', to='bug.profile'),
        ),
        migrations.AlterField(
            model_name='bug',
            name='secondary_owner',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='assigned_bugs', to='bug.profile'),
        ),
        migrations.AlterField(
            model_name='bugcomment',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bug.profile'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='bugs_assigned',
            field=models.ManyToManyField(related_name='bugs_todo', to='bug.bug'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='projects',
            field=models.ManyToManyField(related_name='projects_todo', to='bug.project'),
        ),
        migrations.AlterField(
            model_name='project',
            name='bugs',
            field=models.ManyToManyField(related_name='project_bugs', to='bug.bug'),
        ),
        migrations.AlterField(
            model_name='project',
            name='comments',
            field=models.ManyToManyField(related_name='project_comments', through='bug.ProjectComment', to='bug.profile'),
        ),
        migrations.AlterField(
            model_name='project',
            name='creator',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bug.profile'),
        ),
        migrations.AlterField(
            model_name='project',
            name='members',
            field=models.ManyToManyField(related_name='project_members', to='bug.profile'),
        ),
        migrations.AlterField(
            model_name='projectcomment',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bug.profile'),
        ),
    ]