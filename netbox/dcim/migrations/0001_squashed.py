import dcim.fields
import ipam.fields
import django.contrib.postgres.fields
from utilities.json import CustomFieldJSONEncoder
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import timezone_field.fields
import utilities.fields
import utilities.ordering
import utilities.query_functions
import utilities.validators


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    replaces = [
        ('dcim', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cable',
            fields=[
                ('created', models.DateField(auto_now_add=True, null=True)),
                ('last_updated', models.DateTimeField(auto_now=True, null=True)),
                ('custom_field_data', models.JSONField(blank=True, default=dict, encoder=CustomFieldJSONEncoder)),
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('termination_a_id', models.PositiveIntegerField()),
                ('termination_b_id', models.PositiveIntegerField()),
                ('type', models.CharField(blank=True, max_length=50)),
                ('status', models.CharField(default='connected', max_length=50)),
                ('label', models.CharField(blank=True, max_length=100)),
                ('color', utilities.fields.ColorField(blank=True, max_length=6)),
                ('length', models.PositiveSmallIntegerField(blank=True, null=True)),
                ('length_unit', models.CharField(blank=True, max_length=50)),
                ('_abs_length', models.DecimalField(blank=True, decimal_places=4, max_digits=10, null=True)),
            ],
            options={
                'ordering': ['pk'],
            },
        ),
        migrations.CreateModel(
            name='CablePath',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('origin_id', models.PositiveIntegerField()),
                ('destination_id', models.PositiveIntegerField(blank=True, null=True)),
                ('path', dcim.fields.PathField(base_field=models.CharField(max_length=40), size=None)),
                ('is_active', models.BooleanField(default=False)),
                ('is_split', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='ConsolePort',
            fields=[
                ('created', models.DateField(auto_now_add=True, null=True)),
                ('last_updated', models.DateTimeField(auto_now=True, null=True)),
                ('custom_field_data', models.JSONField(blank=True, default=dict, encoder=CustomFieldJSONEncoder)),
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=64)),
                (
                    '_name',
                    utilities.fields.NaturalOrderingField(
                        'name', blank=True, max_length=100, naturalize_function=utilities.ordering.naturalize
                    ),
                ),
                ('label', models.CharField(blank=True, max_length=64)),
                ('description', models.CharField(blank=True, max_length=200)),
                ('_cable_peer_id', models.PositiveIntegerField(blank=True, null=True)),
                ('mark_connected', models.BooleanField(default=False)),
                ('type', models.CharField(blank=True, max_length=50)),
                ('speed', models.PositiveSmallIntegerField(blank=True, null=True)),
            ],
            options={
                'ordering': ('device', '_name'),
            },
        ),
        migrations.CreateModel(
            name='ConsolePortTemplate',
            fields=[
                ('created', models.DateField(auto_now_add=True, null=True)),
                ('last_updated', models.DateTimeField(auto_now=True, null=True)),
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=64)),
                (
                    '_name',
                    utilities.fields.NaturalOrderingField(
                        'name', blank=True, max_length=100, naturalize_function=utilities.ordering.naturalize
                    ),
                ),
                ('label', models.CharField(blank=True, max_length=64)),
                ('description', models.CharField(blank=True, max_length=200)),
                ('type', models.CharField(blank=True, max_length=50)),
            ],
            options={
                'ordering': ('device_type', '_name'),
            },
        ),
        migrations.CreateModel(
            name='ConsoleServerPort',
            fields=[
                ('created', models.DateField(auto_now_add=True, null=True)),
                ('last_updated', models.DateTimeField(auto_now=True, null=True)),
                ('custom_field_data', models.JSONField(blank=True, default=dict, encoder=CustomFieldJSONEncoder)),
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=64)),
                (
                    '_name',
                    utilities.fields.NaturalOrderingField(
                        'name', blank=True, max_length=100, naturalize_function=utilities.ordering.naturalize
                    ),
                ),
                ('label', models.CharField(blank=True, max_length=64)),
                ('description', models.CharField(blank=True, max_length=200)),
                ('_cable_peer_id', models.PositiveIntegerField(blank=True, null=True)),
                ('mark_connected', models.BooleanField(default=False)),
                ('type', models.CharField(blank=True, max_length=50)),
                ('speed', models.PositiveSmallIntegerField(blank=True, null=True)),
            ],
            options={
                'ordering': ('device', '_name'),
            },
        ),
        migrations.CreateModel(
            name='ConsoleServerPortTemplate',
            fields=[
                ('created', models.DateField(auto_now_add=True, null=True)),
                ('last_updated', models.DateTimeField(auto_now=True, null=True)),
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=64)),
                (
                    '_name',
                    utilities.fields.NaturalOrderingField(
                        'name', blank=True, max_length=100, naturalize_function=utilities.ordering.naturalize
                    ),
                ),
                ('label', models.CharField(blank=True, max_length=64)),
                ('description', models.CharField(blank=True, max_length=200)),
                ('type', models.CharField(blank=True, max_length=50)),
            ],
            options={
                'ordering': ('device_type', '_name'),
            },
        ),
        migrations.CreateModel(
            name='Device',
            fields=[
                ('created', models.DateField(auto_now_add=True, null=True)),
                ('last_updated', models.DateTimeField(auto_now=True, null=True)),
                ('custom_field_data', models.JSONField(blank=True, default=dict, encoder=CustomFieldJSONEncoder)),
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('local_context_data', models.JSONField(blank=True, null=True)),
                ('name', models.CharField(blank=True, max_length=64, null=True)),
                (
                    '_name',
                    utilities.fields.NaturalOrderingField(
                        'name', blank=True, max_length=100, naturalize_function=utilities.ordering.naturalize, null=True
                    ),
                ),
                ('serial', models.CharField(blank=True, max_length=50)),
                ('asset_tag', models.CharField(blank=True, max_length=50, null=True, unique=True)),
                (
                    'position',
                    models.PositiveSmallIntegerField(
                        blank=True, null=True, validators=[django.core.validators.MinValueValidator(1)]
                    ),
                ),
                ('face', models.CharField(blank=True, max_length=50)),
                ('status', models.CharField(default='active', max_length=50)),
                (
                    'vc_position',
                    models.PositiveSmallIntegerField(
                        blank=True, null=True, validators=[django.core.validators.MaxValueValidator(255)]
                    ),
                ),
                (
                    'vc_priority',
                    models.PositiveSmallIntegerField(
                        blank=True, null=True, validators=[django.core.validators.MaxValueValidator(255)]
                    ),
                ),
                ('comments', models.TextField(blank=True)),
            ],
            options={
                'ordering': ('_name', 'pk'),
            },
        ),
        migrations.CreateModel(
            name='DeviceBay',
            fields=[
                ('created', models.DateField(auto_now_add=True, null=True)),
                ('last_updated', models.DateTimeField(auto_now=True, null=True)),
                ('custom_field_data', models.JSONField(blank=True, default=dict, encoder=CustomFieldJSONEncoder)),
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=64)),
                (
                    '_name',
                    utilities.fields.NaturalOrderingField(
                        'name', blank=True, max_length=100, naturalize_function=utilities.ordering.naturalize
                    ),
                ),
                ('label', models.CharField(blank=True, max_length=64)),
                ('description', models.CharField(blank=True, max_length=200)),
            ],
            options={
                'ordering': ('device', '_name'),
            },
        ),
        migrations.CreateModel(
            name='DeviceBayTemplate',
            fields=[
                ('created', models.DateField(auto_now_add=True, null=True)),
                ('last_updated', models.DateTimeField(auto_now=True, null=True)),
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=64)),
                (
                    '_name',
                    utilities.fields.NaturalOrderingField(
                        'name', blank=True, max_length=100, naturalize_function=utilities.ordering.naturalize
                    ),
                ),
                ('label', models.CharField(blank=True, max_length=64)),
                ('description', models.CharField(blank=True, max_length=200)),
            ],
            options={
                'ordering': ('device_type', '_name'),
            },
        ),
        migrations.CreateModel(
            name='DeviceRole',
            fields=[
                ('created', models.DateField(auto_now_add=True, null=True)),
                ('last_updated', models.DateTimeField(auto_now=True, null=True)),
                ('custom_field_data', models.JSONField(blank=True, default=dict, encoder=CustomFieldJSONEncoder)),
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100, unique=True)),
                ('slug', models.SlugField(max_length=100, unique=True)),
                ('color', utilities.fields.ColorField(default='9e9e9e', max_length=6)),
                ('vm_role', models.BooleanField(default=True)),
                ('description', models.CharField(blank=True, max_length=200)),
            ],
            options={
                'ordering': ('name',),
            },
        ),
        migrations.CreateModel(
            name='DeviceType',
            fields=[
                ('created', models.DateField(auto_now_add=True, null=True)),
                ('last_updated', models.DateTimeField(auto_now=True, null=True)),
                ('custom_field_data', models.JSONField(blank=True, default=dict, encoder=CustomFieldJSONEncoder)),
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('model', models.CharField(max_length=100)),
                ('slug', models.SlugField(max_length=100)),
                ('part_number', models.CharField(blank=True, max_length=50)),
                ('u_height', models.PositiveSmallIntegerField(default=1)),
                ('is_full_depth', models.BooleanField(default=True)),
                ('subdevice_role', models.CharField(blank=True, max_length=50)),
                ('front_image', models.ImageField(blank=True, upload_to='devicetype-images')),
                ('rear_image', models.ImageField(blank=True, upload_to='devicetype-images')),
                ('comments', models.TextField(blank=True)),
            ],
            options={
                'ordering': ['manufacturer', 'model'],
            },
        ),
        migrations.CreateModel(
            name='FrontPort',
            fields=[
                ('created', models.DateField(auto_now_add=True, null=True)),
                ('last_updated', models.DateTimeField(auto_now=True, null=True)),
                ('custom_field_data', models.JSONField(blank=True, default=dict, encoder=CustomFieldJSONEncoder)),
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=64)),
                (
                    '_name',
                    utilities.fields.NaturalOrderingField(
                        'name', blank=True, max_length=100, naturalize_function=utilities.ordering.naturalize
                    ),
                ),
                ('label', models.CharField(blank=True, max_length=64)),
                ('description', models.CharField(blank=True, max_length=200)),
                ('_cable_peer_id', models.PositiveIntegerField(blank=True, null=True)),
                ('mark_connected', models.BooleanField(default=False)),
                ('type', models.CharField(max_length=50)),
                (
                    'rear_port_position',
                    models.PositiveSmallIntegerField(
                        default=1,
                        validators=[
                            django.core.validators.MinValueValidator(1),
                            django.core.validators.MaxValueValidator(1024),
                        ],
                    ),
                ),
            ],
            options={
                'ordering': ('device', '_name'),
            },
        ),
        migrations.CreateModel(
            name='FrontPortTemplate',
            fields=[
                ('created', models.DateField(auto_now_add=True, null=True)),
                ('last_updated', models.DateTimeField(auto_now=True, null=True)),
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=64)),
                (
                    '_name',
                    utilities.fields.NaturalOrderingField(
                        'name', blank=True, max_length=100, naturalize_function=utilities.ordering.naturalize
                    ),
                ),
                ('label', models.CharField(blank=True, max_length=64)),
                ('description', models.CharField(blank=True, max_length=200)),
                ('type', models.CharField(max_length=50)),
                (
                    'rear_port_position',
                    models.PositiveSmallIntegerField(
                        default=1,
                        validators=[
                            django.core.validators.MinValueValidator(1),
                            django.core.validators.MaxValueValidator(1024),
                        ],
                    ),
                ),
            ],
            options={
                'ordering': ('device_type', '_name'),
            },
        ),
        migrations.CreateModel(
            name='Interface',
            fields=[
                ('created', models.DateField(auto_now_add=True, null=True)),
                ('last_updated', models.DateTimeField(auto_now=True, null=True)),
                ('custom_field_data', models.JSONField(blank=True, default=dict, encoder=CustomFieldJSONEncoder)),
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=64)),
                ('label', models.CharField(blank=True, max_length=64)),
                ('description', models.CharField(blank=True, max_length=200)),
                ('_cable_peer_id', models.PositiveIntegerField(blank=True, null=True)),
                ('mark_connected', models.BooleanField(default=False)),
                ('enabled', models.BooleanField(default=True)),
                ('mac_address', dcim.fields.MACAddressField(blank=True, null=True)),
                (
                    'mtu',
                    models.PositiveIntegerField(
                        blank=True,
                        null=True,
                        validators=[
                            django.core.validators.MinValueValidator(1),
                            django.core.validators.MaxValueValidator(65536),
                        ],
                    ),
                ),
                ('mode', models.CharField(blank=True, max_length=50)),
                (
                    '_name',
                    utilities.fields.NaturalOrderingField(
                        'name', blank=True, max_length=100, naturalize_function=utilities.ordering.naturalize_interface
                    ),
                ),
                ('type', models.CharField(max_length=50)),
                ('mgmt_only', models.BooleanField(default=False)),
            ],
            options={
                'ordering': ('device', utilities.query_functions.CollateAsChar('_name')),
            },
        ),
        migrations.CreateModel(
            name='InterfaceTemplate',
            fields=[
                ('created', models.DateField(auto_now_add=True, null=True)),
                ('last_updated', models.DateTimeField(auto_now=True, null=True)),
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=64)),
                ('label', models.CharField(blank=True, max_length=64)),
                ('description', models.CharField(blank=True, max_length=200)),
                (
                    '_name',
                    utilities.fields.NaturalOrderingField(
                        'name', blank=True, max_length=100, naturalize_function=utilities.ordering.naturalize_interface
                    ),
                ),
                ('type', models.CharField(max_length=50)),
                ('mgmt_only', models.BooleanField(default=False)),
            ],
            options={
                'ordering': ('device_type', '_name'),
            },
        ),
        migrations.CreateModel(
            name='InventoryItem',
            fields=[
                ('created', models.DateField(auto_now_add=True, null=True)),
                ('last_updated', models.DateTimeField(auto_now=True, null=True)),
                ('custom_field_data', models.JSONField(blank=True, default=dict, encoder=CustomFieldJSONEncoder)),
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=64)),
                (
                    '_name',
                    utilities.fields.NaturalOrderingField(
                        'name', blank=True, max_length=100, naturalize_function=utilities.ordering.naturalize
                    ),
                ),
                ('label', models.CharField(blank=True, max_length=64)),
                ('description', models.CharField(blank=True, max_length=200)),
                ('part_id', models.CharField(blank=True, max_length=50)),
                ('serial', models.CharField(blank=True, max_length=50)),
                ('asset_tag', models.CharField(blank=True, max_length=50, null=True, unique=True)),
                ('discovered', models.BooleanField(default=False)),
                ('lft', models.PositiveIntegerField(editable=False)),
                ('rght', models.PositiveIntegerField(editable=False)),
                ('tree_id', models.PositiveIntegerField(db_index=True, editable=False)),
                ('level', models.PositiveIntegerField(editable=False)),
            ],
            options={
                'ordering': ('device__id', 'parent__id', '_name'),
            },
        ),
        migrations.CreateModel(
            name='Location',
            fields=[
                ('created', models.DateField(auto_now_add=True, null=True)),
                ('last_updated', models.DateTimeField(auto_now=True, null=True)),
                ('custom_field_data', models.JSONField(blank=True, default=dict, encoder=CustomFieldJSONEncoder)),
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('slug', models.SlugField(max_length=100)),
                ('description', models.CharField(blank=True, max_length=200)),
                ('lft', models.PositiveIntegerField(editable=False)),
                ('rght', models.PositiveIntegerField(editable=False)),
                ('tree_id', models.PositiveIntegerField(db_index=True, editable=False)),
                ('level', models.PositiveIntegerField(editable=False)),
            ],
            options={
                'ordering': ['site', 'name'],
            },
        ),
        migrations.CreateModel(
            name='Manufacturer',
            fields=[
                ('created', models.DateField(auto_now_add=True, null=True)),
                ('last_updated', models.DateTimeField(auto_now=True, null=True)),
                ('custom_field_data', models.JSONField(blank=True, default=dict, encoder=CustomFieldJSONEncoder)),
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100, unique=True)),
                ('slug', models.SlugField(max_length=100, unique=True)),
                ('description', models.CharField(blank=True, max_length=200)),
            ],
            options={
                'ordering': ('name',),
            },
        ),
        migrations.CreateModel(
            name='Platform',
            fields=[
                ('created', models.DateField(auto_now_add=True, null=True)),
                ('last_updated', models.DateTimeField(auto_now=True, null=True)),
                ('custom_field_data', models.JSONField(blank=True, default=dict, encoder=CustomFieldJSONEncoder)),
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100, unique=True)),
                ('slug', models.SlugField(max_length=100, unique=True)),
                ('napalm_driver', models.CharField(blank=True, max_length=50)),
                ('napalm_args', models.JSONField(blank=True, null=True)),
                ('description', models.CharField(blank=True, max_length=200)),
            ],
            options={
                'ordering': ('name',),
            },
        ),
        migrations.CreateModel(
            name='PowerFeed',
            fields=[
                ('created', models.DateField(auto_now_add=True, null=True)),
                ('last_updated', models.DateTimeField(auto_now=True, null=True)),
                ('custom_field_data', models.JSONField(blank=True, default=dict, encoder=CustomFieldJSONEncoder)),
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('_cable_peer_id', models.PositiveIntegerField(blank=True, null=True)),
                ('mark_connected', models.BooleanField(default=False)),
                ('name', models.CharField(max_length=100)),
                ('status', models.CharField(default='active', max_length=50)),
                ('type', models.CharField(default='primary', max_length=50)),
                ('supply', models.CharField(default='ac', max_length=50)),
                ('phase', models.CharField(default='single-phase', max_length=50)),
                ('voltage', models.SmallIntegerField(validators=[utilities.validators.ExclusionValidator([0])])),
                (
                    'amperage',
                    models.PositiveSmallIntegerField(validators=[django.core.validators.MinValueValidator(1)]),
                ),
                (
                    'max_utilization',
                    models.PositiveSmallIntegerField(
                        validators=[
                            django.core.validators.MinValueValidator(1),
                            django.core.validators.MaxValueValidator(100),
                        ]
                    ),
                ),
                ('available_power', models.PositiveIntegerField(default=0, editable=False)),
                ('comments', models.TextField(blank=True)),
            ],
            options={
                'ordering': ['power_panel', 'name'],
            },
        ),
        migrations.CreateModel(
            name='PowerOutlet',
            fields=[
                ('created', models.DateField(auto_now_add=True, null=True)),
                ('last_updated', models.DateTimeField(auto_now=True, null=True)),
                ('custom_field_data', models.JSONField(blank=True, default=dict, encoder=CustomFieldJSONEncoder)),
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=64)),
                (
                    '_name',
                    utilities.fields.NaturalOrderingField(
                        'name', blank=True, max_length=100, naturalize_function=utilities.ordering.naturalize
                    ),
                ),
                ('label', models.CharField(blank=True, max_length=64)),
                ('description', models.CharField(blank=True, max_length=200)),
                ('_cable_peer_id', models.PositiveIntegerField(blank=True, null=True)),
                ('mark_connected', models.BooleanField(default=False)),
                ('type', models.CharField(blank=True, max_length=50)),
                ('feed_leg', models.CharField(blank=True, max_length=50)),
            ],
            options={
                'ordering': ('device', '_name'),
            },
        ),
        migrations.CreateModel(
            name='PowerOutletTemplate',
            fields=[
                ('created', models.DateField(auto_now_add=True, null=True)),
                ('last_updated', models.DateTimeField(auto_now=True, null=True)),
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=64)),
                (
                    '_name',
                    utilities.fields.NaturalOrderingField(
                        'name', blank=True, max_length=100, naturalize_function=utilities.ordering.naturalize
                    ),
                ),
                ('label', models.CharField(blank=True, max_length=64)),
                ('description', models.CharField(blank=True, max_length=200)),
                ('type', models.CharField(blank=True, max_length=50)),
                ('feed_leg', models.CharField(blank=True, max_length=50)),
            ],
            options={
                'ordering': ('device_type', '_name'),
            },
        ),
        migrations.CreateModel(
            name='PowerPanel',
            fields=[
                ('created', models.DateField(auto_now_add=True, null=True)),
                ('last_updated', models.DateTimeField(auto_now=True, null=True)),
                ('custom_field_data', models.JSONField(blank=True, default=dict, encoder=CustomFieldJSONEncoder)),
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
            ],
            options={
                'ordering': ['site', 'name'],
            },
        ),
        migrations.CreateModel(
            name='PowerPort',
            fields=[
                ('created', models.DateField(auto_now_add=True, null=True)),
                ('last_updated', models.DateTimeField(auto_now=True, null=True)),
                ('custom_field_data', models.JSONField(blank=True, default=dict, encoder=CustomFieldJSONEncoder)),
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=64)),
                (
                    '_name',
                    utilities.fields.NaturalOrderingField(
                        'name', blank=True, max_length=100, naturalize_function=utilities.ordering.naturalize
                    ),
                ),
                ('label', models.CharField(blank=True, max_length=64)),
                ('description', models.CharField(blank=True, max_length=200)),
                ('_cable_peer_id', models.PositiveIntegerField(blank=True, null=True)),
                ('mark_connected', models.BooleanField(default=False)),
                ('type', models.CharField(blank=True, max_length=50)),
                (
                    'maximum_draw',
                    models.PositiveSmallIntegerField(
                        blank=True, null=True, validators=[django.core.validators.MinValueValidator(1)]
                    ),
                ),
                (
                    'allocated_draw',
                    models.PositiveSmallIntegerField(
                        blank=True, null=True, validators=[django.core.validators.MinValueValidator(1)]
                    ),
                ),
            ],
            options={
                'ordering': ('device', '_name'),
            },
        ),
        migrations.CreateModel(
            name='PowerPortTemplate',
            fields=[
                ('created', models.DateField(auto_now_add=True, null=True)),
                ('last_updated', models.DateTimeField(auto_now=True, null=True)),
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=64)),
                (
                    '_name',
                    utilities.fields.NaturalOrderingField(
                        'name', blank=True, max_length=100, naturalize_function=utilities.ordering.naturalize
                    ),
                ),
                ('label', models.CharField(blank=True, max_length=64)),
                ('description', models.CharField(blank=True, max_length=200)),
                ('type', models.CharField(blank=True, max_length=50)),
                (
                    'maximum_draw',
                    models.PositiveSmallIntegerField(
                        blank=True, null=True, validators=[django.core.validators.MinValueValidator(1)]
                    ),
                ),
                (
                    'allocated_draw',
                    models.PositiveSmallIntegerField(
                        blank=True, null=True, validators=[django.core.validators.MinValueValidator(1)]
                    ),
                ),
            ],
            options={
                'ordering': ('device_type', '_name'),
            },
        ),
        migrations.CreateModel(
            name='Rack',
            fields=[
                ('created', models.DateField(auto_now_add=True, null=True)),
                ('last_updated', models.DateTimeField(auto_now=True, null=True)),
                ('custom_field_data', models.JSONField(blank=True, default=dict, encoder=CustomFieldJSONEncoder)),
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                (
                    '_name',
                    utilities.fields.NaturalOrderingField(
                        'name', blank=True, max_length=100, naturalize_function=utilities.ordering.naturalize
                    ),
                ),
                ('facility_id', models.CharField(blank=True, max_length=50, null=True)),
                ('status', models.CharField(default='active', max_length=50)),
                ('serial', models.CharField(blank=True, max_length=50)),
                ('asset_tag', models.CharField(blank=True, max_length=50, null=True, unique=True)),
                ('type', models.CharField(blank=True, max_length=50)),
                ('width', models.PositiveSmallIntegerField(default=19)),
                (
                    'u_height',
                    models.PositiveSmallIntegerField(
                        default=42,
                        validators=[
                            django.core.validators.MinValueValidator(1),
                            django.core.validators.MaxValueValidator(100),
                        ],
                    ),
                ),
                ('desc_units', models.BooleanField(default=False)),
                ('outer_width', models.PositiveSmallIntegerField(blank=True, null=True)),
                ('outer_depth', models.PositiveSmallIntegerField(blank=True, null=True)),
                ('outer_unit', models.CharField(blank=True, max_length=50)),
                ('comments', models.TextField(blank=True)),
            ],
            options={
                'ordering': ('site', 'location', '_name', 'pk'),
            },
        ),
        migrations.CreateModel(
            name='RackReservation',
            fields=[
                ('created', models.DateField(auto_now_add=True, null=True)),
                ('last_updated', models.DateTimeField(auto_now=True, null=True)),
                ('custom_field_data', models.JSONField(blank=True, default=dict, encoder=CustomFieldJSONEncoder)),
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                (
                    'units',
                    django.contrib.postgres.fields.ArrayField(base_field=models.PositiveSmallIntegerField(), size=None),
                ),
                ('description', models.CharField(max_length=200)),
            ],
            options={
                'ordering': ['created', 'pk'],
            },
        ),
        migrations.CreateModel(
            name='RackRole',
            fields=[
                ('created', models.DateField(auto_now_add=True, null=True)),
                ('last_updated', models.DateTimeField(auto_now=True, null=True)),
                ('custom_field_data', models.JSONField(blank=True, default=dict, encoder=CustomFieldJSONEncoder)),
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100, unique=True)),
                ('slug', models.SlugField(max_length=100, unique=True)),
                ('color', utilities.fields.ColorField(default='9e9e9e', max_length=6)),
                ('description', models.CharField(blank=True, max_length=200)),
            ],
            options={
                'ordering': ('name',),
            },
        ),
        migrations.CreateModel(
            name='RearPort',
            fields=[
                ('created', models.DateField(auto_now_add=True, null=True)),
                ('last_updated', models.DateTimeField(auto_now=True, null=True)),
                ('custom_field_data', models.JSONField(blank=True, default=dict, encoder=CustomFieldJSONEncoder)),
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=64)),
                (
                    '_name',
                    utilities.fields.NaturalOrderingField(
                        'name', blank=True, max_length=100, naturalize_function=utilities.ordering.naturalize
                    ),
                ),
                ('label', models.CharField(blank=True, max_length=64)),
                ('description', models.CharField(blank=True, max_length=200)),
                ('_cable_peer_id', models.PositiveIntegerField(blank=True, null=True)),
                ('mark_connected', models.BooleanField(default=False)),
                ('type', models.CharField(max_length=50)),
                (
                    'positions',
                    models.PositiveSmallIntegerField(
                        default=1,
                        validators=[
                            django.core.validators.MinValueValidator(1),
                            django.core.validators.MaxValueValidator(1024),
                        ],
                    ),
                ),
            ],
            options={
                'ordering': ('device', '_name'),
            },
        ),
        migrations.CreateModel(
            name='RearPortTemplate',
            fields=[
                ('created', models.DateField(auto_now_add=True, null=True)),
                ('last_updated', models.DateTimeField(auto_now=True, null=True)),
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=64)),
                (
                    '_name',
                    utilities.fields.NaturalOrderingField(
                        'name', blank=True, max_length=100, naturalize_function=utilities.ordering.naturalize
                    ),
                ),
                ('label', models.CharField(blank=True, max_length=64)),
                ('description', models.CharField(blank=True, max_length=200)),
                ('type', models.CharField(max_length=50)),
                (
                    'positions',
                    models.PositiveSmallIntegerField(
                        default=1,
                        validators=[
                            django.core.validators.MinValueValidator(1),
                            django.core.validators.MaxValueValidator(1024),
                        ],
                    ),
                ),
            ],
            options={
                'ordering': ('device_type', '_name'),
            },
        ),
        migrations.CreateModel(
            name='Region',
            fields=[
                ('created', models.DateField(auto_now_add=True, null=True)),
                ('last_updated', models.DateTimeField(auto_now=True, null=True)),
                ('custom_field_data', models.JSONField(blank=True, default=dict, encoder=CustomFieldJSONEncoder)),
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100, unique=True)),
                ('slug', models.SlugField(max_length=100, unique=True)),
                ('description', models.CharField(blank=True, max_length=200)),
                ('lft', models.PositiveIntegerField(editable=False)),
                ('rght', models.PositiveIntegerField(editable=False)),
                ('tree_id', models.PositiveIntegerField(db_index=True, editable=False)),
                ('level', models.PositiveIntegerField(editable=False)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Site',
            fields=[
                ('created', models.DateField(auto_now_add=True, null=True)),
                ('last_updated', models.DateTimeField(auto_now=True, null=True)),
                ('custom_field_data', models.JSONField(blank=True, default=dict, encoder=CustomFieldJSONEncoder)),
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100, unique=True)),
                (
                    '_name',
                    utilities.fields.NaturalOrderingField(
                        'name', blank=True, max_length=100, naturalize_function=utilities.ordering.naturalize
                    ),
                ),
                ('slug', models.SlugField(max_length=100, unique=True)),
                ('status', models.CharField(default='active', max_length=50)),
                ('facility', models.CharField(blank=True, max_length=50)),
                ('asn', ipam.fields.ASNField(blank=True, null=True)),
                ('time_zone', timezone_field.fields.TimeZoneField(blank=True)),
                ('description', models.CharField(blank=True, max_length=200)),
                ('physical_address', models.CharField(blank=True, max_length=200)),
                ('shipping_address', models.CharField(blank=True, max_length=200)),
                ('latitude', models.DecimalField(blank=True, decimal_places=6, max_digits=8, null=True)),
                ('longitude', models.DecimalField(blank=True, decimal_places=6, max_digits=9, null=True)),
                ('contact_name', models.CharField(blank=True, max_length=50)),
                ('contact_phone', models.CharField(blank=True, max_length=20)),
                ('contact_email', models.EmailField(blank=True, max_length=254)),
                ('comments', models.TextField(blank=True)),
            ],
            options={
                'ordering': ('_name',),
            },
        ),
        migrations.CreateModel(
            name='SiteGroup',
            fields=[
                ('created', models.DateField(auto_now_add=True, null=True)),
                ('last_updated', models.DateTimeField(auto_now=True, null=True)),
                ('custom_field_data', models.JSONField(blank=True, default=dict, encoder=CustomFieldJSONEncoder)),
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100, unique=True)),
                ('slug', models.SlugField(max_length=100, unique=True)),
                ('description', models.CharField(blank=True, max_length=200)),
                ('lft', models.PositiveIntegerField(editable=False)),
                ('rght', models.PositiveIntegerField(editable=False)),
                ('tree_id', models.PositiveIntegerField(db_index=True, editable=False)),
                ('level', models.PositiveIntegerField(editable=False)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='VirtualChassis',
            fields=[
                ('created', models.DateField(auto_now_add=True, null=True)),
                ('last_updated', models.DateTimeField(auto_now=True, null=True)),
                ('custom_field_data', models.JSONField(blank=True, default=dict, encoder=CustomFieldJSONEncoder)),
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=64)),
                ('domain', models.CharField(blank=True, max_length=30)),
                (
                    'master',
                    models.OneToOneField(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.PROTECT,
                        related_name='vc_master_for',
                        to='dcim.device',
                    ),
                ),
            ],
            options={
                'verbose_name_plural': 'virtual chassis',
                'ordering': ['name'],
            },
        ),
    ]
