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
    def all(con) -> list:
        cur = con.cursor()
        query = f"SELECT * FROM owners"
        cur.execute(query)
        ret_val = [Owner(owner_id=i[0],
                         imie=i[1],
                         nazwisko=i[2],
                         pesel=i[3],
                         kraj=i[4]) for i in cur]
        cur.close()
        return ret_val

    def save(self, con):
        cur = con.cursor()
        query = f"SELECT * FROM owners WHERE owner_id={self.owner_id}"
        cur.execute(query)
        if cur.fetchone() is None:  # add new owner if not exist
            query = f"INSERT INTO owners (owner_id, imie, nazwisko, pesel, kraj) " \
                    f"VALUES ({self.owner_id}, '{self.imie}', '{self.nazwisko}', " \
                    f"'{self.pesel}', '{self.kraj}')"
            cur.reset()
            cur.execute(query)
            con.commit()
            cur.close()
            return

        # if exists update
        query = f"UPDATE owners SET " \
                f"owner_id = {self.owner_id}, " \
                f"imie = '{self.imie}', " \
                f"nazwisko = '{self.nazwisko}', " \
                f"pesel = '{self.pesel}', " \
                f"kraj = '{self.kraj}' " \
                f"WHERE (owner_id = {self.owner_id})"
        cur.reset()
        cur.execute(query)
        con.commit()
        cur.close()
