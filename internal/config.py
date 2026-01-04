import os
# from internal import logger

class Config:
    def __init__(self):
        """Initialize configuration with default settings."""
        self.botApi = os.getenv("botApi", "8117220965:AAEa__gznVseo_VH2G6NSVsrXpnTLvxibqc")
        self.baseUrl = os.getenv("baseUrl", "https://erp.saitm.ac.in")
        # self.loggerId = int(os.getenv("loggerId", ""))
