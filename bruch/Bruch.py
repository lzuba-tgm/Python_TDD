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

        if self.nenner == 0:
            raise ZeroDivisionError
        elif isinstance(self.nenner,float) or isinstance(self.zaehler,float) or isinstance(self.zaehler,str):
            raise TypeError

    @staticmethod
    def __makeBruch (value):
        return Bruch(value)

    def __abs__(self):
        return abs(float(self.zaehler) / float(self.nenner))

    def __int__(self):
        return int(self.zaehler) / int(self.nenner)

    def __float__(self):
        return float(self.zaehler) / float(self.nenner)

    def __str__(self):

        if self.nenner == 1:
            part = int(self.zaehler) / int(self.nenner)
            print part
            return '(%d)' % part

        if self.zaehler < 0:
            self.zaehler = -self.zaehler
        if self.nenner < 0:
            self.nenner = -self.nenner
        return "(%d/%d)" % (self.zaehler,self.nenner)

    def __iadd__(self, other):
        return self+other

    def __invert__(self):
        return Bruch(self.nenner,self.zaehler)

    def __neg__(self):
        return Bruch(-1 * self.zaehler,self.nenner)

    def __pow__(self, power, modulo=None):
        if isinstance(power, int):
            return Bruch(self.zaehler ** power, self.nenner ** power)
        else:
            raise TypeError

    def __add__(self, *args):
        part = 0

        if isinstance(args[0], int):
            part += float(Bruch(self.zaehler, self.nenner)) + float(args[0])
        elif isinstance(args[0], Bruch):
            part += float(Bruch(self.zaehler, self.nenner)) + float(Bruch(args[0].zaehler, args[0].nenner))
        else:
            for i in len(args):
                if isinstance(t,int):
                    part += float(Bruch(self.zaehler, self.nenner)) + float(args)
                elif isinstance(t,Bruch):
                    t = args[i]
                    part += float(Bruch(self.zaehler, self.nenner)) + float(Bruch(t.zaehler, t.nenner))
        return part

    def __eq__(self, other):
        return float(self) == float(other)

    def __ge__(self, other):
        return float(self) >= float(other)

    def __gt__(self, other):
        return float(self) > float(other)

    def __le__(self, other):
        return float(self) <= float(other)

    def __lt__(self, other):
        return float(self) < float(other)

    def __ne__(self, other):
        return float(self) != float(other)

