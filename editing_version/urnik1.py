import time
import datetime

WEEKDAYS = {0:"ponedeljek",1:"torek",2:"sreda",3:"cetrtek",4:"petek",5:"sobota",6:"nedelja"}
WEEKDAYS_R = {v:k for k,v in WEEKDAYS.items()}
#dodatek ČETRTEK
WEEKDAYS_R["četrtek"] = 3
URNIK = [
{"title": 'Umetna inteligenca 1\nBratko / Domen',
"start": (10, 00),
"end": (13, 00),
"day": 0
			}
	,
{"title": 'Kognitivna nevroznanost 1\nPirtošek / Tjaša',
"start": (14, 00),
"end": (17, 25),
"day": 0
}
	,
{"title": 'Uvod v kognitivno znanost 1\nOlga',
"start": (11, 20),
"end": (12, 50),
"day": 1
}
	,
{"title": 'Programiranje\nDemšar',
"start": (13, 45),
"end": (17, 00),
"day": 1
}
	,
{"title": 'Programiranje vaje\nIZBIRNO, Primož',
"start": (10, 30),
"end": (13, 0),
"day": 2   
}
    ,
{"title": 'Uvod v raziskovanje 1\nKordeš / Bon / Jaša',
"start": (14, 30),
"end": (17, 40),
"day": 2   
}
	,
{"title": 'Uvod v jezikoslovje\nTatjana Marvin',
"start": (9, 00),
"end": (12, 00),
"day": 3
}
	,
{"title": 'Uvod v kognitivno znanost 1\nToma / Jaša',
"start": (13, 00),
"end": (14, 30),
"day": 3
}
	,
{"title": 'Uvod v statistiko\nSočan',
"start": (16, 0),
"end": (19, 30),
"day": 3   
}]

class Ura():
    def __init__(self, start, end, dayint, name) -> None:
        self.start = start
        self.end = end
        self.day = dayint
        self.name = name 

    def msg(self):
            return f"{self.name}\n" \
                   f"+ začetek: {self.render_s_time()}\n" \
                   f"+ konec: {self.render_e_time()}\n"

    def get_hours(self):
        return (self.start, self.end)

    def render_s_time(self):
        h,m = self.start
        if m == 00:
            m = "00"
        return f"{h}:{m}"

    def render_e_time(self):
        h,m = self.end
        if m == 00:
            m = "00"
        return f"{h}:{m}"

def get_weekday():
	return datetime.datetime.today().weekday()

def get_time():
    t = datetime.datetime.now()
    return (int(t.strftime("%H")),int(t.strftime("%M")))
    
def next_lecture(urnik):
    #getuser!!!
    t_h, t_m = get_time()
    day = get_day_agenda(urnik, get_weekday())
    
    for ura in day:
        (us_h,us_m) = ura.start
        (ue_h,ue_m) = ura.end

        # trenutno predavanje
        if (us_h*60+us_m) <= (t_h*60+t_m) <= (ue_h*60+ue_m):
            h, m = calc_time_till((ue_h, ue_m), (t_h, t_m))
            return f"TRENUTNEGA predavanja bo konec čez {h}h, {m}min:\n{ura.msg()}"
        
        # trenutno ne poteka predavanje, zato vrne prvo naslednje danes
        if (t_h*60+t_m) <= (us_h*60+us_m):
            h, m = calc_time_till((t_h, t_m), (us_h, us_m))
            return f"NEXT ČEZ {h}h, {m}min:\n{ura.msg()}"
    # ta dan ni več pouka, da 1. naslednji dan, ki ima pouk in 1. uro tisti dan    
    n = 1
    tmrw = get_weekday()+n
    while urnik[tmrw] == []:
        n += 1
        if tmrw > 6:
            tmrw = 0
            n = 0
    return f"Naslednje predavanje je v {WEEKDAYS[tmrw].upper()}!\n{get_day_agenda(urnik, tmrw)[0].msg()}\n"

def get_day_agenda(urnik: dict, day):
		return list(urnik[day])

def calc_time_till(current, target):
    c_h, c_m = current
    t_h, t_m = target
    mins = abs((c_h*60 + c_m) - (t_h*60 + t_m))
    return (mins//60, mins%60)
