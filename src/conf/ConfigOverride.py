'''
Created on 2014-10-29

@author: tiamsw
'''

configs = {
    'game.bigfish':{
        'data_path':'/var/games/gcp/src/data/',
        'dtd':['http://rss.bigfishgames.com/','http://www.bigfishgames','http://games.bigfishgames.com'],
        'url.game':'http://rss.bigfishgames.com/rss.php?username=zzfhrb&type=${type}&locale=${locale}&gametype=${gametype}',
        'url.game_catch':'http://rss.bigfishgames.com/rss.php?username=zzfhrb&content=catch&locale=${locale}&gametype=${gametype}',
        'url.game_daily':'http://rss.bigfishgames.com/rss.php?username=zzfhrb&content=${content}&locale=${locale}&gametype=${gametype}',
        'url.game_feature':'http://rss.bigfishgames.com/rss.php?username=zzfhrb&content=feature&locale=${locale}&gametype=${gametype}',
        '${content}':["glrank","glrelease","action","jigsaw","mahjong","puzzle","card","word","hidden",
                      "match3","marble","brain","adventure_large","adventure","brick","shooter","time",
                      "kids","mystery","strategy","riddle","animal","baking","book","breakout","building",
                      "burger","chicken","childrens","christmas","classic","cooking","detective","dress_up",
                      "educational","fairy","fantasy","farm","fashion","food","garden","holiday","ice_cream",
                      "magic","monster","pirate","point_and_click","poker","quest","restaurant","rpg",
                      "seek_and_find","sim","solitaire","space","sudoku","tower_defense","travel","treasure",
                      "tycoon","water","agatha_christie","diner_dash","dream_day","luxor","nancy_drew","ricochet",
                      "sherlock_holmes","slingo","spongebob","virtual_villagers","azada","hidden_expedition","mystery_case_files",
                      "best_pc","editors_de","collectors","valentines_day","halloween","spooky","zombie","vampire","love_and_romance",
                      "youda","mania","frenzy","big_city_adventure","hidden_mysteries","buildalot","super_granny","mystery_pi",
                      "dracula","physics","bundle"],
        '${gametype}':['pc','mac','og'],
        '${locale}':['en','es','de','fr','jp','pt','da','it','nl','sv'],
        '${type}':[6]
    },
    'game.alawar':{
        'data_path':'/var/games/gcp/src/data/',
        'dtd':'http://export.alawar.com/',
        'url.game.en':'http://www.alawar.com/export/games_agsn_xml.php?pid=10328',
        'url.game.de':'http://www.alawar.de/export/games_agsn_xml.php?pid=10328',
        'url.game.pl':'http://www.alawar.pl/export/games_agsn_xml.php?pid=10328',
        'url.game.ru':'http://export.alawar.ru/games_agsn_xml.php?pid=10328&lang=ru',
        'url.game.tr':'http://eu.export.alawar.com/games_agsn_xml.php?pid=10328&locale=tr',
        'url.game.es':'http://eu.export.alawar.com/games_agsn_xml.php?pid=10328&locale=es',
        'url.game.pt':'http://eu.export.alawar.com/games_agsn_xml.php?pid=10328&locale=pt',
        'url.game.it':'http://eu.export.alawar.com/games_agsn_xml.php?pid=10328&locale=it',
        'url.game.fr':'http://eu.export.alawar.com/games_agsn_xml.php?pid=10328&locale=fr',
        'url.game.nl':'http://eu.export.alawar.com/games_agsn_xml.php?pid=10328&locale=nl',
        'url.game.cs':'http://eu.export.alawar.com/games_agsn_xml.php?pid=10328&locale=cs'
    }
    
}


