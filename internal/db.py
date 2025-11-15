from tortoise import Tortoise


async def init_db():
    await Tortoise.init(
        db_url="sqlite://db.sqlite3",
        modules={"models": [
            "models.user",
            "models.resources",
            "models.jobs",
            "models.startups",
            "models.project_ideas",
            "models.weekly_tests"
        ]},
    )
    await Tortoise.generate_schemas()
