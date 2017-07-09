# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import traceback


class Insegnamento:
    def __init__(self, codice, nome, numsostenuti, numsuperati):
        self.codice = codice
        self.nome = nome
        self.numsostenuti = numsostenuti
        self.numsuperati = numsuperati

    def get_codice(self):
        return self.codice

    def get_nome(self):
        return self.nome

    def get_numsostenuti(self):
        return self.numsostenuti

    def get_numsuperati(self):
        return self.numsuperati


class Figura:
    def __init__(self, id, descrizione):
        self.id = id
        self.descrizione = descrizione

    def get_id(self):
        return self.id

    def get_descrizione(self):
        return self.descrizione


class Domanda:
    def __init__(self, id, testo, punteggio):
        self.id = id
        self.testo = testo
        self.punteggio = punteggio


    def get_id(self):
        return self.id

    def get_testo(self):
        return self.testo

    def get_punteggio(self):
        return self.punteggio

class DomandaChiusa(Domanda):
    def __init__(self, id, testo, punteggio, figure, risposte):
        self.id = id
        self.testo = testo
        self.punteggio = punteggio
        self.figure=figure
        self.risposte=risposte


    def get_figure(self):
        return self.figure

    def get_risposte(self):
        return self.risposte

class DomandaAperta(Domanda):
    def __init__(self, id, testo, punteggio, figure):
        self.id = id
        self.testo = testo
        self.punteggio = punteggio
        self.figure=figure


    def get_figure(self):
        return self.figure


class Dao:
    import cx_Oracle
    try:
        con = cx_Oracle.connect('gianni/gianni@localhost:1521/orcl')
    except:
        traceback.print_exc()

    """ __istanza = None

    def __init__(self):
        if Dao.__istanza:
            raise Dao.__istanza
        Dao.__istanza = self"""

    def get_insegnamenti(self):
        cursor = self.con.cursor()
        cursor.execute("select * from insegnamento order by codice")
        rows = cursor.fetchall()
        to_return = []
        for row in rows:
            to_return.append(Insegnamento(row[0], row[1], row[2], row[3]))
        cursor.close()
        return to_return

    def insert_insegnamento(self, codice, nome):
        try:
            cursor = self.con.cursor()
            query = "insert into insegnamento values('" + codice + "', '" + nome + "', 0, 0)"
            cursor.execute(query)
            cursor.close()
            self.con.commit()
            return "Insegnamento inserito"
        except:
            traceback.print_exc()
            return "ERRORE!"

    def get_figure(self):
        cursor = self.con.cursor()
        cursor.execute("select * from figura order by id")
        rows = cursor.fetchall()
        to_return = []
        for row in rows:
            to_return.append(Figura(row[0], row[1]))
        cursor.close()
        return to_return

    def insert_figura(self, descrizione):
        try:
            cursor = self.con.cursor()
            query = "insert into figura values(1, '" + descrizione + "')"
            cursor.execute(query)
            cursor.close()
            self.con.commit()
            return "Figura inserita"
        except:
            traceback.print_exc()
            return "ERRORE!"

    def get_domande(self):
        cursor = self.con.cursor()
        cursor.execute("select id, testo, punteggio from domanda order by id")
        rows = cursor.fetchall()
        to_return = []
        for row in rows:
            to_return.append(Domanda(row[0], row[1], row[2]))
        cursor.close()
        return to_return

    def get_domande_chiuse(self):
        cursor = self.con.cursor()
        cursor.execute("select d.id, d.testo, d.punteggio, ff.figura.id, rr.risposte.testo from domanda d, table(d.figure) ff, table(d.risposte) rr where value(d) is of type (domanda_chiusaty) order by d.id")
        rows = cursor.fetchall()
        to_return = []
        for row in rows:
            to_return.append(DomandaChiusa(row[0], row[1], row[2], row[3], row[4]))
        cursor.close()
        return to_return

    def get_domande_aperte(self):
        cursor = self.con.cursor()
        cursor.execute("select d.id, d.testo, d.punteggio, ff.figura.id from domanda d, table(d.figure) ff where value(d) is of type (domanda_apertaty) order by d.id")
        rows = cursor.fetchall()
        to_return = []
        for row in rows:
            to_return.append(DomandaAperta(row[0], row[1], row[2], row[3]))
        cursor.close()
        return to_return
