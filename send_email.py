import schedule
import time
import smtplib
from email.mime.text import MIMEText

def send_email():
    # create email content
    msg = MIMEText("这是一封从 Python 发出的测试邮件！", "plain", "utf-8")
    msg["Subject"] = "Python 邮件测试"
    msg["From"] = "send@example.com"
    msg["To"] = "recv@example.com"

    # login and send email
    server = smtplib.SMTP_SSL("smtp.qq.com", 465)
    server.login("send@example.com", "your_authorization_code")
    server.sendmail("send@example.com", ["recv@example.com"], msg.as_string())
    server.quit()

if __name__ == "__main__":
        # schedule the email to be sent daily at 10:00 AM (just the example)
        schedule.every().day.at("10:00").do(send_email)

        while True:
            schedule.run_pending()
            time.sleep(1)
