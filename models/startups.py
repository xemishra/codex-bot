from tortoise.models import Model
from tortoise import fields


class Startup(Model):
    id = fields.IntField(pk=True)
    name = fields.CharField(max_length=200)
    description = fields.TextField()
    industry = fields.CharField(max_length=100, null=True)
    stage = fields.CharField(max_length=50, null=True)
    founded_date = fields.DateField(null=True)
    website = fields.CharField(max_length=300, null=True)
    founder_names = fields.JSONField(null=True)
    team_size = fields.IntField(null=True)
    funding_amount = fields.CharField(max_length=100, null=True)
    tech_stack = fields.JSONField(null=True)
    is_hiring = fields.BooleanField(default=False)
    contact_email = fields.CharField(max_length=150, null=True)
    submitted_by = fields.ForeignKeyField(
        'models.User', related_name='submitted_startups')
    is_verified = fields.BooleanField(default=False)
    is_active = fields.BooleanField(default=True)
    created_at = fields.DatetimeField(auto_now_add=True)
    updated_at = fields.DatetimeField(auto_now=True)

    class Meta:
        table = "startups"

    def __str__(self):
        return self.name
