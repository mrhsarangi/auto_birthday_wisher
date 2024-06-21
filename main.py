import smtplib
from datetime import date
from random import randint
from collections import namedtuple


# CONSTANTS
FILEPATH = "data/data.csv"
PORT = 465
SMTP_SERVER = "smtp.gmail.com"
SENDER_EMAIL = "1920hrud@gmail.com"
PASSWORD = "aqup dmze iyiv fthu"


def load_data(filepath: str) -> list[tuple]:
    """
        Reads data from given file and returns a list of person
        objects having attrs as name, email and dob.
    ------------------------------------------------------------------------
        args:
        filepath : Path of the file containing data about birthdays ( str )

    """
    data = []
    with open(filepath) as f:
        fields = [ s.strip() for s in f.readline().split(',')]
        Person = namedtuple('Person', fields)
        for line in f.readlines():
            attrs = [s.strip() for s in line.split(',')]
            data.append(Person(*attrs))
    return data


def send_wish(name: str, email: str) -> None:
    """
        Sends birthday wish using a randomly selected birthday wish
        template.

    --------------------------------------------------------------------
        args:
        name  : Recipient's name  ( str )
        email : Recipient's email ( str ) 
    
    """
    choice = randint(1, 4)
    with open(f"templates/wish{choice}.txt") as f:
        body = f.read()
    body = body.replace("[name]", name)    
    
    try:
        with smtplib.SMTP_SSL(SMTP_SERVER, PORT) as smtp_server:
            smtp_server.ehlo_or_helo_if_needed()
            smtp_server.login(SENDER_EMAIL, PASSWORD)
            smtp_server.sendmail(SENDER_EMAIL, email, body)
        print(f'Wish sent to {name} at {email}')
    except Exception as e:
        print("Exception encountered:\n", e)
        

if __name__ == "__main__":

    data = load_data(FILEPATH)
    
    today = str(date.today())
    year, month, day = [s.strip() for s in today.split('-')]
    
    for person in data[:]:
        birth_month, birth_day = person.dob.split('-')
        if month == birth_month and day == birth_day:
            print("Sending mail")
            send_wish(person.name, person.email)

exit(0)