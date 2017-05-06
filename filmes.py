# -*- coding: utf-8 -*-
""" Este script verifica filmes cujo titulo
    tenham VP ou (V.P.) e envia um twitt

"""
import requests
from bs4 import BeautifulSoup
import twitter
import re
import datetime


URL_LISTA_CANAIS = "http://services.sapo.pt/EPG/GetChannelList"
URL_CANAL = "http://services.sapo.pt/EPG/GetChannelByDateInterval?"\
            "channelSigla={canal}&startDate={DATA_INI}+20%3A00%3A00&"\
            "endDate={DATA_FIN}+21%3A00%3A00"
WORDS = ["VP", "(V.P.)"]
DATA_INI = datetime.datetime.now().date()
DATA_FIN = datetime.datetime.now().date() + datetime.timedelta(days=1)


# sacar lista de canais
result = requests.get(URL_LISTA_CANAIS)
soup = BeautifulSoup(result.text, 'lxml')
canais = []
for tag in soup.findChildren():
    if tag.name == 'sigla':
        canais.append(tag.text)

# Pesquisar em todos os canais
for canal in canais:
    if canal.endswith("HD"): continue
    result = requests.get(URL_CANAL.replace("{canal}", canal)\
    .replace("{DATA_INI}", str(DATA_INI)).replace("{DATA_FIN}", \
    str(DATA_FIN)))
    soup = BeautifulSoup(result.text, 'lxml')
    for program_tag in soup.find_all('program'):
        tit = ""
        for line in program_tag:
            if str(line).startswith("<title>"): tit = str(line)
            if str(line).startswith("<starttime>"): dt_ini = str(line)
            if str(line).startswith("<channelname>"): ch_name = str(line)
        if any(sub in tit for sub in WORDS):
            tit = re.sub('<[^>]+>', '', tit)
            dt_ini = re.sub('<[^>]+>', '', dt_ini)
            ch_name = re.sub('<[^>]+>', '', ch_name)
            msg = (tit+" no canal "+ch_name+" no dia "+dt_ini)
            twitter.send_msg(msg)
