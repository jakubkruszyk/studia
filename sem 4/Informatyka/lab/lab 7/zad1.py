import mysql.connector
from car import Car
from owner import Owner


CON_DICT = {
    'host': '127.0.0.1',
    'database': 'lab6',
    'user': 'root',
    'password': 'admin',
    'raise_on_warnings': True
}


con = mysql.connector.connect(**CON_DICT)
cursor = con.cursor()

a = Owner.all(con)
a[0].imie = "test"
a[0].save(con)
b = Owner(3, "Jan", "Michalak", "0129812", "UK")  # test dodawania, zmienic id za kazdym razem
b.save(con)

c = Car.all(con)
c[0].kolor = "czerwony"
c[0].save(con)

d = Car(1, "biały", "Toyota", "Corolla", "1.6", 2018, 3)
d.save(con)

cursor.close()
con.close()
