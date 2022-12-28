import baza
import sqlite3
import os
import hashlib

conn = sqlite3.connect('spletna_trgovina.db')
baza.ustvari_bazo_ce_ne_obstaja(conn)
conn.execute('PRAGMA foreign_keys = ON')

dir = os.path.dirname(os.path.realpath(__file__))
db_path = os.path.join(dir, "spletna_trgovina.db")

class Uporabnik:
    
    @staticmethod
    def registriraj_če_ne_obstaja(username, password, pwd_repeat, email, birthday, address):
        
        with sqlite3.connect(db_path) as conn:
            c = conn.cursor()

            sql = "SELECT uidUporabniki FROM uporabniki WHERE uidUporabniki=?"
            c.execute(sql, [username])
            result_check= len(c.fetchall())

            if password != pwd_repeat:
                return "<p> Vneseni gesli se ne ujemata </p>"
            elif result_check > 0:
                return "<p> Uporabniško ime že obstaja </p>"
            else:
                sql2 = "INSERT INTO uporabniki(uidUporabniki, pwdUporabniki, emailUporabniki, rojstvoUporabniki, naslovUporabniki) VALUES (?, ?, ?, ?, ?)"
                salt = "5gz"
                password_salt = password + salt
                password = hashlib.md5(password_salt.encode()).hexdigest()
                c.execute(sql2, [username, password, email, birthday, address])
                conn.commit()

    @staticmethod
    def prijavi(username, password):
        with sqlite3.connect(db_path) as conn:
            c = conn.cursor()

            sql = "SELECT uidUporabniki, pwdUporabniki FROM uporabniki WHERE uidUporabniki = ?"
            c.execute(sql, [username])
            result = c.fetchall()
            result_check = len(result)
            if result_check == 0:
                return '<p>Uporabniško ime ali geslo ni pravilno</p>'
            else:
                salt = "5gz"
                password_salt = password + salt
                password = hashlib.md5(password_salt.encode()).hexdigest()
                if result[0][0] == username and result[0][1] == password:
                    return True
                else:
                    return False
