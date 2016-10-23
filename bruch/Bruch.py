class Bruch(object):
    """
    Diese Klasse stellt einen Bruch dar mit 1 oder 2 Parameter.
    Es handelt sich bei den meisten Methode, um ueberladene Methode die nur auf Bruch angepasst werden
    Ausserdem wird auch auf ungueltige Eingabe ueberprueft

        :ivar int zaehler:      Int, in dem die zaehler Zahl steht
        :ivar int nenner:      Int, in dem die nenner Zahl steht
        :ivar int new:      Int, in dem das Ergebnis steht
        :ivar int temp:      Int, in dem die erste Zahl von args steht

        :param Tupel *args:   Tupel, in dem die Zahlen stehen, weil mehr als eine Zahl moeglich ist
        :param int other:      Int, in dem Uebergabe-Zahl steht

    """

    def __init__(self, *args):
        """
        speichert die Parameter in Instanzvariablen, weist wenn nur eine Zahl uebergeben wird einen Standartwert zu
        und prueft auf ungueltige Eingaben

        :param Tupel *args:   Tupel, in dem die Zahlen stehen, weil mehr als eine Zahl moeglich ist
        """
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
        """
        Ruft die init Methode auf mit den Parameter value
        :param value: Zahl mit dem der Bruch gebildet werden soll
        :return: Ergebnis von Bruch
        """
        return Bruch(value)

    def __abs__(self):
        """
        Wandelt den Bruch in den absolut Wert um
        :return: Liefert den absolut Wert des Bruches zurueck
        """
        return abs(float(self.zaehler) / float(self.nenner))

    def __int__(self):
        """
        Wandelt den Bruch in den int Wert um
        :return: Liefert den int Wert des Bruches zurueck
        """
        return int(self.zaehler) / int(self.nenner)

    def __float__(self):
        """
        Wandelt den Bruch in den float Wert um
        :return: Liefert den float Wert des Bruches zurueck
        """
        return float(self.zaehler) / float(self.nenner)

    def __str__(self):
        """
        Wandelt den Bruch in String Werte um
        Kann auf 2 verschiedene Aufruf-Methode reagieren
        :ivar String new: String, in dem das Ergebnis steht
        :return: Liefert einen string Wert des Bruches zurueck
        """
        if self.nenner == 1:
            new = int(self.zaehler) / int(self.nenner)
            return '(%d)' % new

        if self.zaehler < 0:
            self.zaehler = -self.zaehler
        if self.nenner < 0:
            self.nenner = -self.nenner
        return "(%d/%d)" % (self.zaehler,self.nenner)

    def __iadd__(self, other):
        """
        Addiert other auf den Bruch
        :param other: Zahl, um die addiert werden soll
        :return: Liefert das Ergebniss zurueck
        """
        return self+other

    def __invert__(self):
        """
        Invertiert den Bruch
        :return: Liefert den invertierten Bruch zurueck
        """
        return Bruch(self.nenner,self.zaehler)

    def __neg__(self):
        """
        Negiert den Zeahler
        :return: :return: Liefert den negierten Bruch zurueck
        """
        return Bruch(-1 * self.zaehler,self.nenner)

    def __pow__(self, power, modulo=None):
        """
        Multipliziert zaehler und nenner mit sich selbst
        Ueberpruft ob die Zahl eine int Zahl ist
        :param int power: wie oft mit sich selbst multipiziert werden soll
        :return: Liefert das Ergebnis zurueck
        """
        if isinstance(power, int):
            return Bruch(self.zaehler ** power, self.nenner ** power)
        else:
            raise TypeError

    def __iter__(self):
        """
        Wandelt den Burch in eine Tupel um
        :return: Liefert den Tupel zurueck
        """
        return iter([self.zaehler,self.nenner])

    def __add__(self, *args):
        """
        Addiert eine Zahl oder einen Bruch auf diesen Bruch
        :ivar int new: Int, in dem das Ergebnis steht
        :param Tupel args: Tupel, in dem die Zahlen stehen, weil mehr als eine Zahl moeglich ist
        :return: Liefert das Ergebnis zurueck
        """
        new = 0

        if isinstance(args[0], int):
            new += float(Bruch(self.zaehler, self.nenner)) + float(args[0])
        elif isinstance(args[0], Bruch):
            new += float(Bruch(self.zaehler, self.nenner)) + float(Bruch(args[0].zaehler, args[0].nenner))
        else:
            for i in len(args):
                t = args[i]
        return new

    def __radd__(self, other):
        """
        Addiert eine Zahl auf den Bruch
        :param int other: Int, in dem die Zahl steht
        :return: Liefert das Ergebnis zurueck
        """
        return self + other

    def __sub__(self, *args):
        """
        Subtrahiert eine Zahl oder einen Bruch auf diesen Bruch
        :ivar int new: Int, in dem das Ergebnis steht
        :param Tupel args: Tupel, in dem die Zahlen stehen, weil mehr als eine Zahl moeglich ist
        :return: Liefert das Ergebnis zurueck
        """
        new = 0
        if isinstance(args[0], int):
            new += float(Bruch(self.zaehler, self.nenner)) - float(args[0])
        elif isinstance(args[0], Bruch):
            new += float(Bruch(self.zaehler, self.nenner)) - float(Bruch(args[0].zaehler, args[0].nenner))
        return new

    def __isub__(self, other):
        """
        Subtrahiert eine Zahl mit den Bruch
        Ueberpruft ob die Zahl eine float Zahl ist
        :param int other: Int, in dem die Zahl steht
        :return: Liefert das Ergebnis zurueck
        """
        if isinstance(other, str):
            raise TypeError

        return self - other

    def __rsub__(self, other):
        """
        Subtrahiert eine Zahl mit den Bruch
        Ueberpruft ob die Zahl eine float Zahl ist
        :param int other: Int, in dem die Zahl steht
        :return: Liefert das Ergebnis zurueck
        """
        if isinstance(other, float):
            raise TypeError

        return -self + other

    def __mul__(self, *args):
        """
        Multiplizert eine Zahl oder einen Bruch mit dem Bruch
        :ivar int new: Int, in dem das Ergebnis steht
        :param Tupel args: Tupel, in dem die Zahlen stehen, weil mehr als eine Zahl moeglich ist
        :return: Liefert das Ergebnis zurueck
        """
        if isinstance(args[0], float):
            raise TypeError
        new = 0
        if isinstance(args[0], int):
            new += float(Bruch(self.zaehler, self.nenner)) * float(args[0])
        elif isinstance(args[0], Bruch):
            new += float(Bruch(self.zaehler, self.nenner)) * float(Bruch(args[0].zaehler, args[0].nenner))
        return new

    def __rdiv__(self, other):
        """
        Dividiert eine Zahl durch den Bruch
        :param int other: Int, in dem die Zahl steht
        :return: Liefert das Ergebnis zurueck
        """
        return self / other

    def __div__(self, *args):
        """
        ividiert eine Zahl oder einen Bruch durch den Bruch
        :ivar int new: Int, in dem das Ergebnis steht
        :param Tupel args: Tupel, in dem die Zahlen stehen, weil mehr als eine Zahl moeglich ist
        :return: Liefert das Ergebnis zurueck
        """
        new = 0
        if isinstance(args[0], int):
            new += float(Bruch(self.zaehler, self.nenner)) / float(args[0])
        elif isinstance(args[0], Bruch):
            new += float(Bruch(self.zaehler, self.nenner)) / float(Bruch(args[0].zaehler, args[0].nenner))
        return new

    def __truediv__(self, other):
        """
        Wandlet die Zahl in einen Bruch um und dividiert durch den Bruch
        Ueberpruft ob die Zahl nicht Null ist
        :param int other: Int, in dem die Zahl steht
        :return: Liefert das Ergebnis zurueck
        """
        if other == 0:
            raise ZeroDivisionError
        return self / Bruch(other)

    def __itruediv__(self, other):
        """
        Wandlet die Zahl in einen Bruch um und dividiert durch den Bruch
        Ueberpruft ob die Zahl ein String ist
        :param int other: Int, in dem die Zahl steht
        :return: Liefert das Ergebnis zurueck
        """
        if isinstance(other, str):
            raise TypeError
        return self / other

    def __rtruediv__(self, other):
        """
        Ueberpruft ob die Zahl Null ist und ob die Zahl eine float Zahl ist
        :param int other: Int, in dem die Zahl steht
        """
        if other == 0  or self == 0:
            raise  ZeroDivisionError
        if isinstance(other, float):
            raise TypeError

    def __rmul__(self, other):
        """
        Multiplizert eine Zahl mit dem Bruch
        :param int other: Int, in dem die Zahl steht
        :return: Liefert das Ergebnis zurueck
        """
        return self * other

    def __imul__(self, other):
        """
        Multiplizert eine Zahl mit dem Bruch
        Ueberpruft ob die Zahl ein String ist
        :param int other: Int, in dem die Zahl steht
        :return: Liefert das Ergebnis zurueck
        """
        if isinstance(other, str):
            raise TypeError
        return self * other

    def __eq__(self, other):
        """
        Ueberprueft ob der Bruch als Float gleich gross ist wie other als Float
        :param int other: Int, in dem die Zahl steht
        :return: Ture oder False
        """
        return float(self) == float(other)

    def __ge__(self, other):
        """
        Ueberprueft ob der Bruch als Float gleich gross oder grosser ist wie other als Float
        :param int other: Int, in dem die Zahl steht
        :return: Ture oder False
        """
        return float(self) >= float(other)

    def __gt__(self, other):
        """
        Ueberprueft ob der Bruch als Float grosser ist wie other als Float
        :param int other: Int, in dem die Zahl steht
        :return: Ture oder False
        """
        return float(self) > float(other)

    def __le__(self, other):
        """
        Ueberprueft ob der Bruch als Float kleiner oder gleich gross ist wie other als Float
        :param int other: Int, in dem die Zahl steht
        :return: Ture oder False
        """
        return float(self) <= float(other)

    def __lt__(self, other):
        """
        Ueberprueft ob der Bruch als Float kleiner ist wie other als Float
        :param int other: Int, in dem die Zahl steht
        :return: Ture oder False
        """
        return float(self) < float(other)

    def __ne__(self, other):
        """
        Ueberprueft ob der Bruch als Float nicht so gross ist wie other als Float
        :param int other: Int, in dem die Zahl steht
        :return: Ture oder False
        """
        return float(self) != float(other)