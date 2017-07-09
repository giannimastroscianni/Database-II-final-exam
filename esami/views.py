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
