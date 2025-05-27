import pandas as pd
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

SMTP_SERVER = "smtp.gmail.com"
SMTP_PORT = 587
EMAIL_SENDER = "your_email@gmail.com"        
EMAIL_PASSWORD = "your_app_password_here"      

csv_file = r"C:\Users\paava\OneDrive\Documents\Java Programs\Python Projects\Personalized_Messages.csv"
df_messages = pd.read_csv(csv_file)

def send_email(to_email, subject, message_body):
    msg = MIMEMultipart()
    msg['From'] = EMAIL_SENDER
    msg['To'] = to_email
    msg['Subject'] = subject
    msg.attach(MIMEText(message_body, 'plain'))

    try:
        with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as server:
            server.starttls()
            server.login(EMAIL_SENDER, EMAIL_PASSWORD)
            server.send_message(msg)
        print(f"✅ Email sent to {to_email}")
    except Exception as e:
        print(f"❌ Failed to send to {to_email}: {e}")

# === LOOP TO SEND ALL EMAILS ===
for index, row in df_messages.iterrows():
    email = row.get("email")
    message = row.get("message")
    if pd.notna(email) and "@" in email and pd.notna(message):
        send_email(email, "Event Follow-up", message)
