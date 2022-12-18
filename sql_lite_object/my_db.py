import sqlite3
from tkinter import *


class DataBase:
    win = Tk()

    def __init__(self, name):
        self.name = name

    def create(self, columns):
        """

        :param columns: listed tuples of (name_of_column, type_of_var)
        :return:
        """
        # if type(columns) is not list:
        #     return "wrong type of argument, a list of tuples is needed"
        # if ".db" not in self.name:
        #     db_name = f"{self.name}.db"
        # else:
        #     db_name = self.name
        db_name = self.name
        connection = sqlite3.connect(db_name)
        cursor = connection.cursor()

        quarry = f"CREATE TABLE {db_name} ("

        x = 0
        for element in columns:
            print(element)
            quarry += element
            if element != columns[-1]:
                quarry += ", "

            x += 1

        quarry = f"{quarry})"

        print(quarry)
        cursor.execute(quarry)
        connection.commit()
        connection.close()

    win.mainloop()


if __name__ == "main":
    data_col = ["ID integer", "nombre text", "nombrete text", "email text"]
    db = DataBase("jalamanguines.db")
    db.create(data_col)
