import smtplib
from email.mime.text import MIMEText

def send_email(config, error_lines):
    smtp_server = config['email']['smtp_server']
    port = config['email']['port']
    sender = config['email']['sender']
    recipients = config['email']['recipients']
    subject = config['email']['subject']

    body = "🚨 Alert! Errors Detected:\n\n" + "\n".join(error_lines)
    msg = MIMEText(body)
    msg['Subject'] = subject
    msg['From'] = sender
    msg['To'] = ", ".join(recipients)

    with smtplib.SMTP(smtp_server, port) as server:
        server.starttls()
        server.login(sender, config['email']['password'])
        server.sendmail(sender, recipients, msg.as_string())
