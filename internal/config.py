import os


class Config:
    def __init__(self):
        """Initialize configuration with default settings."""
        self.tel_key = os.getenv("TELEGRAM_API_KEY")
        if not self.tel_key:
            raise ValueError("Missing TELEGRAM_API_KEY environment variable")
