class SpletnaTrgovina:
    def __init__(self, conn):
        """
        Konstruktor razreda.
        """
        self.conn = conn

    def ustvari_in_uvozi(self):
        with open("tabele.sql", encoding="UTF-8") as f:
            sql = f.read()
        self.conn.executescript(sql)

def ustvari_bazo(conn):
    """
    Izvede ustvarjanje baze.
    """
    spletna = pripravi_tabele(conn)
    spletna.ustvari_in_uvozi()

def pripravi_tabele(conn):
    """
    Pripravi objekte za tabele.
    """
    return SpletnaTrgovina(conn)

def ustvari_bazo_ce_ne_obstaja(conn):
    """
    Ustvari bazo, če ta še ne obstaja.
    """
    with conn:
        cur = conn.execute("SELECT COUNT(*) FROM sqlite_master")
        # sqlite_master je "sistemska" tabela, kjer so podatki o
        # tabelah, ki jih baza vsebuje
        if cur.fetchone() == (0, ): # v bazi ni tabele
            ustvari_bazo(conn)