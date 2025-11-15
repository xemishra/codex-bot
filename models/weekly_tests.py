from tortoise.models import Model
from tortoise import fields


class WeeklyTest(Model):
    id = fields.IntField(pk=True)
    title = fields.CharField(max_length=200)
    description = fields.TextField()
    test_date = fields.DatetimeField()
    duration_minutes = fields.IntField()
    total_marks = fields.IntField()
    passing_marks = fields.IntField()
    difficulty_level = fields.CharField(max_length=50)
    topics = fields.JSONField(null=True)
    questions = fields.JSONField(null=True)
    created_by = fields.ForeignKeyField(
        'models.User', related_name='created_tests')
    is_active = fields.BooleanField(default=True)
    is_published = fields.BooleanField(default=False)
    created_at = fields.DatetimeField(auto_now_add=True)
    updated_at = fields.DatetimeField(auto_now=True)

    class Meta:
        table = "weekly_tests"

    def __str__(self):
        return self.title


class TestSubmission(Model):
    id = fields.IntField(pk=True)
    test = fields.ForeignKeyField(
        'models.WeeklyTest', related_name='submissions')
    user = fields.ForeignKeyField(
        'models.User', related_name='test_submissions')
    answers = fields.JSONField()
    score = fields.IntField(null=True)
    submitted_at = fields.DatetimeField(auto_now_add=True)
    time_taken_minutes = fields.IntField(null=True)
    is_evaluated = fields.BooleanField(default=False)

    class Meta:
        table = "test_submissions"
        unique_together = (('test', 'user'),)

    def __str__(self):
        return f"{self.user} - {self.test}"
