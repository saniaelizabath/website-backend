import smtplib
from email.message import EmailMessage
from dotenv import load_dotenv
import os

load_dotenv()

SMTP_EMAIL = os.getenv("SMTP_EMAIL")
SMTP_PASSWORD = os.getenv("SMTP_PASSWORD")

print(f"Email: {SMTP_EMAIL}")
print(f"Password: {'*' * len(SMTP_PASSWORD)}")

msg = EmailMessage()
msg["From"] = SMTP_EMAIL
msg["To"] = SMTP_EMAIL  # Send to yourself
msg["Subject"] = "Test from EC2"
msg.set_content("This is a test email from EC2 server")

try:
    print("Connecting to Gmail SMTP...")
    with smtplib.SMTP_SSL("smtp.gmail.com", 465, timeout=10) as server:
        print("Logging in...")
        server.login(SMTP_EMAIL, SMTP_PASSWORD)
        print("Sending email...")
        server.send_message(msg)
        print("✅ Email sent successfully!")
except Exception as e:
    print(f"❌ Error: {e}")
