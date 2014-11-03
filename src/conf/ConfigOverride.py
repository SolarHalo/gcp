'''
Created on 2014-10-29

@author: tiamsw
'''

configs = {
    'game.bigfish':{
        'data_path':'D:\\work\\workspace\\pythonspace\\gcp\\src\\data\\',
        'dtd':'http://rss.bigfishgames.com/',
        #'url.game':'http://rss.bigfishgames.com/rss.php?username=zzfhrb&type=${type}&locale=${locale}&gametype=${gametype}',
        'url.game_catch':'http://rss.bigfishgames.com/rss.php?username=zzfhrb&content=catch&locale=${locale}&gametype=${gametype}',
        #'url.game_daily':'http://rss.bigfishgames.com/rss.php?username=zzfhrb&content=daily&locale=${locale}&gametype=${gametype}',
        #'url.game_feature':'http://rss.bigfishgames.com/rss.php?username=zzfhrb&content=feature&locale=${locale}&gametype=${gametype}',
        '${gametype}':['pc','mac','og'],
        '${locale}':['en','es','de','fr','jp','pt','da','it','nl','sv'],
        '${type}':[6]
    },
    'game.alawar':{
        'data_path':'D:\\work\\workspace\\pythonspace\\gcp\\src\\data\\',
        'dtd':'http://export.alawar.com/',
        'url.game':'http://eu.export.alawar.com/games_agsn_xml.php?pid=10328&locale=${locale}',
        '${locale}':['en','de','fr','nl','it','pt','es','tr']
    }
    
}
