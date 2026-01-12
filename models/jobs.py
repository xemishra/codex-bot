from tortoise.models import Model
from tortoise import fields

class Job(Model):
    id = fields.IntField(pk=True)
    title = fields.CharField(max_length=200)
    company_name = fields.CharField(max_length=150)
    description = fields.TextField()
    location = fields.CharField(max_length=150, null=True)
    job_type = fields.CharField(max_length=50)
    experience_level = fields.CharField(max_length=50, null=True)
    salary_range = fields.CharField(max_length=100, null=True)
    required_skills = fields.JSONField(null=True)
    application_url = fields.CharField(max_length=500)
    application_deadline = fields.DatetimeField(null=True)
    posted_by = fields.ForeignKeyField(
        'models.User', related_name='posted_jobs')
    is_active = fields.BooleanField(default=True)
    view_count = fields.IntField(default=0)
    created_at = fields.DatetimeField(auto_now_add=True)
    updated_at = fields.DatetimeField(auto_now=True)

    class Meta:
        table = "jobs"

    def __str__(self):
        return f"{self.title} at {self.company_name}"
