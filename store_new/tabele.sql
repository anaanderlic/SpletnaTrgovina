CREATE TABLE `izdelek`(
  `idIzdelek` INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
  `naziv` TEXT NOT NULL,
  `cena` REAL NOT NULL,
  `kolicina` INTEGER NOT NULL,
  `kategorija` TEXT NOT NULL,
  `slika` TEXT NOT NULL,
  `akcija` TEXT,
  `ocena` REAL,
  `opis` TEXT 
);

CREATE TABLE `uporabnik`(
  `idUporabnik` INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
  `email` TEXT NOT NULL,
  `geslo` TEXT NOT NULL,
  `ime` TEXT NOT NULL,
  `priimek` TEXT NOT NULL,
  `datumRojstva` TEXT NOT NULL,
  `admin` TEXT DEFAULT 'N'
);

CREATE TABLE `kosarica`(
  `idKosarica` INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
   idUporabnik INTEGER REFERENCES uporabnik(idUporabnik)
);

CREATE TABLE `narocilo`(
  `idNarocilo` INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
  `ulica` TEXT NOT NULL,
  `postnaStevilka` INTEGER NOT NULL,
  `kraj` TEXT NOT NULL,
  `telStevilka` TEXT,
  `datum` TEXT NOT NULL,
   idUporabnik INTEGER REFERENCES uporabnik(idUporabnik),
   idKosarica INTEGER REFERENCES kosarica(idKosarica)
);

CREATE TABLE `ocenaIzdelka`(
  `idOcena` INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
  `ocena` INTEGER NOT NULL,
   idIzdelek INTEGER REFERENCES izdelek(idIzdelek)
);

CREATE TABLE `izdKosarica`(
   `kolicina` INTEGER,
   idKosarica INTEGER REFERENCES kosarica(idKosarica),
   idIzdelek INTEGER REFERENCES izdelek(idIzdelek)
);

CREATE TABLE `narIzdelek`(
   idNarocilo INTEGER REFERENCES narocilo(idNarocilo),
   idIzdelek INTEGER REFERENCES izdelek(idIzdelek),
   PRIMARY KEY (idNarocilo, idIzdelek)
);

-->Dodaj še stavke za dodajanje stvari v tabele
