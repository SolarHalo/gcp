#coding=utf-8
'''
Created on 2014-10-29

@author: tiamsw
'''

configs = {
    'db':{
        'db_host':'127.0.0.1',
        'db_user':'root',
        'db_pass':'mypassword',
        'db_db':'game'
    },
    'sys':{
        'threadpool.min':4,
        'threadpool.max':11,
        'threadpool.keep':4,
        'download.num':4,
        'db.batch.size':500
    },
    'genrelist':{
        'puzzle' : 4,
        'hidden object' : 15,
        'time management' : 25,
        'adventure' : 21,
        'match 3' : 17,
        'large file' : 20,
        'arcade & action' : 1,
        'word' : 6,
        'mahjong' : 3 ,
        'card & board' : 5,
        'strategy' : 29,
        'marble popper' : 18,
        'brain teaser' : 19,
        'kids' : 26,
        'video' : 97,
        'driving' : 98,
        'other' : 99,
        'jigsaw':100,
        'casino':101,
        'holiday':102,
        'sports':103,
        
        4 : 'puzzle',
        15 : 'hidden object',
        25 : 'time management',
        21 : 'adventure',
        17 : 'match 3',
        20 : 'large file',
        1 : 'arcade & action',
        6 : 'word',
        3 : 'mahjong',
        5 : 'card & board',
        29 : 'strategy',
        18 : 'marble popper',
        19 : 'brain teaser',
        26 : 'kids',
        97 : 'video',
        98 : 'driving',
        99 : 'other',
        100:'jigsaw',
        101:'casino',
        102:'holiday',
        103:'sports',
        
        'en':{
            'puzzle' : 4,
            'hidden object' : 15,
            'time management' : 25,
            'adventure' : 21,
            'match 3' : 17,
            'large file' : 20,
            'arcade & action' : 1,
            'word' : 6,
            'mahjong' : 3,
            'card & board' : 5,
            'strategy' : 29,
            'marble popper' : 18,
            'brain teaser' : 19,
            'kids' : 26,
            'video' : 97,
            'driving' : 98,
            'other' : 99,
            'all' : 'all',
            'new' : 'new',
            'top' : 'top',
            '1' : 'LangSeq',
            'english' : 'LangName',
            'English' : 'LangSelfName',
            'english version' : 'LangVersion',
            'america/los_angeles': 'LangTZ',
            'jigsaw':100,
            'casino':101,
            'holiday':102
        },
        'de':{
            'puzzle' : 4,
            'wimmelbild' : 15,
            'gegen-die-zeit' : 25,
            'abenteuer' : 21,
            '3-gewinnt' : 17,
            'breitband' : 20,
            'arcade- & action' : 1,
            'wort' : 6,
            'mahjong' : 3,
            'karten- & brett' : 5,
            'strategie' : 29,
            'murmel' : 18,
            'denksport' : 19,
            'kinder': 26 ,
            'other' : 99,
            'alle' : 'all',
            'neue' : 'new',
            'top' : 'top',
            '2' : 'LangSeq',
            'German' : 'LangName',
            'Deutsch' : 'LangSelfName',
            'Deutsch Version' : 'LangVersion',
            'Europe/Berlin' : 'LangTZ',
            
            'jigsaw':100,
            'worträtsel':6
        },
        'fr':{
            'puzzle' : 4,
            'objets cach&eacute;s' : 15,
            'gestion du temps' : 25,
            'aventure' : 21,
            'match 3' : 17,
            'grande aventure' : 20,
            'arcade & action' : 1,
            'mots' : 6,
            'mahjong' : 3,
            'cartes & plateau' : 5,
            'strat&eacute;gie' : 29,
            'destruction de billes' : 18,
            'casse-t&ecirc;te' : 19,
            'enfants' : 26,
            'other' : 99,
            'tous' : 'all',
            'nouveaux' : 'new',
            'top' : 'top',
            '3' : 'LangSeq',
            'French' : 'LangName',
            'Français' : 'LangSelfName',
            'Version Français' : 'LangVersion',
            'Europe/Paris' : 'LangTZ',
            
            'objets cachés': 15,
            'stratégie': 29,
            'casse-tête': 4
        },
        'es':{
            'puzzle' : 4,
            'objetos ocultos' : 15,
            'gesti&oacute;n del tiempo' : 25,
            'aventura' : 21,
            'match 3' : 17,
            'gran aventura' : 20,
            'arcade y acci&oacute;n' : 1,
            'palabras' : 6,
            'mahjong' : 3,
            'cartas y tablero' : 5,
            'estrategia' : 29,
            'destruir Bolas' : 18,
            'ingenio' : 19,
            'ni&ntilde;os' : 26,
            'other' : 99,
            'todo' : 'all',
            'nuevo' : 'new',
            'top' : 'top',
            '4' : 'LangSeq',
            'Spanish' : 'LangName',
            'Español' : 'LangSelfName',
            'Versión en Español' : 'LangVersion',
            'Europe/Madrid' : 'LangTZ',
            
            'gestión del tiempo':25,
            'arcade y acción':1,
            'rompecabezas':4,
            'niños':26,  
            'deportes':103,
            'destruir bolas':18,
            'casino':101
        },
        'dk':{
            'puzzle' : 4,
            'søg og find-spil' : 15,
            'tidsstyringsspil' : 25,
            'eventyrspil' : 21,
            'tre på stribe-spil' : 17,
            'arkade- og actionspil' : 1,
            'mahjong-spil' : 3,
            'strategispil' : 29,
            'other' : 99,
            'alle': 'all' ,
            'nye' : 'new',
            'topspil' : 'top',
            '5' : 'LangSeq',
            'Danish' : 'LangName',
            'Dansk' : 'LangSelfName',
            '' : 'LangVersion',
            'Europe/Copenhagen' : 'LangTZ'
        },
        'it':{
            'puzzle' : 4,
            'oggetti nascosti' : 15,
            'gestione del tempo' : 25,
            'avventura' : 21,
            'abbinamenti a 3' : 17,
            'arcade e azione' : 1,
            'mahjong' : 3,
            'carte e da tavolo' : 5,
            'strategia' : 29,
            'other' : 99,
            'tutti' : 'all',
            'novità' : 'new',
            'top' : 'top',
            '6' : 'LangSeq',
            'Italian' : 'LangName',
            'Italiano' : 'LangSelfName',
            '' : 'LangVersion',
            'Europe/Rome' : 'LangTZ',
            
            'enigmi & puzzle':4,
            'rebus':4,
            'scoppiabolle':18,
            'sports':103

        },
        'nl':{
            'puzzle' : 4,
            'verborgen voorwerp' : 15,
            'tijdmanagement' : 25,
            'avontuur' : 21,
            'drie-op-een-rij' : 17,
            'arcade & actie' : 1,
            'mahjong' : 3,
            'kaart & bord' : 5,
            'strategie' : 29,
            'other' : 99,
            'alle' : 'all',
            'nieuwe' : 'new',
            'topspellen' : 'top',
            '7' : 'LangSeq',
            'Dutch' : 'LangName',
            'Nederlands' : 'LangSelfName',
            '' : 'LangVersion',
            'Europe/Amsterdam' : 'LangTZ',
            
            'knikker':18
        },
        'se':{
            'puzzle' : 4,
            'sök och finn-spel' : 15,
            'tidsplaneringsspel' : 25,
            'äventyrsspel' : 21,
            '3-i-rad-spel' : 17,
            'arkad- och actionspel' : 1,
            'mahjong-spel' : 3,
            'kort- och brädspel' : 5,
            'strategispel' : 29,
            'other' : 99,
            'alla' : 'all',
            'nya' : 'new',
            'topplistan' : 'top',
            '8': 'LangSeq' ,
            'Swedish' : 'LangName',
            'Svenska' : 'LangSelfName',
            '' : 'LangVersion',
            'Europe/Stockholm' : 'LangTZ'
        },
        'br':{
            'puzzle' : 4,
            'objetos escondidos' : 15,
            'gerenciamento de tempo' : 25,
            'aventura' : 21,
            'combine 3' : 17,
            'fliperama e ação' : 1,
            'mahjong' : 3,
            'estratégia' : 29,
            'other' : 99,
            'todos' : 'all',
            'lançamentos' : 'new',
            'melhores' : 'top',
            '9' : 'LangSeq',
            'Portuguese' : 'LangName',
            'Português' : 'LangSelfName',
            '' : 'LangVersion',
            'America/Sao_Paulo' : 'LangTZ'
        },
        'jp':{
            'パズル' :4 ,
            'アイテム探し' : 15,
            'タイム マネージメント' : 25,
            'アドベンチャー' : 21,
            'マッチ 3': 17 ,
            'アーケード & アクション' : 1,
            '麻雀 & 上海' : 3 ,
            '戦略系' : 29,
            'ビー玉ポッパー' : 18,
            '頭の体操' : 19,
            'その他の' : 99,
            '全' : 'all',
            'ニュー' : 'new',
            'トップ' : 'top',
            '10' : 'LangSeq',
            'Japanese' : 'LangName',
            '日本語': 'LangSelfName',
            '日本語版' : 'LangVersion',
            'Asia/Tokyo' : 'LangTZ',
            
            'カード & ボード':5
        },
        'sv':{
            'sök och finn-spel':15,
            'arkad- och actionspel' :1,
            'kort- och brädspel':5,
            '3-i-rad-spel' :17,
            'mahjong-spel': 3,
            'tidsplaneringsspel':25,
            'Äventyrsspel': 21,
            'strategispel':29
        },
        'pt':{
            'objetos escondidos':15,
            'mahjong':3,
            'combine 3':17,
            'gerenciamento de tempo':25,
            'fliperama e ação':1,
            'aventura':21,
            'jigsaw':100,
            'cartas e tabuleiro':5,
            'estratégia':29,
            'sports':103
        },
        'da':{
            'tre på stribe-spil':18,
            'arkade- og actionspil':1,
            'tidsstyringsspil':25,
            'strategispil':29,
            'mahjong-spil':3,
            'søg og find-spil':15,
            'eventyrspil':21,
            'kort- og brætspil':5
        }
    }
      
}
