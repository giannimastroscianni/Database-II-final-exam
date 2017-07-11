# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
import models
import traceback


def index(request):
    context_dict = {'string': "Benvenuto!"}
    return render(request, 'esami/index.html', context=context_dict)


def get_insegnamenti(request):
    dic = {}
    try:
        dao = models.Dao()
        insegnamenti = dao.get_insegnamenti()
        dic['insegnamenti'] = insegnamenti
    except:
        traceback.print_exc()
    return render(request, 'esami/get_insegnamenti.html', context=dic)


def insert_insegnamento(request):
    dic = {}
    try:
        dao = models.Dao()
        if request.method == "POST":
            codice = request.POST.get('codice')
            nome = request.POST.get('nome')
            dic['message'] = dao.insert_insegnamento(codice, nome)
    except:
        traceback.print_exc()
    return render(request, 'esami/insert_insegnamento.html', context=dic)


def get_figure(request):
    dic = {}
    try:
        dao = models.Dao()
        figure = dao.get_figure()
        dic['figure'] = figure
    except:
        traceback.print_exc()
    return render(request, 'esami/get_figure.html', context=dic)


def insert_figura(request):
    dic = {}
    try:
        dao = models.Dao()
        if request.method == "POST":
            descrizione = request.POST.get('descrizione')
            dic['message'] = dao.insert_figura(descrizione)
    except:
        traceback.print_exc()
    return render(request, 'esami/insert_figura.html', context=dic)


def get_domande(request):
    dic = {}
    try:
        dao = models.Dao()
        domande = dao.get_domande()
        dic['domande'] = domande
    except:
        traceback.print_exc()
    return render(request, 'esami/get_domande.html', context=dic)


def get_domande_chiuse(request):
    dic = {}
    try:
        dao = models.Dao()
        domande_chiuse = dao.get_domande_chiuse()
        dic['domande_chiuse'] = domande_chiuse
    except:
        traceback.print_exc()
    return render(request, 'esami/get_domande_chiuse.html', context=dic)


def get_domande_aperte(request):
    dic = {}
    try:
        dao = models.Dao()
        domande_aperte = dao.get_domande_aperte()
        dic['domande_aperte'] = domande_aperte
    except:
        traceback.print_exc()
    return render(request, 'esami/get_domande_aperte.html', context=dic)


def insert_chiusa(request):
    dic = {}
    try:
        dao = models.Dao()
        if request.method == "POST":
            testo = request.POST.get('testo')
            punteggio = request.POST.get('punteggio')
            figure = request.POST.get('figure')
            risposte = request.POST.get('risposte')
            dic['message'] = dao.insert_chiusa(testo, punteggio, figure, risposte)
    except:
        traceback.print_exc()
    return render(request, 'esami/insert_chiusa.html', context=dic)


def insert_aperta(request):
    dic = {}
    try:
        dao = models.Dao()
        if request.method == "POST":
            testo = request.POST.get('testo')
            punteggio = request.POST.get('punteggio')
            figure = request.POST.get('figure')
            dic['message'] = dao.insert_aperta(testo, punteggio, figure)
    except:
        traceback.print_exc()
    return render(request, 'esami/insert_aperta.html', context=dic)


def get_compiti(request):
    dic = {}
    try:
        dao = models.Dao()
        compiti = dao.get_compiti()
        dic['compiti'] = compiti
    except:
        traceback.print_exc()
    return render(request, 'esami/get_compiti.html', context=dic)


def insert_compito(request):
    dic = {}
    try:
        dao = models.Dao()
        insegnamenti = dao.get_insegnamenti()
        dic['insegnamenti'] = insegnamenti
        if request.method == "POST":
            docente = request.POST.get('docente')
            insegnamento = request.POST.get('insegnamento')
            data = request.POST.get('data')
            numDomande = request.POST.get('numDomande')
            domande = request.POST.get('domande')
            dic['message'] = dao.insert_compito(docente, insegnamento, data, numDomande, domande)
    except:
        traceback.print_exc()
    return render(request, 'esami/insert_compito.html', context=dic)


def get_studenti(request):
    dic = {}
    try:
        dao = models.Dao()
        studenti = dao.get_studenti()
        dic['studenti'] = studenti
    except:
        traceback.print_exc()
    return render(request, 'esami/get_studenti.html', context=dic)


def insert_studente(request):
    dic = {}
    try:
        dao = models.Dao()
        if request.method == "POST":
            matricola = request.POST.get('matricola')
            cognome = request.POST.get('cognome')
            dic['message'] = dao.insert_studente(matricola, cognome)
    except:
        traceback.print_exc()
    return render(request, 'esami/insert_studente.html', context=dic)


def get_esami(request):
    dic = {}
    try:
        dao = models.Dao()
        esami = dao.get_esami()
        dic['esami'] = esami
    except:
        traceback.print_exc()
    return render(request, 'esami/get_esami.html', context=dic)


def insert_esame(request):
    dic = {}
    try:
        dao = models.Dao()
        studenti = dao.get_studenti()
        compiti = dao.get_distinct_compiti()
        dic['studenti'] = studenti
        dic['compiti'] = compiti
        if request.method == "POST":
            studente = request.POST.get('studente')
            compito = request.POST.get('compito')
            voto = request.POST.get('voto')
            dic['message'] = dao.insert_esame(studente, compito, voto)
    except:
        traceback.print_exc()
    return render(request, 'esami/insert_esame.html', context=dic)


def get_prove(request):
    dic = {}
    try:
        dao = models.Dao()
        prove = dao.get_prove()
        dic['prove'] = prove
    except:
        traceback.print_exc()
    return render(request, 'esami/get_prove.html', context=dic)


def insert_prova(request):
    dic = {}
    try:
        dao = models.Dao()
        studenti = dao.get_studenti()
        compiti = dao.get_distinct_compiti()
        dic['studenti'] = studenti
        dic['compiti'] = compiti
        if request.method == "POST":
            studente = request.POST.get('studente')
            compito = request.POST.get('compito')
            domanda = request.POST.get('domanda')
            chiusa = request.POST.get('chiusa')
            aperta = request.POST.get('aperta')
            dic['message'] = dao.insert_prova(studente, compito, domanda, chiusa, aperta)
    except:
        traceback.print_exc()
    return render(request, 'esami/insert_prova.html', context=dic)


def valuta_prova(request):
    dic = {}
    try:
        dao = models.Dao()
        prove = dao.get_prove_da_valutare()
        dic['prove'] = prove
        if request.method == "POST":
            id = request.POST.get('id')
            voto = request.POST.get('voto')
            dic['message'] = dao.valuta_prova(id, voto)
    except:
        traceback.print_exc()
    return render(request, 'esami/valuta_prova.html', context=dic)


def scegli_studente(request):
    dic = {}
    try:
        dao = models.Dao()
        studenti = dao.get_studenti()
        dic['studenti'] = studenti
        if request.method == "POST":
            studente = request.POST.get('studente')
    except:
        traceback.print_exc()
    return render(request, 'esami/scegli_studente.html', context=dic)


def vedi_esami(request):
    dic = {}
    try:
        dao = models.Dao()
        if request.method == "POST":
            studente = request.POST.get('studente')
            esami = dao.vedi_esami(studente)
            dic['esami'] = esami
    except:
        traceback.print_exc()
    return render(request, 'esami/vedi_esami.html', context=dic)
