class Bruch(object):

    def __init__(self, *args):

        temp = args[0]

        if isinstance(temp, Bruch):
            self.nenner = temp.nenner
            self.zaehler = temp.zaehler
        elif isinstance(temp, int):
            self.nenner = 1
            self.zaehler = temp


        self.zaehler = args[0]
        if len(args) > 1:
            self.nenner = args[1]
        else:
            self.nenner = 1

    def _Bruch__makeBruch (value):
        return value

    def __abs__(self):
        return abs(float(self.zaehler) / float(self.nenner))

    def __int__(self):
        return int(self.zaehler) / int(self.nenner)

    def __float__(self):
        return float(self.zaehler) / float(self.nenner)

    def __str__(self):
        if self.zaehler < 0:
            self.zaehler = -self.zaehler
        if self.nenner < 0:
            self.nenner = -self.nenner
        return "(%d/%d)" % (self.zaehler,self.nenner)

    def __add__(self, other):
        return Bruch(self.zaehler+other, self.nenner)