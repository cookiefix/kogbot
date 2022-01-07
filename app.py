# TODO fking add .predmet v Ura, in .json database za userje da si zberejo kaj nimajoimport fbchat
# TODO user_database mapa: notr nrdi file ko spozna userja prvič; notr pise preference za predmete in reminderje ce je treba
# TODO se en ALL_USERS file v mapi ki pa je za pošiljanje vsem userjem
# TODO sms 6 dni pred izpiti + kolokviji
# TODO izpiti date f, render f, update za app za izpiti f

from urnik import URNIK, WEEKDAYS, WEEKDAYS_R
import urnik
import fbchat
from izpiti import IZPITI_P
import izpiti

USERNAME = "kogbot@protonmail.com"
PASSWORD = "KogBotTopDown2021"
HELP_LIST = {0:f"POMOČ UPORABNIKOM\nČe kej ne prime probi poslat se enkrat haha.\nBot NE uporablja nobenih posebnih znakov ( \"ali_ ), SAMO crke in presledki.\nVse funkcije:\nurnik | urnik dan | izpiti | izpiti next\nVelike/male crke nimajo vpliva.\nZa več info napiši npr:\n\"help urnik dan\"",
             "urnik": "Funkcija URNIK:\nPreprosto pošlješ besedo urnik.\nPove naslednje predavanje oz. kaj trenutno poteka. Če danes predavanj ni več pove kdaj je nasledni dan z predavanji.",
             "urnik dan": "Funkcija URNIK DAN\nPošješ: urnik dan\nNamesto dan napiši dan brez šumnikov.\nPove celoten urnik izbranega dneva oz. če je dan prazen.",
             "izpiti": "Funkcija IZPITI\nPošješ: izpiti\nTrenutno pove vse obveznosti, ki jih imamo za oddat. Izboljšave sledijo...",
             "izpiti next": "Funkcija IZPITI NEXT\nPošješ: izpiti next\nPove naslednji datum z obveznostmi, čez koliko dni bo in obveznosti, ki jih imamo za oddat/se učit."}

urnik_r = {dan:[urnik.Ura(ura["start"],ura["end"],ura["day"],ura["title"]) for ura in URNIK if ura["day"] == dan] for dan in WEEKDAYS}
cur_date = izpiti.get_date()
datum_obv = {k: izpiti.DatumObv(k,v) for k,v in IZPITI_P.items() if k[1] > cur_date[1] or (k[0] > cur_date[0] and k[1] == cur_date[1])}

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
        # command help
        elif "help" in text:
            if text == "help":
                self.send(fbchat.Message(text=HELP_LIST[0]), thread_id, thread_type)
            else:
                self.send(fbchat.Message(text=HELP_LIST[text.strip("help ")]), thread_id, thread_type)
        # nik je car
        elif "kdo" in text and "car" in text:
            self.send(fbchat.Message(text="NIK je CAR B) !"), thread_id, thread_type)
        # izpiti beta
        elif "izpiti" in text:
            dan, mesec = izpiti.get_date()
            vsi_izpiti = sorted([obvs for datum, obvs in datum_obv.items() if datum[1] > mesec or (datum[0] > dan and datum[1] == mesec)], key=lambda x: x.days_till())
            if "izpiti" == text:
                t = "\n".join(["IZPITI"]+[obvs.render_obv() for obvs in vsi_izpiti])
                self.send(fbchat.Message(text=t), thread_id, thread_type)
            # izpit beta modifiers
            elif text.split(" ")[0] == "izpiti" and text.split(" ")[1] != "":
                modifier = text.split(" ")[1]
                t_mod = {"next": "\n".join([f"NEXT ČEZ {vsi_izpiti[0].days_till()} dni!\n{vsi_izpiti[0].render_obv()}"])}
                self.send(fbchat.Message(text=t_mod[modifier]), thread_id, thread_type)


client = OnMessClient(USERNAME, PASSWORD)

client.listen()