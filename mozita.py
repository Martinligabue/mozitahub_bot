import telepot
import time
from telepot.loop import MessageLoop
from telepot.namedtuple import InlineKeyboardMarkup, InlineKeyboardButton

TOKEN="---NASCOSTO---"

def risposte(msg):
    try:
        chat_id=msg['chat']['id']
        text=msg['text']
    except:
        print("Exception:001")
        ##entra in questa eccezione se NON è avviato come comando diretto (digitato come comando e inviato)
    try:
        query_id, chat_id, text = telepot.glance(msg, flavor='callback_query')
        print(query_data)
    except:
        print("Exception:002")
        ##entra in questa eccezione se NON è stato premendo su un pulsante delle inlineKeyboard
    ##i try-except precedente servono per assegnare, in qualunque circostanza, chat_id e text corettamente (in base al caso)
    home = InlineKeyboardMarkup(inline_keyboard=[
                    [InlineKeyboardButton(text='Vai al gruppo Home', url='https://t.me/joinchat/BCql3UMy26nl4qxuRecDsQ')],
                ])

    feedback = InlineKeyboardMarkup(inline_keyboard=[
                    [InlineKeyboardButton(text="Vai in 'Home' e lascia il tuo feedback", url='https://t.me/joinchat/BCql3UMy26nl4qxuRecDsQ')]
                ])

    start = InlineKeyboardMarkup(inline_keyboard=[
                    [InlineKeyboardButton(text='Mostrami che cosa posso fare', callback_data='/azioni')],
                    [InlineKeyboardButton(text='Ho bisogno di assistenza', callback_data='/support')],
                ])

    support = InlineKeyboardMarkup(inline_keyboard=[
                    [InlineKeyboardButton(text='Supporto via Telegram', url='https://t.me/joinchat/BCql3UMy26nl4qxuRecDsQ'),
                    InlineKeyboardButton(text='Supporto via forum', callback_data='/forum')],
                ])

    azioni = InlineKeyboardMarkup(inline_keyboard=[
                    [InlineKeyboardButton(text='Supporto', callback_data='/support'),
                    InlineKeyboardButton(text='Gruppi', callback_data='/gruppi'),
                    InlineKeyboardButton(text='Collabora', callback_data='/collabora')],
                    [InlineKeyboardButton(text='Info', callback_data='/info'),
                    InlineKeyboardButton(text='Home', callback_data='/home'),
                    InlineKeyboardButton(text='Vademecum', callback_data='/vademecum')],
                    [InlineKeyboardButton(text='News', callback_data='/news'),
                    InlineKeyboardButton(text='Feedback', callback_data='/feedback'),
                    InlineKeyboardButton(text='IoT', callback_data='/iot')],
                    [InlineKeyboardButton(text='Developer', callback_data='/developer'),
                    InlineKeyboardButton(text='Design', callback_data='/design')],
                ])

    gruppi = InlineKeyboardMarkup(inline_keyboard=[
                    [InlineKeyboardButton(text='Home', url='https://t.me/joinchat/BCql3UMy26nl4qxuRecDsQ'),
                    InlineKeyboardButton(text='News', url='https://t.me/mozItaNews')],
                    [InlineKeyboardButton(text='Voglio diventare volontario', url='https://t.me/joinchat/B1cgtEQAHkGVBTbI0XPd-A')],
                    [InlineKeyboardButton(text='Developer', url='https://t.me/joinchat/B1cgtENXHcxd3jzFar7Kuw'),
                    InlineKeyboardButton(text='L10N (chiedi in Home)', url='https://t.me/joinchat/BCql3UMy26nl4qxuRecDsQ')],
                    [InlineKeyboardButton(text='Design', url='https://t.me/joinchat/B1cgtA7DF3qDzuRvsEtT6g'),
                    InlineKeyboardButton(text='IoT', url='https://t.me/joinchat/B1cgtEzLzr0gvSJcEicq1g')],
                ])

    developer = InlineKeyboardMarkup(inline_keyboard=[
                    [InlineKeyboardButton(text='Vai al gruppo Developer', url='https://t.me/joinchat/B1cgtENXHcxd3jzFar7Kuw')],
                ])

    design = InlineKeyboardMarkup(inline_keyboard=[
                    [InlineKeyboardButton(text='Vai al gruppo Design Team', url='https://t.me/joinchat/B1cgtA7DF3qDzuRvsEtT6g')],
                ])

    iot = InlineKeyboardMarkup(inline_keyboard=[
                    [InlineKeyboardButton(text='Vai al gruppo IoT', url='https://t.me/joinchat/B1cgtEzLzr0gvSJcEicq1g')],
                ])

    vademecum = InlineKeyboardMarkup(inline_keyboard=[
                    [InlineKeyboardButton(text='Vademecum Generale', url='https://github.com/MozillaItalia/firefox-vademecum/blob/master/volantino/Vademecum_2.0_VG.pdf'),
                    InlineKeyboardButton(text='Vademecum Tecnico', url='https://github.com/MozillaItalia/firefox-vademecum/blob/master/volantino/Vademecum_2.0_VT.pdf')],
                ])

    collabora = InlineKeyboardMarkup(inline_keyboard=[
                    [InlineKeyboardButton(text="Si, vai al gruppo 'Home'", url='https://t.me/joinchat/BCql3UMy26nl4qxuRecDsQ'),
                    InlineKeyboardButton(text="No, ma vorrei collaborare", url='https://t.me/joinchat/B1cgtEQAHkGVBTbI0XPd-A')],
                ])

    news = InlineKeyboardMarkup(inline_keyboard=[
                    [InlineKeyboardButton(text="Vai al canale ufficiale 'News'", url='https://t.me/mozItaNews')],
                ])

    forum = InlineKeyboardMarkup(inline_keyboard=[
                    [InlineKeyboardButton(text='Vai al forum di Mozilla Italia', url='https://forum.mozillaitalia.org/')],
                ])

    '''
    nome_nome = InlineKeyboardMarkup(inline_keyboard=[
                    [InlineKeyboardButton(text='Testo bottone', callback_data='testo')],
                    [InlineKeyboardButton(text='Testo bottone', url='https://t.me/')],
                ])
    '''

    if text=="/home":
        bot.sendMessage(chat_id, "Mozilla Italia - Home e' gruppo che accomuna tutti i volontari Mozilla Italia, a prescindere dal gruppo di provenienza. Unisciti anche tu e diventa parte di questa grande famiglia!", reply_markup=home)
    #elif text=="/stop":
        #bot.sendMessage(chat_id, "Stai per disattivare MozIta Hub. Per attivarlo nuovamente sara' sufficiente premere il pulsante sottostante 'Avvia' o digitare /start. Se lo desideri puoi anche lasciarci un feedback sulla tua esperienza d'utilizzo del bot e la motivazione dell'abbandono. Grazie.", reply_markup=stop)
    elif text=="/start":
        bot.sendMessage(chat_id, "Benvenuto/a in Mozilla Italia Hub.\nQui potrai usufruire di funzioni uniche, come ottenere informazioni, richiedere supporto, e molto altro.\nScopri tutto cio' che puoi fare digitando /azioni.")
        bot.sendMessage(chat_id, "Dopo questa breve presentazione, che cosa desideri fare?", reply_markup=start)
    elif text=="/support":
        bot.sendMessage(chat_id, "Puoi aprire un topic sul nostro forum ufficiale dove, il team di volontari del Supporto Mozilla (SuMo), ti assistera' nel migliore modo possibile.\nIn alternativa puoi provare a chiedere nel gruppo 'Home' della comunita' direttamente da Telegram.")
        bot.sendMessage(chat_id, "Scegli tu cosa vuoi fare :)", reply_markup=support)
    elif text=="/gruppi":
        bot.sendMessage(chat_id, "Ecco qui la lista di tutti i canali e gruppi ufficiali di Mozilla Italia su Telegram:\n\n'Mozilla Italia - HOME' (/home):\nil gruppo principale di Mozilla Italia, nel quale vengono affrontate tante tematiche, dove si possono chiedere informazioni, supporto. E' il gruppo che accomuna tutti i volontari Mozilla Italia, ma anche i non-volontari, ovvero chi vuole rimanere in contatto con la comunità.\n\n'Mozilla Italia - News' (/news):\nil canale che ti permette di rimanere sempre aggiornato sulle ultime novità da Mozilla Italia.\n\n'Mozilla Italia - Voglio diventare volontario' (/collabora):\nil gruppo adatto per chi vuole entrare a far parte della comunità. Qui potrai avere maggiori informazioni su ciascun gruppo o, se non sai ancora come puoi contribuire alla causa, troverai persone che sono in grado di indirizzarti nel gruppo piu' adatto alle tue caratteristiche, alle tue abilita' e alle tue attitudini.\n\n'Mozilla Italia - Developers' (/developer):\nil gruppo dedicato agli sviluppatori Mozilla Italia, quindi a coloro che si dedicano maggiormente alla programmazione.\n\n'Mozilla Italia - L10N' (privato):\nil gruppo dedicato ai localizzatori (traduttori). Questo gruppo è privato, quindi chiedere nel gruppo Home di essere inserite se si e' interessati.\n\n'Mozilla Italia - Design Team' (/design):\nil gruppo dedicato ai 'designer' e a coloro che si dedicano maggiormente alla grafica.\n\n'Mozilla Italia - IoT' (/iot):\nil gruppo dedicato alle tecnologie Internet of Thing di Mozilla.\n\nPuoi appartenere e unirti anche a piu' gruppi contemporaneamente. Ti consigliamo, comunque, di unirti al gruppo 'Home' che è quello piu' generico :)", reply_markup=gruppi)
    elif text=="/collabora":
        bot.sendMessage(chat_id, "In Mozilla abbiamo bisogno di tutte le abilita'!\nLa comunita' di Mozilla Italia, infatti, si occupa di tradurre progetti e documentazione Mozilla, sviluppare progetti interni a Mozilla Italia, ma anche direttamente per Mozilla, prestare supporto tecnico a utenti bisognosi e tanto altro.")
        bot.sendMessage(chat_id, "Sai gia' come potresti essere utile e contribuire a Mozilla Italia?", reply_markup=collabora)
    elif text=="/vademecum":
        bot.sendMessage(chat_id, "Il vademecum e' un volantino che, in foglio A4 fronte-retro, riesce a spiegarti (molto brevemente) che cosa e' Mozilla, che cosa e' Mozilla Italia, i progetti attivi e altro.\nEsistono 2 tipi di Vademecum: il Generale, adatto a tutti, e il Tecnico, adatto piu' specificatamente per gli sviluppatori e programmatori (o chi e' in questo campo).\nQuindi, di quale versione vuoi prendere visione?", reply_markup=vademecum)
    elif text=="/feedback":
        bot.sendMessage(chat_id, "Puoi lasciare quando vuoi un feedback sui servizi offerti da Mozilla Italia, semplicemente recandoti sul gruppo 'Home', quindi riportando il feedback.\nNon preoccuparti, nessuno ti giudichera' o aggredira', ma anzi, troverai persone pronte a capire i tuoi problemi e i tuoi suggerimenti ed, eventualmente, a segnalarli direttamente a Mozilla :)", reply_markup=feedback)
    elif text=="/azioni":
        bot.sendMessage(chat_id, "Ecco cosa puoi fare su MozIta HUB:\n/support: richiedere e ricevere assistenza, da parte dei nostri volontari, su prodotti e progetti di Mozilla\n/gruppi: ottenere la lista di tutti i gruppi e canali ufficiali di Mozilla Italia\n/collabora: per unirti ai volontari Mozilla Italia\n/info: avere informazioni riguardo questo bot\n/home: per essere reindirizzato al gruppo piu' attivo di tutti! Dove vengono trattate varie tematiche, anche di ordine generale, come aggiornamenti, novita', richiesta di informazione o supporto, e altro ancora. E' il gruppo che accomuna tutti i volontari Mozilla Italia, a prescindere dal gruppo di appartenenza.\n/vademecum: ottieni il vademecum, il volantino che in poche e semplici parole ti illustra che cosa è Mozilla e i vari progetti attivi.\n/news: rimani sempre aggiornato sulle novità di Mozilla Italia; su questo canale potrai ricevere tutte le novità necessarie.\n/feedback: sentiti libero di lasciare un feedback sul bot e sui servizi di Mozilla Italia. Ricorda di essere sincero e imparziale per permetterci di migliore ciò che offriamo :)\n/developer: il gruppo dei volontari sviluppatori di Mozilla Italia.\n/design: il gruppo dei volontari designer di Mozilla Italia.\n/iot: il gruppo dedicato strettamente alla tecnologia IoT di Mozilla.")
        bot.sendMessage(chat_id, "Allora, che cosa vorresti fare?", reply_markup=azioni)
    elif text=="/news":
        bot.sendMessage(chat_id, "Rimani sempre aggiornato sul mondo Mozilla! Grazie a questo canale ufficiale sarai a conoscenze sempre delle ultime novita' da Mozilla Italia.", reply_markup=news)
    elif text=="/info":
        bot.sendMessage(chat_id, "MozIta Hub e' un bot realizzato per Mozilla Italia\nVersione: 0.0.1 preview\nUltimo aggiornamento: 30-08-2018")
    elif text=="/forum":
        bot.sendMessage(chat_id, "La comunita' di Mozilla Italia presta supporto tramite il forum ufficiale (www.forum.mozillaitalia.org) gratuitamente e quasi in tempo reale. Prima di aprire un topic e' necessario leggere il regolamento e accertarsi, ovviamente, che un topic uguale non sia stato gia' aperto e, magari, anche risolto.", reply_markup=forum)
    elif text=="/developer":
        bot.sendMessage(chat_id, "Entra a far parte del gruppo dedicato agli sviluppatori Mozilla Italia.", reply_markup=developer)
    elif text=="/design":
        bot.sendMessage(chat_id, "Unisciti al gruppo dei designer di Mozilla Italia.", reply_markup=design)
    elif text=="/iot":
        bot.sendMessage(chat_id, "Unisciti al gruppo ufficiale di Mozilla Italia dedicato allo sviluppo delle IoT.", reply_markup=iot)
    else:
        bot.sendMessage(chat_id, "Errore: comando non riconosciuto", reply_markup=start)


bot=telepot.Bot(TOKEN)
MessageLoop(bot, {'chat': risposte, 'callback_query': risposte}).run_as_thread()

while 1:
    time.sleep(10)
