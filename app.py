# TODO fking add .predmet v Ura, in .json database za userje da si zberejo kaj nimajoimport fbchat
# TODO user_database mapa: notr nrdi file ko spozna userja prvič; notr pise preference za predmete in reminderje ce je treba
# TODO se en ALL_USERS file v mapi ki pa je za pošiljanje vsem userjem
# TODO sms 6 dni pred izpiti + kolokviji


from urnik import URNIK, WEEKDAYS, WEEKDAYS_R, get_day_agenda, get_time, get_weekday, next_lecture, today_no_more
import urnik
import fbchat
from izpiti import IZPITI_P
import izpiti

USERNAME = "kogbot@protonmail.com"
PASSWORD = "KogBotTopDown2021"
HELP_LIST = {0:"POMOČ UPORABNIKOM\nČe kej ne prime probi poslat se enkrat haha.\nBot NE uporablja nobenih posebnih znakov ( \"ali_ ), SAMO crke in presledki.\nVse funkcije:\nurnik | urnik dan | izpiti\nVelike/male crke nimajo vpliva.\nZa več info napiši npr:\n\"help urnik dan\"",
             "urnik": "Funkcija URNIK:\nPreprosto pošlješ besedo urnik.\nPove naslednje predavanje oz. kaj trenutno poteka. Če danes predavanj ni več pove kdaj je nasledni dan z predavanji.",
             "urnik dan": "Funkcija URNIK DAN\nPošješ: urnik dan\nNamesto dan napiši dan brez šumnikov.\nPove celoten urnik izbranega dneva oz. če je dan prazen.",
             "izpiti": "Funkcija IZPITI\nPošješ: izpiti\nTrenutno le pove vse obveznosti, ki jih imamo za oddat. Izboljšave sledijo..."}

urnik_r = {dan:[urnik.Ura(ura["start"],ura["end"],ura["day"],ura["title"]) for ura in URNIK if ura["day"] == dan] for dan in WEEKDAYS}

class OnMessClient(fbchat.Client):
    def onMessage(self, mid, author_id, message_object, thread_id, thread_type, ts, metadata, msg, **kwargs):
        text = message_object.text.strip().lower()
        
        # command urnik
        if text == "urnik":
            self.send(fbchat.Message(text=urnik.next_lecture(urnik_r)), thread_id, thread_type)
        # command urnik <dan>
        elif "urnik" in text and text.split(" ")[1] in WEEKDAYS_R.keys():
            day_i = WEEKDAYS_R[text.split(" ")[1]]
            if urnik_r[day_i] == []:
                t = f"{WEEKDAYS[day_i].capitalize()} je FREJ :D !"
            else:
                t = "------\n".join([text.split(" ")[1].upper() + "\n"] + [u.msg() for u in urnik.get_day_agenda(urnik_r, day=day_i)])
            self.send(fbchat.Message(text=t), thread_id, thread_type)
        # help
        elif "help" in text:
            if text == "help":
                self.send(fbchat.Message(text=HELP_LIST[0]), thread_id, thread_type)
            else:
                self.send(fbchat.Message(text=HELP_LIST[text.strip("help ")]), thread_id, thread_type)
        # nik je car
        elif "kdo" in text and "car" in text:
            self.send(fbchat.Message(text="NIK je CAR B) !"), thread_id, thread_type)
        # izpiti beta
        elif "izpiti" == text:
            self.send(fbchat.Message(text=IZPITI_P), thread_id, thread_type)
        

client = OnMessClient(USERNAME, PASSWORD)

client.listen()





