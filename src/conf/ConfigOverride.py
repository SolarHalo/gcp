'''
Created on 2014-10-29

@author: tiamsw
'''

configs = {
    'game.bigfish':{
        'data_path':'D:\\working\\workspace\\pythonspace\\gcp\\src\\data\\',
        'dtd':'http://rss.bigfishgames.com/',
        'url':'http://rss.bigfishgames.com/rss.php?username=zzfhrb&type=${type}&locale=${locale}&gametype=${gametype}',
        #'url':'http://rss.bigfishgames.com/rss.php?username=zzfhrb&content=${content}&locale=${locale}&gametype=${gametype}',
        '${gametype}':['pc','mac','og'],
        '${locale}':['en','es','de','fr','jp','pt','da','it','nl','sv'],
        '${type}':[6]
        #'${content}':['catch','daily','feature']
    },
    'game.alawar':{
        'data_path':'D:\\working\\workspace\\pythonspace\\gcp\\src\\data\\',
        'dtd':'http://export.alawar.com/',
        'url':'http://eu.export.alawar.com/games_agsn_xml.php?pid=10328&locale=${locale}',
        '${locale}':['en','de','fr','nl','it','pt','es','tr']
    }
    
}
