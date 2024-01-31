import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication
from config import *

from random import choice

def generate_name_files(len_token=20):
    GEN_CONST = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p',
                 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    new_token = ""
    for _ in range(len_token):
        new_token += choice(GEN_CONST)
    return new_token


class Emailer:
    def __init__(self) -> None:
        self.sender_email = "od.ob@yandex.ru"
        self.smtp_username = "od.ob@yandex.ru"
        self.smtp_password = "nshtntsxecjxhntb"


    def send_email(self, recipient_email, subject, text) -> bool:

        # Создание объекта MIMEMultipart и добавление темы и текста письма
        msg = MIMEMultipart()
        msg['From'] = self.sender_email
        msg['To'] = recipient_email
        msg['Subject'] = subject
        msg.attach(MIMEText(text))

        # Отправка письма через SMTP-сервер Yandex
        try:
            smtp_connection = smtplib.SMTP_SSL('smtp.yandex.ru', 465)
            smtp_connection.login(self.smtp_username, self.smtp_password)
            smtp_connection.sendmail(self.sender_email, recipient_email, msg.as_string())
            smtp_connection.close()
            print("Email sent successfully!")
            return True
        except Exception as e:
            print("Error sending email: ", e)
            return False
        
    def confirmation_by_email(self, address,link):
        try:
            text = f'''Здравствуйте!
В приложение НЕЙРОМУЗЫКА была произведена регистрация с использованием вашей электронной почты.
Email: {address}
Для подтверждения регистрации пройдите по ссылке:
{FULL_LINK}/confirm/{link}

С уважением,
Администрация НЕЙРОМУЗЫКА'''
            if self.send_email(address, 'Подтверждение аккаунта НЕЙРОМУЗЫКА', text):
                return link
            return False
        except:
            return False
        
    def test(self):
        self.confirmation_by_email('dmitryodintsov2007@gmail.com','ee')

if __name__ == '__main__':
    emailer = Emailer()
    emailer.test()