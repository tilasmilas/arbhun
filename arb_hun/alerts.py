import requests, smtplib
from email.message import EmailMessage
from typing import List, Dict
from arb_hun.config import settings

def notify(results: List[Dict]) -> None:
    if not results: return
    summary = "".join(
        f\"{r['title']}: 💰{r['profit']:.2f} ROI {r['margin']:.2%}\\n\"
        for r in results
    )
    if settings.telegram_token and settings.telegram_chat:
        requests.post(
            f\"https://api.telegram.org/bot{settings.telegram_token.get_secret_value()}/sendMessage\",
            json={"chat_id": settings.telegram_chat, "text": summary}
        )
    if settings.slack_webhook:
        requests.post(settings.slack_webhook, json={"text": summary})
    if settings.email_user and settings.email_password and settings.email_recipients:
        msg = EmailMessage()
        msg['Subject'] = 'ArbHun Alerts'
        msg['From']    = settings.email_user
        msg['To']      = ",".join(settings.email_recipients)
        msg.set_content(summary)
        with smtplib.SMTP('smtp.gmail.com', 587) as smtp:
            smtp.starttls()
            smtp.login(settings.email_user, settings.email_password.get_secret_value())
            smtp.send_message(msg)
