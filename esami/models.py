# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import traceback
from datetime import datetime as dt


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
        self.figure = figure
        self.risposte = risposte

    def get_figure(self):
        return self.figure

    def get_risposte(self):
        return self.risposte


class DomandaAperta(Domanda):
    def __init__(self, id, testo, punteggio, figure):
        self.id = id
        self.testo = testo
        self.punteggio = punteggio
        self.figure = figure

    def get_figure(self):
        return self.figure


class Compito:
    def __init__(self, id, docente, insegnamento, data, numDomande, domande):
        self.id = id
        self.docente = docente
        self.insegnamento = insegnamento
        self.data = data
        self.numDomande = numDomande
        self.domande = domande

    def get_id(self):
        return self.id

    def get_docente(self):
        return self.docente

    def get_insegnamento(self):
        return self.insegnamento

    def get_data(self):
        return self.data

    def get_num_domande(self):
        return self.numDomande

    def get_domande(self):
        return self.domande


class Studente:
    def __init__(self, matricola, cognome, numEsami):
        self.matricola = matricola
        self.cognome = cognome
        self.numEsami = numEsami

    def get_matricola(self):
        return self.matricola

    def get_cognome(self):
        return self.cognome

    def get_numEsami(self):
        return self.numEsami


class Esame:
    def __init__(self, id, studente, compito, voto):
        self.id = id
        self.studente = studente
        self.compito = compito
        self.voto = voto

    def get_id(self):
        return self.id

    def get_studente(self):
        return self.studente

    def get_compito(self):
        return self.compito

    def get_voto(self):
        return self.voto


class Prova:
    def __init__(self, id, studente, compito, domanda, risposta, valutazione):
        self.id = id
        self.studente = studente
        self.compito = compito
        self.domanda = domanda
        self.risposta = risposta
        self.valutazione = valutazione

    def get_id(self):
        return self.id

    def get_studente(self):
        return self.studente

    def get_compito(self):
        return self.compito

    def get_domanda(self):
        return self.domanda

    def get_risposta(self):
        return self.risposta

    def get_valutazione(self):
        return self.valutazione


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
        cursor.execute(
            "select d.id, d.testo, d.punteggio, ff.figura.id, rr.risposte.testo from domanda d, table(d.figure) ff, table(d.risposte) rr where value(d) is of type (domanda_chiusaty) order by d.id")
        rows = cursor.fetchall()
        to_return = []
        for row in rows:
            to_return.append(DomandaChiusa(row[0], row[1], row[2], row[3], row[4]))
        cursor.close()
        return to_return

    def get_domande_aperte(self):
        cursor = self.con.cursor()
        cursor.execute(
            "select d.id, d.testo, d.punteggio, ff.figura.id from domanda d, table(d.figure) ff where value(d) is of type (domanda_apertaty) order by d.id")
        rows = cursor.fetchall()
        to_return = []
        for row in rows:
            to_return.append(DomandaAperta(row[0], row[1], row[2], row[3]))
        cursor.close()
        return to_return

    def insert_chiusa(self, testo, punteggio, figure, risposte):
        risp = risposte.split(',')
        for i in range(len(risp)):
            pos = risp[i].index('X')
            text = risp[i][:pos]
            if not self._check_esiste_risposta(text):
                try:
                    cursor = self.con.cursor()
                    query = "insert into risposta select risposta_chiusaty('" + text + "') from dual"
                    cursor.execute(query)
                    cursor.close()
                    self.con.commit()
                except:
                    traceback.print_exc()
        try:
            cursor = self.con.cursor()
            query = "insert into domanda select domanda_chiusaty('" + testo + "', " + punteggio + ", ref_figurent("
            figure = figure.split()
            if len(figure) > 0:
                for i in range(len(figure)):
                    sub_query = "ref_figurety((select ref(f) from figura f where f.id = " + figure[i] + "))"
                    query += sub_query
                    if i != (len(figure) - 1):
                        query += ","
                query += "), "
            else:
                query += "ref_figurety((select ref(f) from figura f where f.id=1))),"
            query += "ref_rispostent("
            risposte = risposte.split()
            for j in range(len(risposte)):
                pos = risposte[j].index('X')
                testo = risposte[j][:pos]
                punt = risposte[j][pos + 1:]
                new_sub_query = "ref_rispostety((select treat(ref(r) as ref risposta_chiusaty) from risposta r where r.testo='" + testo + "')," + punt + ")"
                query += new_sub_query
                if j != (len(risp) - 1):
                    query += ","

            query += "))from dual"
            print query
            cursor.execute(query)
            cursor.close()
            self.con.commit()
            return "Domanda chiusa inserita"
        except:
            traceback.print_exc()
            return "ERRORE!"

    def _check_esiste_risposta(self, text):
        bool = False;
        cursor = self.con.cursor()
        query = "select * from risposta r where r.testo='" + text + "'"
        cursor.execute(query)
        rows = cursor.fetchall()
        if len(rows) > 0:
            bool = True
        cursor.close()
        return bool

    def insert_aperta(self, testo, punteggio, figure):
        try:
            cursor = self.con.cursor()
            query = "insert into domanda select domanda_apertaty('" + testo + "', " + punteggio + ", ref_figurent(ref_figurety((select ref(f) from figura f where f.id="
            figu = figure.split()
            if len(figu) == 0:
                query += "-1)))) from dual"
            else:
                query += "" + figure + ")))) from dual"
            print query
            cursor.execute(query)
            cursor.close()
            self.con.commit()
            return "Domanda aperta inserita"
        except:
            traceback.print_exc()
            return "ERRORE!"

    def get_compiti(self):
        cursor = self.con.cursor()
        cursor.execute(
            "select c.id, c.docente, deref(c.insegnamento).nome, c.data, c.num_domande, dd.domanda.testo from compito c, table(c.domande) dd order by c.id")
        rows = cursor.fetchall()
        to_return = []
        for row in rows:
            dat = row[3].strftime("%Y/%m/%d")
            date = dt.strptime(dat, "%Y/%m/%d").timetuple()
            d = (date[0], date[1], date[2])
            to_return.append(Compito(row[0], row[1], row[2], d, row[4], row[5]))
        cursor.close()
        return to_return

    def insert_compito(self, docente, insegnamento, data, numDomande, domande):
        try:
            cursor = self.con.cursor()
            query = "insert into compito values(1, '" + docente + "', (select ref(i) from insegnamento i where i.nome='" + insegnamento + "'), to_date('" + data + "', 'yyyy-mm-dd'), " + numDomande + ", ref_domandent("
            domande = domande.split()
            for i in range(len(domande)):
                sub_query = "ref_domandety((select ref(d) from domanda d where d.id = " + domande[i] + "))"
                query += sub_query
                if i != (len(domande) - 1):
                    query += ","
            query += "))"
            cursor.execute(query)
            cursor.close()
            self.con.commit()
            return "Compito inserito"
        except:
            traceback.print_exc()
            return "ERRORE!"

    def get_studenti(self):
        cursor = self.con.cursor()
        cursor.execute("select * from studente order by matricola")
        rows = cursor.fetchall()
        to_return = []
        for row in rows:
            to_return.append(Studente(row[0], row[1], row[2]))
        cursor.close()
        return to_return

    def insert_studente(self, matricola, cognome):
        try:
            cursor = self.con.cursor()
            query = "insert into studente values(" + matricola + ", '" + cognome + "', 0)"
            cursor.execute(query)
            cursor.close()
            self.con.commit()
            return "Studente inserito"
        except:
            traceback.print_exc()
            return "ERRORE!"

    def get_esami(self):
        cursor = self.con.cursor()
        cursor.execute(
            "select id, deref(studente).cognome, deref(compito).id, valutazione from esami_sostenuti order by id")
        rows = cursor.fetchall()
        to_return = []
        for row in rows:
            to_return.append(Esame(row[0], row[1], row[2], row[3]))
        cursor.close()
        return to_return

    def insert_esame(self, studente, compito, voto):
        try:
            cursor = self.con.cursor()
            query = "insert into esami_sostenuti values(1, (select ref(s) from studente s where s.cognome='" + studente + "'), (select ref(c) from compito c where c.id=" + compito + "), " + voto + ")"
            cursor.execute(query)
            cursor.close()
            self.con.commit()
            return "Esame inserito"
        except:
            traceback.print_exc()
            return "ERRORE!"

    def get_prove(self):
        cursor = self.con.cursor()
        cursor.execute(
            "select id, deref(studente).cognome, deref(compito).id, deref(domanda).testo, deref(risposta).testo, valutazione from prova order by id")
        rows = cursor.fetchall()
        to_return = []
        for row in rows:
            to_return.append(Prova(row[0], row[1], row[2], row[3], row[4], row[5]))
        cursor.close()
        return to_return

    def insert_prova(self, studente, compito, domanda, chiusa, aperta):
        try:
            cursor = self.con.cursor()
            if aperta:
                _insert_risposta_aperta(aperta)
                query = "insert into prova values(1, (select ref(s) from studente s where s.cognome='" + studente + "'), (select ref(c) from compito c where c.id=" + compito + "), (select ref(d) from domanda d where d.id=" + domanda + "), (select ref(r) from risposta r where r.testo='" + aperta + "'), null)"
            else:
                query = "insert into prova values(1, (select ref(s) from studente s where s.cognome='" + studente + "'), (select ref(c) from compito c where c.id=" + compito + "), (select ref(d) from domanda d where d.id=" + domanda + "), (select ref(r) from risposta r where r.id=" + chiusa + "), null)"
            print query
            cursor.execute(query)
            cursor.close()
            self.con.commit()
            return "Prova inserita"
        except:
            traceback.print_exc()
            return "ERRORE!"

    def valuta_prova(self, id, voto):
        try:
            cursor = self.con.cursor()
            query = "update prova set valutazione=" + voto + " where id=" + id
            cursor.execute(query)
            cursor.close()
            self.con.commit()
            return "Valutazione inserita"
        except:
            traceback.print_exc()
            return "ERRORE!"

    def get_distinct_compiti(self):
        cursor = self.con.cursor()
        cursor.execute(
            "select id from compito order by id")
        rows = cursor.fetchall()
        to_return = []
        for row in rows:
            to_return.append(row[0])
        cursor.close()
        return to_return

    def get_prove_da_valutare(self):
        cursor = self.con.cursor()
        cursor.execute(
            "select id from prova where deref(prova.domanda).tipo='domanda_aperta'")
        rows = cursor.fetchall()
        to_return = []
        for row in rows:
            to_return.append(row[0])
        cursor.close()
        return to_return


def _insert_risposta_aperta(risp):
    dao = Dao()
    cursor = dao.con.cursor()
    query = "insert into risposta select risposta_apertaty('" + risp + "') from dual"
    print query
    cursor.execute(query)
    cursor.close()
    dao.con.commit()

