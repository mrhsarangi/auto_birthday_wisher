import smtplib
from datetime import date
from random import randint
from email.mime.text import MIMEText


# CONSTANTS
FILEPATH = "data/data.csv"
PORT = 465
SMTP_SERVER = "smtp.gmail.com"
SENDER_EMAIL = "1920hrud@gmail.com"
PASSWORD = "aqup dmze iyiv fthu"

def load_data(filepath: str) -> list[tuple]:
    data = []
    with open(filepath) as f:
        header = [ s.strip() for s in f.readline().split(',')]
        print(header)
        for line in f.readlines():
            name, dob, email = [s.strip() for s in line.split(',')]
            data.append((name, dob, email))

    return data


def send_wish(name: str, email: str) -> None:
    test_msg = "Test Mail"
    try:
        with smtplib.SMTP_SSL(SMTP_SERVER, PORT) as smtp_server:
            smtp_server.ehlo()
            smtp_server.login(SENDER_EMAIL, PASSWORD)
            smtp_server.sendmail(SENDER_EMAIL, email, test_msg)
        print(f'Wish sent to {name} at {email}')
    except Exception as e:
        print("Exception encountered:\n", e)
        


if __name__ == "__main__":
    data = load_data(FILEPATH)

    today = str(date.today())
    year, month, day = [s.strip() for s in today.split('-')]
    
    for name, dob, email in data[:]:
        # convert dob to int and then to a date object
        birth_month, birth_day = dob.split('-')
        if month == birth_month and day == birth_day:
            print("Sending mail")
            send_wish(name, email)

    exit(0)