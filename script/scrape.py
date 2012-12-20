#!/usr/bin/env python
# encoding: utf-8
"""
untitled.py

Created by Michael Porath on 2011-02-23.
Copyright (c) 2011 __MyCompanyName__. All rights reserved.
"""

from pyquery import PyQuery as pq
from lxml import etree
import urllib
import re
import json

# 2003/04
# matches=[{"match_id":96,"date":"16.07.2003","team_home":12,"team_away":1,"goals_home":2,"goals_away":1},
# {"match_id":95,"date":"19.07.2003","team_home":1,"team_away":41,"goals_home":0,"goals_away":1},
# {"match_id":94,"date":"26.07.2003","team_home":10,"team_away":1,"goals_home":2,"goals_away":1},
# {"match_id":93,"date":"02.08.2003","team_home":1,"team_away":13,"goals_home":2,"goals_away":2},
# {"match_id":92,"date":"08.08.2003","team_home":15,"team_away":1,"goals_home":2,"goals_away":1},
# {"match_id":91,"date":"17.08.2003","team_home":15,"team_away":1,"goals_home":1,"goals_away":0},
# {"match_id":90,"date":"23.08.2003","team_home":1,"team_away":41,"goals_home":3,"goals_away":1},
# {"match_id":89,"date":"30.08.2003","team_home":18,"team_away":1,"goals_home":3,"goals_away":3},
# {"match_id":88,"date":"03.09.2003","team_home":1,"team_away":11,"goals_home":4,"goals_away":0},
# {"match_id":87,"date":"14.09.2003","team_home":1,"team_away":12,"goals_home":0,"goals_away":1},
# {"match_id":85,"date":"28.09.2003","team_home":41,"team_away":1,"goals_home":3,"goals_away":1},
# {"match_id":84,"date":"05.10.2003","team_home":13,"team_away":1,"goals_home":2,"goals_away":1},
# {"match_id":83,"date":"15.10.2003","team_home":1,"team_away":10,"goals_home":0,"goals_away":2},
# {"match_id":81,"date":"26.10.2003","team_home":1,"team_away":15,"goals_home":3,"goals_away":1},
# {"match_id":80,"date":"29.10.2003","team_home":1,"team_away":15,"goals_home":0,"goals_away":2},
# {"match_id":79,"date":"02.11.2003","team_home":41,"team_away":1,"goals_home":2,"goals_away":1},
# {"match_id":76,"date":"23.11.2003","team_home":1,"team_away":18,"goals_home":4,"goals_away":2},
# {"match_id":75,"date":"30.11.2003","team_home":11,"team_away":1,"goals_home":2,"goals_away":0},
# {"match_id":73,"date":"15.02.2004","team_home":18,"team_away":1,"goals_home":2,"goals_away":4},
# {"match_id":72,"date":"22.02.2004","team_home":1,"team_away":41,"goals_home":2,"goals_away":0},
# {"match_id":71,"date":"29.02.2004","team_home":10,"team_away":1,"goals_home":2,"goals_away":2},
# {"match_id":69,"date":"07.03.2004","team_home":1,"team_away":41,"goals_home":2,"goals_away":1},
# {"match_id":68,"date":"14.03.2004","team_home":15,"team_away":1,"goals_home":1,"goals_away":2},
# {"match_id":67,"date":"17.03.2004","team_home":1,"team_away":12,"goals_home":1,"goals_away":0},
# {"match_id":66,"date":"21.03.2004","team_home":13,"team_away":1,"goals_home":1,"goals_away":3},
# {"match_id":65,"date":"28.03.2004","team_home":1,"team_away":15,"goals_home":1,"goals_away":0},
# {"match_id":64,"date":"04.04.2004","team_home":11,"team_away":1,"goals_home":2,"goals_away":1},
# {"match_id":62,"date":"08.04.2004","team_home":1,"team_away":11,"goals_home":0,"goals_away":0},
# {"match_id":60,"date":"15.04.2004","team_home":15,"team_away":1,"goals_home":4,"goals_away":2},
# {"match_id":57,"date":"18.04.2004","team_home":1,"team_away":13,"goals_home":2,"goals_away":2},
# {"match_id":56,"date":"24.04.2004","team_home":12,"team_away":1,"goals_home":1,"goals_away":1},
# {"match_id":55,"date":"02.05.2004","team_home":1,"team_away":15,"goals_home":0,"goals_away":0},
# {"match_id":54,"date":"08.05.2004","team_home":41,"team_away":1,"goals_home":0,"goals_away":1},
# {"match_id":53,"date":"12.05.2004","team_home":1,"team_away":10,"goals_home":2,"goals_away":2},
# {"match_id":52,"date":"15.05.2004","team_home":41,"team_away":1,"goals_home":2,"goals_away":3},
# {"match_id":51,"date":"23.05.2004","team_home":1,"team_away":18,"goals_home":4,"goals_away":1}]

# 2005/06
matches=[
{"match_id": 2  , "date": "16.07.2005", "team_home": 12, "team_away": 1, "goals_home": 1, "goals_away": 3},
{"match_id": 1  , "date": "24.07.2005", "team_home": 1, "team_away": 13, "goals_home": 4, "goals_away": 2},
{"match_id": 3  , "date": "30.07.2005", "team_home": 11, "team_away": 1, "goals_home": 2, "goals_away": 1},
{"match_id": 4  , "date": "06.08.2005", "team_home": 1, "team_away": 10, "goals_home": 2, "goals_away": 2},
{"match_id": 5  , "date": "14.08.2005", "team_home": 1, "team_away": 15, "goals_home": 3, "goals_away": 2},
{"match_id": 7  , "date": "21.08.2005", "team_home": 9, "team_away": 1, "goals_home": 3, "goals_away": 1},
{"match_id": 16 , "date": "28.08.2005", "team_home": 1, "team_away": 14, "goals_home": 5, "goals_away": 0},
{"match_id": 58 , "date": "10.09.2005", "team_home": 16, "team_away": 1, "goals_home": 0, "goals_away": 2},
{"match_id": 78 , "date": "21.09.2005", "team_home": 17, "team_away": 1, "goals_home": 1, "goals_away": 1},
{"match_id": 97 , "date": "25.09.2005", "team_home": 1, "team_away": 12, "goals_home": 3, "goals_away": 0},
{"match_id": 99 , "date": "02.10.2005", "team_home": 13, "team_away": 1, "goals_home": 1, "goals_away": 0},
{"match_id": 139, "date": "16.10.2005", "team_home": 1, "team_away": 11, "goals_home": 2, "goals_away": 4},
{"match_id": 144, "date": "29.10.2005", "team_home": 10, "team_away": 1, "goals_home": 1, "goals_away": 6},
{"match_id": 150, "date": "06.11.2005", "team_home": 15, "team_away": 1, "goals_home": 3, "goals_away": 5},
{"match_id": 168, "date": "20.11.2005", "team_home": 1, "team_away": 9, "goals_home": 1, "goals_away": 1},
{"match_id": 176, "date": "27.11.2005", "team_home": 14, "team_away": 1, "goals_home": 0, "goals_away": 2},
{"match_id": 177, "date": "04.12.2005", "team_home": 1, "team_away": 16, "goals_home": 1, "goals_away": 1},
{"match_id": 181, "date": "11.12.2005", "team_home": 1, "team_away": 17, "goals_home": 3, "goals_away": 0},
{"match_id": 253, "date": "12.02.2006", "team_home": 1, "team_away": 11, "goals_home": 1, "goals_away": 1},
{"match_id": 254, "date": "19.02.2006", "team_home": 16, "team_away": 1, "goals_home": 0, "goals_away": 3},
{"match_id": 268, "date": "26.02.2006", "team_home": 1, "team_away": 10, "goals_home": 1, "goals_away": 0},
{"match_id": 270, "date": "11.03.2006", "team_home": 1, "team_away": 12, "goals_home": 1, "goals_away": 0},
{"match_id": 272, "date": "19.03.2006", "team_home": 17, "team_away": 1, "goals_home": 1, "goals_away": 1},
{"match_id": 273, "date": "22.03.2006", "team_home": 1, "team_away": 15, "goals_home": 4, "goals_away": 1},
{"match_id": 274, "date": "26.03.2006", "team_home": 9, "team_away": 1, "goals_home": 0, "goals_away": 2},
{"match_id": 275, "date": "29.03.2006", "team_home": 13, "team_away": 1, "goals_home": 0, "goals_away": 0},
{"match_id": 276, "date": "02.04.2006", "team_home": 14, "team_away": 1, "goals_home": 1, "goals_away": 4},
{"match_id": 277, "date": "06.04.2006", "team_home": 1, "team_away": 14, "goals_home": 0, "goals_away": 0},
{"match_id": 278, "date": "09.04.2006", "team_home": 1, "team_away": 9, "goals_home": 3, "goals_away": 3},
{"match_id": 279, "date": "20.04.2006", "team_home": 1, "team_away": 17, "goals_home": 6, "goals_away": 0},
{"match_id": 280, "date": "23.04.2006", "team_home": 12, "team_away": 1, "goals_home": 2, "goals_away": 3},
{"match_id": 281, "date": "26.04.2006", "team_home": 15, "team_away": 1, "goals_home": 0, "goals_away": 1},
{"match_id": 282, "date": "30.04.2006", "team_home": 1, "team_away": 13, "goals_home": 2, "goals_away": 0},
{"match_id": 283, "date": "03.05.2006", "team_home": 10, "team_away": 1, "goals_home": 1, "goals_away": 3},
{"match_id": 284, "date": "06.05.2006", "team_home": 1, "team_away": 16, "goals_home": 4, "goals_away": 1},
{"match_id": 285, "date": "13.05.2006", "team_home": 11, "team_away": 1, "goals_home": 1, "goals_away": 2}]


results = []
teams = {}
players = {}

def extract_result(match, elem):
    a = elem.find('a')
    r = re.search("[0-9]+", d(a[0]).attr('href'))
    match['team_home'] = int(r.group(0))
    r = re.search("[0-9]+", d(a[1]).attr('href'))
    match['team_away'] = int(r.group(0))
    if match['team_home'] not in teams:
        teams[match['team_home']] = d(a[0]).text()
    if match['team_away'] not in teams:
        teams[match['team_away']] = d(a[1]).text()
    if match['team_home'] == 1:
        match['home'] = 1
    else:
        match['home'] = 0
    return match

def extract_goals(match, elem):
    goals = []
    gs = elem.html().strip().split(',')
    goals_home = 0
    goals_away = 0
    for g in gs:
        if g == '':
            break
        goal = {}
        # minute
        r = re.search("[0-9]+", g)
        minute = int(r.group(0))
        a = d(g).find('a')
        # player
        r = re.search("[0-9]+", d(a[0]).attr('href'))
        player_id = int(r.group(0))
        player = d(a[0]).text()
        # score
        r = re.search("[0-9]+:[0-9]+", d(g).html())
        goal['score'] = r.group(0)
        scr = r.group(0).split(':')
        if goals_home != int(scr[0]):
            team = match['team_home']
            goals_home = goals_home + 1
        else:
            team = match['team_away']
            goals_away = goals_away + 1
        goal['team'] = team
        goal['goals_home'] = goals_home
        goal['goals_away'] = goals_away
        # specials (penalty, goals)
        r = re.search("Penalty", d(g).html())
        if r != None:
            goal['Penalty'] = 1
        # set fields
        goal['minute'] = minute
        goal['player'] = player_id
        if player_id not in players:
            players[player_id] = {"name": player, "team": team};
        goals.append(goal)
    match['goals'] = goals
    return match
        
def extract_spectators(match, elem):
    match['spectators'] = d(elem).text()
    return match

def extract_red_cards(match, elem):
    match['red_cards'] = extract_cards(match, elem)
    return match

def extract_yellow_cards(match, elem):
    match['yellow_cards'] = extract_cards(match, elem)
    return match

def extract_cards(match, elem):
    cards = []
    cs = elem.html().strip().split(',')
    for c in cs:
        if c == '':
            break
        card = {}
        # minute
        r = re.search("[0-9]+", c)
        minute = int(r.group(0))
        # player
        a = d(c).find('a')
        r = re.search("[0-9]+", d(a[0]).attr('href'))
        player_id = int(r.group(0))
        player = d(a[0]).text()
        # specials (penalty, goals)
        r = re.search("\(.+\)", d(c).html())
        if r != None:
            card['reason'] = r.group(0)[1:-1]
        # set fields
        card['minute'] = minute
        card['player'] = player_id
        if player_id not in players:
            is_team_home = reduce(lambda l, c: l or c['id'] == player_id, match['players_home'])
            if is_team_home:
                team = match['team_home']
            else: 
                team = match['team_away']
            players[player_id] = {"name": player, "team": team}
        cards.append(card)
    return cards

def extract_team_home(match, elem):
    match['players_home'] = extract_players(match, elem, match['team_home'])
    return match
    
def extract_team_away(match, elem):
    match['players_away'] = extract_players(match, elem, match['team_away'])
    return match

def extract_players(match, elem, team):
    pls = []
    ps = elem.html().split(',')
    for p in ps:
        player = {}
        # player
        a = d(p).find('a')
        if len(a) == 0:
            a = d(p)
        r = re.search("[0-9]+", d(a[0]).attr('href'))
        player_id = int(r.group(0))
        player_name = d(a[0]).text()
        player['id'] = player_id
        player['in'] = 0
        player['out'] = 90
        if player_id not in players:
            players[player_id] = {"name": player_name, "team": team}
        if len(a) > 1:
            # minute
            r = re.search("[0-9]+\.", p)
            minute = int(r.group(0)[:-1])
            player['out'] = int(minute)
            r = re.search("[0-9]+", d(a[1]).attr('href'))
            substitute = {}
            substitute['id'] = int(r.group(0))
            substitute['in'] = int(minute)
            substitute['out'] = 90
            sub_playername = d(a[1]).text()
            if substitute['id'] not in players:
                players[substitute['id']] = {"name": sub_playername, "team": team}
            pls.append(substitute)
        pls.append(player)
    return pls


# 2003/04
# match_ids = [96,95,94,93,92,91,90,89,88,87,85,84,83,81,80,79,76,75,73,72,71,69,68,67,66,65,64,62,60,57,56,55,54,53,52,51]
# 2005/06
match_ids = [2, 1, 3, 4, 5, 7, 16, 58, 78, 97, 99, 139, 144, 150, 168, 176, 177, 181, 253, 254, 268, 270, 272, 273, 274, 275, 276, 277, 278, 279, 280, 281, 282, 283, 284, 285]    

# d = pq(u'<head><meta http-equiv="Content-Type" content="text/html; charset=utf-8" /><meta name="description" content="dbFCZ ist eine Online-Datenbank, die alle Spiele des Fussballclubs Z\xfcrich (FCZ) nachweist. Bis heute sind alle Pflichtspiele und viele Freundschaftsspiele (insgesamt 1722) zwischen dem 11.11.1979 und dem 11.12.2010 erfasst." /><title>dbFCZ | Spiel \u2013 02.08.2003</title><style type="text/css" media="all">\n/*&lt;![CDATA[*/\n@import url(css/fcz.css);\n/*]]&gt;*/\n</style></head><body>\n<div id="main">\n<div id="kopf">\n<span class="t34b">dbFCZ</span>\n<span class="t10gr"></span>\n</div>\n<div id="menue_links">\n<div id="navbar">\n<br /><ul><li><a href="./index.php" class="current">Home</a></li>\n<li><a href="./saison.php" class="current">Saison</a></li>\n<li><a href="./topx.php" class="current">TopX</a></li>\n<li><a href="./storystart.php" class="current">Story</a></li>\n<li><a href="./offen.php" class="current">Noch offen</a></li>\n<li><a href="./disclaimer.php" class="current">Kontakt</a></li>\n</ul></div>\n\xa0\n<div class="trennstrich">\n\xa0\n</div>\n\xa0\n<div id="form_suche">\n<form action="suche.php" method="post">\n<ul><li><span>suchen</span></li>\n<li><input type="text" size="18" name="suche_string" />\xa0<input id="submit" type="submit" value="los" /></li>\n<li><input type="radio" name="suche_radio" value="suche_volltext" checked="checked" /><span class="radio">\xa0Volltext</span></li>\n<li><input type="radio" name="suche_radio" value="suche_spiel" /><span class="radio">\xa0Spiel</span></li>\n<li><input type="radio" name="suche_radio" value="suche_spieler" /><span class="radio">\xa0Spieler</span></li>\n<li><input type="radio" name="suche_radio" value="suche_team" /><span class="radio">\xa0Team</span></li>\n<li><input type="radio" name="suche_radio" value="suche_saison" /><span class="radio">\xa0Saison</span></li>\n</ul></form>\n</div>\n\xa0\n<div class="trennstrich">\n\xa0\n</div>\n\xa0\n<div id="info">\n<table><tr><td>Spiele seit: </td><td class="listabst">\xa0</td><td>11.11.1979</td></tr><tr><td>Spiele bis: </td><td class="listabst">\xa0</td><td>11.12.2010</td></tr><tr><td>Total Spiele: </td><td class="listabst">\xa0</td><td>1722</td></tr></table></div>\n<div style="position:absolute; bottom:1px; left:3px">\n<a href="http://flattr.com/thing/43787/dbFCZ-Die-Spiele-des-FC-Zurich" target="_blank">\n<img src="http://api.flattr.com/button/button-compact-static-100x17.png" alt="Flattr this" title="Flattr this" border="0" /></a></div>\n</div>\n<div id="orientierungszeile">\nSpiel | FCZ - St. Gallen (02.08.2003)\n</div>\n<div id="text_bereich">\n<br /><table border="0"><tr><td></td>\n<td class="listabst">\xa0</td>\n<td>\n<a href="saison.php?saison_id=3">2003/2004</a> - 02.08.2003 - 90 Min.</td></tr><tr><td>\n</td>\n<td class="listabst">\xa0</td>\n<td>\nMeisterschaftsspiel (Phase 1) - Runde: 4</td></tr><tr><td class="leerzeile">\xa0</td>\n<td class="listabst">\xa0</td>\n<td class="leerzeile">\xa0</td>\n</tr><tr><td class="label">\n*</td>\n<td class="listabst">\xa0</td>\n<td>\n<a href="team.php?team_id=1">FCZ</a> - <a href="team.php?team_id=12">St. Gallen</a> 2:2 (0:1)</td></tr><tr><td class="leerzeile">\xa0</td>\n<td class="listabst">\xa0</td>\n<td class="leerzeile">\xa0</td>\n</tr><tr><td class="label">\nTore</td>\n<td class="listabst">\xa0</td>\n<td>\n11.\xa0<a href="./spieler.php?spieler_id=82">Alexander Tachie Mensah</a> (<a href="./spieler.php?spieler_id=792">Mendes Da Concei\xe7ao Naldo</a>) 0:1, 63.\xa0<a href="./spieler.php?spieler_id=15">Artur Petrosyan</a> (<a href="./spieler.php?spieler_id=30">Daniel Gygax</a>) 1:1, 78.\xa0<a href="./spieler.php?spieler_id=82">Alexander Tachie Mensah</a>  (Penalty)<a href="./spieler.php?spieler_id=0"></a>  1:2, 89.\xa0<a href="./spieler.php?spieler_id=15">Artur Petrosyan</a> (<a href="./spieler.php?spieler_id=713">Sergio Bastida</a>) 2:2</td></tr><tr><td class="leerzeile">\xa0</td>\n<td class="listabst">\xa0</td>\n<td class="leerzeile">\xa0</td>\n</tr><tr><td class="label">\nFCZ</td>\n<td class="listabst">\xa0</td>\n<td>\n<a href="./spieler.php?spieler_id=1">Davide Taini</a>, <a href="./spieler.php?spieler_id=7">Alain Nef</a> (73.\xa0<a href="./spieler.php?spieler_id=39">Tariq Chihab</a>), <a href="./spieler.php?spieler_id=31">Stephan Keller</a>, <a href="./spieler.php?spieler_id=6">Blerim Dzemaili</a>, <a href="./spieler.php?spieler_id=532">Ivan Dal Santo</a>, <a href="./spieler.php?spieler_id=30">Daniel Gygax</a>, <a href="./spieler.php?spieler_id=33">Daniel Tarone</a> (77.\xa0<a href="./spieler.php?spieler_id=13">Almen Abdi</a>), <a href="./spieler.php?spieler_id=15">Artur Petrosyan</a>, <a href="./spieler.php?spieler_id=713">Sergio Bastida</a>, <a href="./spieler.php?spieler_id=22">Alhassane Keita</a>, <a href="./spieler.php?spieler_id=32">Francisco Guerrero</a> (69.\xa0<a href="./spieler.php?spieler_id=21">Kresimir Stanic</a>)</td></tr><tr><td class="label">\nTrainer </td>\n<td class="listabst">\xa0</td>\n<td>\n<a href="./spieler.php?spieler_id=24">Lucien Favre</a></td></tr><tr><td class="leerzeile">\xa0</td><td class="listabst">\xa0</td>\n\n<td class="leerzeile">\xa0</td>\n</tr><tr><td class="label">\nSt. Gallen</td>\n<td class="listabst">\xa0</td>\n<td>\n<a href="./spieler.php?spieler_id=67">Stefano Razzetti</a>, <a href="./spieler.php?spieler_id=879">Thomas Balmer</a>, <a href="./spieler.php?spieler_id=74">Marc Zellweger</a>, <a href="./spieler.php?spieler_id=70">Stefan Wolf</a>, <a href="./spieler.php?spieler_id=269">Pascal Jenny</a>, <a href="./spieler.php?spieler_id=790">Tranquillo Barnetta</a> (55.\xa0<a href="./spieler.php?spieler_id=79">David Marazzi</a>), <a href="./spieler.php?spieler_id=55">Dusan Pavlovic</a>, <a href="./spieler.php?spieler_id=715">Daniel Imhof</a>, <a href="./spieler.php?spieler_id=78">Bruno Sutter</a>, <a href="./spieler.php?spieler_id=82">Alexander Tachie Mensah</a> (88.\xa0<a href="./spieler.php?spieler_id=903">Christoph B\xe4ttig</a>), <a href="./spieler.php?spieler_id=792">Mendes Da Concei\xe7ao Naldo</a> (64.\xa0<a href="./spieler.php?spieler_id=85">Moreno Merenda</a>)</td></tr><tr><td class="label">\nTrainer </td>\n<td class="listabst">\xa0</td>\n<td>\n<a href="./spieler.php?spieler_id=719">Heinz Peischl</a></td></tr><tr><td class="leerzeile">\xa0</td>\n<td class="listabst">\xa0</td>\n<td class="leerzeile">\xa0</td>\n</tr><tr><td class="label">\nStadion/Ort</td>\n<td class="listabst">\xa0</td>\n<td>\nLetzigrund, Z\xfcrich</td>\n</tr><tr><td class="label">\nZuschauerInnen</td>\n<td class="listabst">\xa0</td>\n<td>\n7400</td>\n</tr><tr><td class="label">\nSchiedsrichter</td>\n<td class="listabst">\xa0</td>\n<td>\n<a href="./schiedsrichter.php?schiedsrichter_id=12">Guido Wildhaber</a></td>\n</tr><tr><td class="label">\nRote Karten</td>\n<td class="listabst">\xa0</td>\n<td>\n78. <a href="./spieler.php?spieler_id=6">Blerim Dzemaili</a> (Handspiel)</td>\n</tr><tr><td class="label">\nGelbe Karten</td>\n<td class="listabst">\xa0</td>\n<td>\n29. <a href="./spieler.php?spieler_id=74">Marc Zellweger</a> (Foul), 41. <a href="./spieler.php?spieler_id=33">Daniel Tarone</a> (Foul), 58. <a href="./spieler.php?spieler_id=31">Stephan Keller</a> (Foul), 73. <a href="./spieler.php?spieler_id=713">Sergio Bastida</a> (Foul), 79. <a href="./spieler.php?spieler_id=79">David Marazzi</a> (Foul), 89. <a href="./spieler.php?spieler_id=879">Thomas Balmer</a> (Foul), 93. <a href="./spieler.php?spieler_id=55">Dusan Pavlovic</a> (Foul)</td></tr><tr><td class="leerzeile">\xa0</td>\n<td class="listabst">\xa0</td>\n<td class="leerzeile">\xa0</td>\n</tr><tr><td class="label">\n</td>\n<td class="listabst">\xa0</td>\n<td>\n</td></tr></table><br /><br /><br /></div>\n<div id="fuss">\n<table style="width:100%"><tr><td>\xa92006-2011 rmz\n</td><td style="text-align:right"><form action="kontakt.php" method="post">\n<input type="hidden" name="fehler" value="/spiel.php?spiel_id=93" />\nFehler auf dieser Seite melden: <input id="submit" type="submit" value="los" /></form>\n</td></tr></table></div>\n<script type="text/javascript">\nvar gaJsHost = (("https:" == document.location.protocol) ? "https://ssl." : "http://www.");\ndocument.write(unescape("%3Cscript src=\'" + gaJsHost + "google-analytics.com/ga.js\' type=\'text/javascript\'%3E%3C/script%3E"));\n</script><script type="text/javascript">\ntry{\nvar pageTracker = _gat._getTracker("UA-1329203-2");\npageTracker._trackPageview();\n} catch(err) {}</script></div>\n</body>')
for m in match_ids:
    print m
    d = pq(url='http://dbfcz.ch/spiel.php?spiel_id=' + str(m))
    d = d('#text_bereich table')
    tds = d.find('td').not_('.listabst').not_('.leerzeile')

    match = {}
    match['id'] = m
    for i in matches:
        if i['match_id'] == m:
            match['goals_home'] = i['goals_home']
            match['goals_away'] = i['goals_away']
            match['date'] = i['date']
    for idx, td in enumerate(tds[4::2]):
        elem = d(tds[idx*2 + 5])
        if idx == 0:
            match = extract_result(match, elem)
        elif idx == 1:
            match = extract_goals(match, elem)
        elif idx == 2:
             match = extract_team_home(match, elem)
        # elif idx == 3:
        #     extract_trainer_home(match, elem)
        elif idx == 4:
            match = extract_team_away(match, elem)
        # elif idx == 5:
        #     extract_trainer_away(match, elem)
        # elif idx == 6:
        #     extract_stadium(match, elem)
        elif idx == 7:
            match = match = extract_spectators(match, elem)
        # elif idx == 8:
        #     extract_ref(match, elem)
        elif idx == 9:
            match = extract_red_cards(match, elem)
        elif idx == 10:
            match = extract_yellow_cards(match, elem)

    results.append(match)

outf = open('matches.js', 'w')
outf.write(json.dumps(results))
outf.close()

outf = open('players.js', 'w')
outf.write(json.dumps(players))
outf.close()

outf = open('teams.js', 'w')
outf.write(json.dumps(teams))
outf.close()

print players
print results
    
