from models import User

async def isuser(user_id) -> bool:
    """Checking is user already registered"""
    return await User.exists(telegram_id=user_id)