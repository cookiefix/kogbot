from datetime import date

IZPITI_P = {(4,1): ["PROG naloga za oceno"],

(10,1): ["UKZ oddaja seminarske", "UR poročilo o raziskovalnem načrtu", "UI domača naloga"],

(11,1): ["UKZ predstavitve seminarske"],

(13,1): ["UKZ predstavitve seminarske"],

(17,1): ["PROG izpit"],

(19,1): ["NEVRA izpit"],

(21,1): ["UKZ izpit"],

(24,1): ["UR izpit", "UR končno poročilo"],

(25,1): ["STAT izpit", "UI seminarska"],

(26,1): ["Prijava na Erasmus+ izmenjavo"],

(27,1): ["UI izpit"],

(1,2): ["PROG izpit"],

(3,2): ["NEVRA izpit"],

(4,2): ["STAT izpit"],

(7,2): ["UKZ izpit"],

(10,2): ["UR izpit"]}

# TODO class za obveznost, te se doda v dict k jih uredi po datumih lahko ma tut vsaka obveznost datum

class DatumObv():
    def __init__(self, datum, obv):
        self.obveznosti = obv
        self.datum = datum

    def render_obv(self):
        s = f"\n{self.datum[0]}. {self.datum[1]}. 2022"
        for o in self.obveznosti:
            s += "\n- " + o
        return s

    def days_till(self):
        d,m = get_date()
        self.datum
        return (self.datum[0] + {1: 0, 2: 31, 3: 59, 4: 90, 5: 120, 6: 151, 7: 181, 8: 212, 9: 243, 10: 273, 11: 303, 12: 334}[self.datum[1]]) - \
               (d + {1: 0, 2: 31, 3: 59, 4: 90, 5: 120, 6: 151, 7: 181, 8: 212, 9: 243, 10: 273, 11: 303, 12: 334}[m])
    
    def convert_to_days(self):
        return self.datum[0] + {1: 0, 2: 31, 3: 59, 4: 90, 5: 120, 6: 151, 7: 181, 8: 212, 9: 243, 10: 273, 11: 303, 12: 334}[self.datum[1]]
           

def get_date():
    return (date.today().day, date.today().month)

def convert_days(obv):
    return obv.datum[0] + {1: 0, 2: 31, 3: 59, 4: 90, 5: 120, 6: 151, 7: 181, 8: 212, 9: 243, 10: 273, 11: 303, 12: 334}[obv.datum[1]]
