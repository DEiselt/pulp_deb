# Generated by Django 4.2.16 on 2024-12-11 16:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('deb', '0006_debrepository'),
    ]

    operations = [
        migrations.CreateModel(
            name='Release',
            fields=[
                ('content_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, related_name='deb_release', serialize=False, to='core.content')),
                ('codename', models.CharField(max_length=255)),
                ('suite', models.CharField(max_length=255)),
                ('distribution', models.CharField(max_length=255)),
            ],
            options={
                'default_related_name': '%(app_label)s_%(model_name)s',
                'unique_together': {('codename', 'suite', 'distribution')},
            },
            bases=('core.content',),
        ),
        migrations.CreateModel(
            name='ReleaseComponent',
            fields=[
                ('content_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, related_name='deb_releasecomponent', serialize=False, to='core.content')),
                ('component', models.CharField(max_length=255)),
                ('release', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='deb_releasecomponent', to='deb.release')),
            ],
            options={
                'default_related_name': '%(app_label)s_%(model_name)s',
                'unique_together': {('component', 'release')},
            },
            bases=('core.content',),
        ),
        migrations.CreateModel(
            name='ReleaseArchitecture',
            fields=[
                ('content_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, related_name='deb_releasearchitecture', serialize=False, to='core.content')),
                ('architecture', models.CharField(max_length=255)),
                ('release', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='deb_releasearchitecture', to='deb.release')),
            ],
            options={
                'default_related_name': '%(app_label)s_%(model_name)s',
                'unique_together': {('architecture', 'release')},
            },
            bases=('core.content',),
        ),
        migrations.CreateModel(
            name='PackageReleaseComponent',
            fields=[
                ('content_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, related_name='deb_packagereleasecomponent', serialize=False, to='core.content')),
                ('package', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='deb_packagereleasecomponent', to='deb.package')),
                ('release_component', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='deb_packagereleasecomponent', to='deb.releasecomponent')),
            ],
            options={
                'default_related_name': '%(app_label)s_%(model_name)s',
                'unique_together': {('package', 'release_component')},
            },
            bases=('core.content',),
        ),
    ]
