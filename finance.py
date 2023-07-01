import sqlite3
import matplotlib.pyplot as plt
import plotly.express as px
import os
from datetime import date, datetime

# Global variables
running: bool = True


def main() -> None:
    global running
    conn: sqlite3.Connection = sqlite3.connect('database.db')
    cur = conn.cursor()
    while (running):
        print('1-Add\n2-Consult\n3-Exit\n')
        option:int = int(input("Choose an option:\n"))

        try:
            cur.execute("CREATE TABLE Compras(name VARCHAR(30), price DECIMAL, date DATE);")
        except:
            pass

        
        match option:
            case 1:
                print('Caso 1')
                name: str = input()
                price: float = input()
                #
                date: str = input()
                date: datetime.datetime = str(datetime.strptime(date, '%d/%m/%Y')).split(' ')[0]
                print(date)
                cur.execute(f"INSERT INTO Compras(name, price, date) \
                            VALUES(?, ?, ?);",[name, price, date])
            case 2:
                option_2:int = int(input('2.1-Per Item Name\n2.2-Per Month'))
                match option_2:
                    case 1:
                        name_search: str = input()
                        cur.execute(f"SELECT * FROM Compras WHERE name=?;",[name_search])
                        print(cur.fetchall()[0])
                    case 2:
                        date_search: str = input()
                        _, mt, yr = date_search.split('/')
                        cur.execute(f"SELECT * FROM Compras WHERE SUBSTR()")
                        print(cur.fetchall())
            case 3:
                running=False
            case _:
                print('')
    conn.commit()
    conn.close()




if __name__=="__main__":
    main()
