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
