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
    def all(con) -> list:
        query = f"SELECT * FROM cars"
        cur = con.cursor()
        cur.execute(query)
        ret_val = [Car(car_id=i[0],
                       kolor=i[1],
                       marka=i[2],
                       model=i[3],
                       pojemnosc=i[4],
                       rocznik=i[5],
                       owner_id=i[6]) for i in cur]
        cur.close()
        return ret_val

    def save(self, con):
        cur = con.cursor()
        query = f"SELECT * FROM cars WHERE car_id={self.car_id}"
        cur.execute(query)
        if cur.fetchone() is None:  # add new owner if not exist
            query = f"INSERT INTO cars (car_id, kolor, marka, model, pojemnosc, " \
                    f"rocznik, owner_id) " \
                    f"VALUES ({self.car_id}, '{self.kolor}', '{self.marka}', " \
                    f"'{self.model}', '{self.pojemnosc}', {self.rocznik}, {self.owner_id})"
            cur.reset()
            cur.execute(query)
            con.commit()
            cur.close()
            return

        query = f"UPDATE cars SET " \
                f"car_id = {self.car_id}, " \
                f"kolor = '{self.kolor}', " \
                f"marka = '{self.marka}', " \
                f"model = '{self.model}', " \
                f"pojemnosc = '{self.pojemnosc}', " \
                f"rocznik = {self.rocznik}, " \
                f"owner_id = {self.owner_id} " \
                f"WHERE (car_id = {self.car_id})"
        cur.reset()
        cur.execute(query)
        con.commit()
        cur.close()
