from pydantic import BaseSettings, AnyHttpUrl, SecretStr
from typing import List

class Settings(BaseSettings):
    depth: int = 2
    timeout: int = 10
    g2g_url: AnyHttpUrl
    z2u_url: AnyHttpUrl
    proxies: List[str] = []
    platform_fee: float = 0.10
    payment_fee: float = 0.03
    conversion_fee: float = 0.02
    roi_threshold: float = 0.15
    telegram_token: SecretStr = None
    telegram_chat: str = None
    slack_webhook: AnyHttpUrl = None
    email_user: str = None
    email_password: SecretStr = None
    email_recipients: List[str] = []
    auto_purchase: bool = False

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"

settings = Settings()
