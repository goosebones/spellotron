"""
my_corrected_words = ['abilitey', 'abouy', 'accomodate', 'acord', 'adultry', 'aggresive', 'alchohol', 'alchoholic', 'amature', 'amification', 'annoint', 'appreceiated', 'archeype', 'artic', 'ast', 'asymetric', 'atentively', 'beging', 'behaviour', 'belive', 'blait', 'buch', 'buder', 'budr', 'budter', 'buton', 'changeing', 'cheet', 'cicle', 'cimplicity', 'circue', 'circumstaces', 'clob', 'coaln', 'colloquilism', 'columne', 'comiler', 'commerciasl', 'commited', 'commitee', 'companys', 'compicated', 'contast', 'cooly', 'courst', 'crasy', 'cravets', 'croke', 'ctitique', 'dag', 'daly', 'deaft', 'descrption', 'destint', 'developement', 'diagree', 'dieties', 'direcyly', 'discuess', 'disect', 'doenload', 'doog', 'drunkeness', 'dur', 'dynaic', 'effots', 'eitiology', 'embarass', 'embarassment', 'engins', 'ennuui', 'enought', 'enviroment', 'equire', 'errara', 'erro', 'excercise', 'excpt', 'excution', 'expresso', 'failer', 'faver', 'faxe', 'firey', 'flatterring', 'fluk', 'flukse', 'fone', 'forsee', 'fuction', 'futs', 'gamne', 'gobernment', 'gracefull', 'gradualy', 'hallo', 'hapily', 'harrass', 'havne', 'heighth', 'hellp', 'helo', 'herlo', 'higer', 'hippopotamous', 'hlp', 'hourse', 'houssing', 'howver', 'hystrical', 'ident', 'imfamy', 'inerface', 'infact', 'inital', 'innoculate', 'insistenet', 'instulation', 'inteligent', 'interate', 'interpretter', 'johhn', 'latext', 'leasve', 'lesure', 'liason', 'libary', 'likly', 'lilometer', 'lossing', 'luser', 'maddness', 'majoraly', 'maks', 'mant', 'marshall', 'maxium', 'meory', 'metter', 'mic', 'millenium', 'minum', 'mischievious', 'momento', 'mousr', 'mroe', 'neccessary', 'necesary', 'neice', 'neighbour', 'nevade', 'nieve', 'noone', 'noticably', 'notin', 'objectsion', 'obsfuscate', 'occuppied', 'occurence', 'olf', 'organise', 'organiz', 'oving', 'patten', 'perogative', 'politict', 'pollice', 'practicle', 'preceeding', 'precios', 'prefices', 'prefixt', 'presue', 'presued', 'priviledge', 'proceedures', 'pronounciation', 'quoz', 'radious', 'rectangeles', 'redign', 'respct', 'roon', 'rought', 'rsx', 'runnung', 'salut', 'secion', 'seferal', 'segements', 'sieze', 'simplye', 'sitte', 'situration', 'smil', 'sometmes', 'spel', 'spoak', 'stering', 'stumach', 'subpena', 'suger', 'taff', 'taht', 'tattos', 'teh', 'tem', 'teo', 'tesst', 'tets', 'ths', 'thw', 'tommorrow', 'tomorow', 'ttest', 'tured', 'unnaturral', 'volumptuous', 'volye', 'wadting', 'waite', "wan't", 'warloord', 'whard', 'whimp', 'wicken', 'wrank', 'writting', 'youe']

their_corrected_words = ['abilitey', 'abouy', 'accomodate', 'acord', 'adultry', 'aggresive', 'alchohol', 'alchoholic', 'amature', 'amification', 'annoint', 'appreceiated', 'archeype', 'artic', 'ast', 'asymetric', 'atentively', 'beging', 'behaviour', 'belive', 'blait', 'buch', 'buder', 'budr', 'budter', 'buton', 'changeing', 'cheet', 'cicle', 'cimplicity', 'circue', 'circumstaces', 'clob', 'coaln', 'colloquilism', 'columne', 'comiler', 'commerciasl', 'commited', 'commitee', 'companys', 'compicated', 'contast', 'cooly', 'courst', 'crasy', 'cravets', 'croke', 'ctitique', 'dag', 'daly', 'deaft', 'descrption', 'destint', 'developement', 'diagree', 'dieties', 'direcyly', 'discuess', 'disect', 'doenload', 'doog', 'drunkeness', 'dur', 'dynaic', 'effots', 'eitiology', 'embarass', 'embarassment', 'engins', 'ennuui', 'enought', 'enviroment', 'equire', 'errara', 'erro', 'excercise', 'excpt', 'excution', 'expresso', 'failer', 'faver', 'faxe', 'firey', 'flatterring', 'fluk', 'flukse', 'fone', 'forsee', 'fuction', 'futs', 'gamne', 'gobernment', 'gracefull', 'gradualy', 'hallo', 'hapily', 'harrass', 'havne', 'heighth', 'hellp', 'helo', 'herlo', 'higer', 'hippopotamous', 'hlp', 'hourse', 'houssing', 'howver', 'hystrical', 'ident', 'imfamy', 'inerface', 'infact', 'inital', 'innoculate', 'insistenet', 'instulation', 'inteligent', 'interate', 'interpretter', 'johhn', 'latext', 'leasve', 'lesure', 'liason', 'libary', 'likly', 'lilometer', 'lossing', 'luser', 'maddness', 'majoraly', 'maks', 'mant', 'marshall', 'maxium', 'meory', 'metter', 'mic', 'millenium', 'minum', 'mischievious', 'momento', 'mousr', 'mroe', 'neccessary', 'necesary', 'neice', 'neighbour', 'nevade', 'nieve', 'noone', 'noticably', 'notin', 'objectsion', 'obsfuscate', 'occuppied', 'occurence', 'olf', 'organise', 'organiz', 'oving', 'patten', 'perogative', 'politict', 'pollice', 'practicle', 'preceeding', 'precios', 'prefices', 'prefixt', 'presue', 'presued', 'priviledge', 'proceedures', 'pronounciation', 'quoz', 'radious', 'rectangeles', 'redign', 'respct', 'roon', 'rought', 'rsx', 'runnung', 'salut', 'secion', 'seferal', 'segements', 'sieze', 'simplye', 'sitte', 'situration', 'smil', 'sometmes', 'spel', 'spoak', 'stering', 'stumach', 'subpena', 'suger', 'taff', 'taht', 'tattos', 'teh', 'tem', 'teo', 'tesst', 'tets', 'ths', 'thw', 'tommorrow', 'tomorow', 'ttest', 'tured', 'unnaturral', 'volumptuous', 'volye', 'wadting', 'waite', "wan't", 'warloord', 'whard', 'whimp', 'wicken', 'wrank', 'writting', 'youe']


my_unknown_words = ['Steffen', 'absorbtion', 'accidently', 'accosinly', 'acommadate', 'allieve', 'ambivilant', 'amourfous', 'annonsment', 'annuncio', 'anonomy', 'anotomy', 'anynomous', 'appresteate', 'aquantance', 'aratictature', 'aricticure', 'asentote', 'asterick', 'autoamlly', 'bankrot', 'basicly', 'batallion', 'bbrose', 'beauro', 'beaurocracy', 'beggining', 'beleive', 'benidifs', 'bigginging', 'bouyant', 'boygot', 'brocolli', 'buracracy', 'burracracy', 'byby', 'cauler', 'cemetary', 'cocamena', 'colleaque', 'comitmment', 'comitte', 'comittmen', 'comittmend', 'comupter', 'concensus', 'congradulations', 'conibation', 'consident', 'contastant', 'contunie', 'cosmoplyton', 'credetability', 'criqitue', 'crucifiction', 'crusifed', 'cumba', 'custamisation', 'danguages', 'defence', 'defenly', 'definate', 'definately', 'dependeble', 'descrptn', 'desparate', 'dessicate', 'develepment', 'develpond', 'devulge', 'dinasaur', 'dinasour', 'disippate', 'disition', 'dispair', 'disssicion', 'distarct', 'distart', 'distroy', 'documtations', 'dongle', 'dramaticly', 'ductioneery', 'duren', 'dymatic', 'ecstacy', 'efficat', 'efficity', 'egsistence', 'elagent', 'elligit', 'embaress', 'encapsualtion', 'encyclapidia', 'encyclopia', 'enhence', 'enligtment', 'enventions', 'envireminakl', 'epitomy', 'evaualtion', 'evething', 'evtually', 'excede', 'exhileration', 'existance', 'expleyly', 'explity', 'exspidient', 'extions', 'factontion', 'famdasy', 'fistival', 'frustartaion', 'funetik', 'gaurd', 'generly', 'goberment', 'gobernement', 'gotton', 'grammer', 'heellp', 'hifin', 'hifine', 'hiphine', 'howaver', 'humaniti', 'hyfin', 'hypotathes', 'hypotathese', 'illegitament', 'imediaetly', 'immenant', 'implemtes', 'inadvertant', 'incase', 'incedious', 'incompleet', 'incomplot', 'inconvenant', 'inconvience', 'independant', 'independenent', 'indepnends', 'indepth', 'indispensible', 'inefficite', 'influencial', 'initinized', 'initized', 'insistant', 'intealignt', 'intejilent', 'intelegent', 'intelegnent', 'intelejent', 'intelignt', 'intellagant', 'intellegent', 'intellegint', 'intellgnt', 'internation', 'interpretate', 'intertes', 'intertesd', 'invermeantial', 'irresistable', 'irritible', 'isotrop', 'kippur', 'knawing', 'liasion', 'lloyer', 'maintanence', 'majaerly', 'midia', 'minkay', 'misilous', 'monkay', 'mosaik', 'mostlikely', 'necesser', 'nickleodeon', 'nozled', 'ocassion', 'occusionaly', 'octagenarian', 'opposim', 'oscilascope', 'paramers', 'parametic', 'paranets', 'partrucal', 'pataphysical', 'permissable', 'permition', 'permmasivie', 'persue', 'phantasia', 'phenominal', 'playwrite', 'polation', 'poligamy', 'polypropalene', 'possable', 'pragmaticism', 'precion', 'preemptory', 'presbyterian', 'privielage', 'pronensiation', 'pronisation', 'properally', 'proplematic', 'protray', 'pscolgst', 'psicolagest', 'psycolagest', 'ramplily', 'reccomend', 'reccona', 'recieve', 'reconise', 'repitition', 'replasments', 'reposable', 'reseblence', 'respecally', 'rudemtry', 'sacreligious', 'saftly', 'satifly', 'scrabdle', 'sence', 'seperate', 'sicolagest', 'simpfilty', 'singal', 'slyph', 'soonec', 'specificialy', 'sponsered', 'stutent', 'styleguide', 'subisitions', 'subjecribed', 'supercede', 'superfulous', 'susan', 'swim_wear', 'syncorization', 'techniquely', 'teridical', 'thanot', 'theirselves', 'theridically', 'thredically', 'thruout', 'titalate', 'tradegy', 'trubbel', 'tunnellike', 'tyrrany', 'unatourral', 'unaturral', 'unconisitional', 'unconscience', 'underladder', 'unentelegible', 'unformanlly', 'unfortally', 'unfortunently', 'upcast', 'upmost', 'uranisium', 'verison', 'vinagarette', 'volunteerism', 'whaaat', 'wierd', 'yeild']


thier_unknown_words = ['Steffen', 'absorbtion', 'accidently', 'accosinly', 'acommadate', 'allieve', 'ambivilant', 'amourfous', 'annonsment', 'annuncio', 'anonomy', 'anotomy', 'anynomous', 'appresteate', 'aquantance', 'aratictature', 'aricticure', 'asentote', 'asterick', 'autoamlly', 'bankrot', 'basicly', 'batallion', 'bbrose', 'beauro', 'beaurocracy', 'beggining', 'beleive', 'benidifs', 'bigginging', 'bouyant', 'boygot', 'brocolli', 'buracracy', 'burracracy', 'byby', 'cauler', 'cemetary', 'cocamena', 'colleaque', 'comitmment', 'comitte', 'comittmen', 'comittmend', 'comupter', 'concensus', 'congradulations', 'conibation', 'consident', 'contastant', 'contunie', 'cosmoplyton', 'credetability', 'criqitue', 'crucifiction', 'crusifed', 'cumba', 'custamisation', 'danguages', 'defence', 'defenly', 'definate', 'definately', 'dependeble', 'descrptn', 'desparate', 'dessicate', 'develepment', 'develpond', 'devulge', 'dinasaur', 'dinasour', 'disippate', 'disition', 'dispair', 'disssicion', 'distarct', 'distart', 'distroy', 'documtations', 'dongle', 'dramaticly', 'ductioneery', 'duren', 'dymatic', 'ecstacy', 'efficat', 'efficity', 'egsistence', 'elagent', 'elligit', 'embaress', 'encapsualtion', 'encyclapidia', 'encyclopia', 'enhence', 'enligtment', 'enventions', 'envireminakl', 'epitomy', 'evaualtion', 'evething', 'evtually', 'excede', 'exhileration', 'existance', 'expleyly', 'explity', 'exspidient', 'extions', 'factontion', 'famdasy', 'fistival', 'frustartaion', 'funetik', 'gaurd', 'generly', 'goberment', 'gobernement', 'gotton', 'grammer', 'heellp', 'hifin', 'hifine', 'hiphine', 'howaver', 'humaniti', 'hyfin', 'hypotathes', 'hypotathese', 'illegitament', 'imediaetly', 'immenant', 'implemtes', 'inadvertant', 'incase', 'incedious', 'incompleet', 'incomplot', 'inconvenant', 'inconvience', 'independant', 'independenent', 'indepnends', 'indepth', 'indispensible', 'inefficite', 'influencial', 'initinized', 'initized', 'insistant', 'intealignt', 'intejilent', 'intelegent', 'intelegnent', 'intelejent', 'intelignt', 'intellagant', 'intellegent', 'intellegint', 'intellgnt', 'internation', 'interpretate', 'intertes', 'intertesd', 'invermeantial', 'irresistable', 'irritible', 'isotrop', 'kippur', 'knawing', 'liasion', 'lloyer', 'maintanence', 'majaerly', 'midia', 'minkay', 'misilous', 'monkay', 'mosaik', 'mostlikely', 'necesser', 'nickleodeon', 'nozled', 'ocassion', 'occusionaly', 'octagenarian', 'opposim', 'oscilascope', 'paramers', 'parametic', 'paranets', 'partrucal', 'pataphysical', 'permissable', 'permition', 'permmasivie', 'persue', 'phantasia', 'phenominal', 'playwrite', 'polation', 'poligamy', 'polypropalene', 'possable', 'pragmaticism', 'precion', 'preemptory', 'presbyterian', 'privielage', 'pronensiation', 'pronisation', 'properally', 'proplematic', 'protray', 'pscolgst', 'psicolagest', 'psycolagest', 'ramplily', 'reccomend', 'reccona', 'recieve', 'reconise', 'repitition', 'replasments', 'reposable', 'reseblence', 'respecally', 'rudemtry', 'sacreligious', 'saftly', 'satifly', 'scrabdle', 'sence', 'seperate', 'sicolagest', 'simpfilty', 'singal', 'slyph', 'soonec', 'specificialy', 'sponsered', 'stutent', 'styleguide', 'subisitions', 'subjecribed', 'supercede', 'superfulous', 'susan', 'swim_wear', 'syncorization', 'techniquely', 'teridical', 'thanot', 'theirselves', 'theridically', 'thredically', 'thruout', 'titalate', 'tradegy', 'trubbel', 'tunnellike', 'tyrrany', 'unatourral', 'unaturral', 'unconisitional', 'unconscience', 'underladder', 'unentelegible', 'unformanlly', 'unfortally', 'unfortunently', 'upcast', 'upmost', 'uranisium', 'verison', 'vinagarette', 'volunteerism', 'whaaat', 'wierd', 'yeild']


my_cor_dict = dict()
their_cor_dict = dict()

for word in my_corrected_words:
    my_cor_dict[word] = word
    
for word in their_corrected_words:
    their_cor_dict[word] = word


my_unknown_dict = dict()
their_unknown_dict = dict()

for word in my_unknown_words:
    my_unknown_dict[word] = word
    
for word in thier_unknown_words:
    their_unknown_dict[word] = word


print("corrected", "i should not have")
for key in their_cor_dict:
    is_in = key in my_cor_dict
    print(is_in)

print()
print()
print()
print("unknown", "i am missing")
for key in my_unknown_dict:
    is_in = key in their_unknown_dict
    print(is_in)
"""

def printer():
    my_words = open("my_printed_words.txt")
    my_printed_words = []
    for line in my_words:
        line = line.strip()
        my_printed_words.append(line)

    their_words = open("their_printed_words.txt")
    their_printed_words = []
    for line in their_words:
        line = line.strip()
        their_printed_words.append(line)

    my_print_dict = dict()
    for word in my_printed_words:
        my_print_dict[word] = word
        
    their_print_dict = dict()
    for word in their_printed_words:
        their_print_dict[word] = word

    count = 0
    for key in their_print_dict:
        is_in = key in my_print_dict
        if is_in == False:
            print(key)
            

printer()
    


