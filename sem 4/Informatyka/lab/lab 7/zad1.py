import mysql.connector

CON_DICT = {
    'host': '127.0.0.1',
    'database': 'lab6',
    'user': 'root',
    'password': 'admin',
    'raise_on_warnings': True
}


class Car:
    def __init__(self, car_id: int, kolor: str,
                 marka: str, model: str, pojemnosc: str,
                 rocznik: int, owner_id: int):
        self.car_id = car_id
        self.kolor = kolor
        self.marka = marka
        self.model = model
        self.pojemnosc = pojemnosc
        self.rocznik = rocznik
        self.owner_id = owner_id

    @staticmethod
    def all(cur) -> list:
        query = f"SELECT * FROM cars"
        cur.execute(query)
        return [Car(car_id=i[0],
                    kolor=i[1],
                    marka=i[2],
                    model=i[3],
                    pojemnosc=i[4],
                    rocznik=i[5],
                    owner_id=i[6]) for i in cur]

    def save(self, con):
        cur = con.cursor()
        query = f"UPDATE cars SET " \
                f"car_id = {self.car_id}, " \
                f"kolor = '{self.kolor}', " \
                f"marka = '{self.marka}', " \
                f"model = '{self.model}', " \
                f"pojemnosc = '{self.pojemnosc}', " \
                f"rocznik = '{self.rocznik}', " \
                f"owner_id = '{self.owner_id}'" \
                f"WHERE (car_id = {self.car_id})"
        cur.execute(query)
        con.commit()
        cur.close()


class Owner:
    def __init__(self, owner_id: int,
                 imie: str, nazwisko: str,
                 pesel: str, kraj: str):
        self.owner_id = owner_id
        self.imie = imie
        self.nazwisko = nazwisko
        self.pesel = pesel
        self.kraj = kraj

    @staticmethod
    def all(cur) -> list:
        query = f"SELECT * FROM owners"
        cur.execute(query)
        return [Owner(owner_id=i[0],
                      imie=i[1],
                      nazwisko=i[2],
                      pesel=i[3],
                      kraj=i[4]) for i in cur]

    def save(self, con):
        cur = con.cursor()
        query = f"UPDATE owners SET " \
                f"owner_id = {self.owner_id}, " \
                f"imie = '{self.imie}', " \
                f"nazwisko = '{self.nazwisko}', " \
                f"pesel = '{self.pesel}', " \
                f"kraj = '{self.kraj}' " \
                f"WHERE (owner_id = {self.owner_id})"
        print(query)
        cur.execute(query)
        con.commit()
        cur.close()


con = mysql.connector.connect(**CON_DICT)
cursor = con.cursor()

a = Owner.all(cursor)
print(a)
a[0].imie = "test"
a[0].save(con)
cursor.close()
con.close()
