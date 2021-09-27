#   Coded by D4n13l3k00    #
#     t.me/D4n13l3k00      #
# This code under AGPL-3.0 #
# translate to UA t.me/Daniel_Maklein
from .. import loader
from telethon.tl.types import *


@loader.tds
class ChatStatisticMod(loader.Module):
    "Статистика чату"
    strings = {"name": "ChatStatistic"}

    @loader.owner
    async def statacmd(self, m):
        await m.edit("<b>Рахуєсо...</b>")
        al = str((await m.client.get_messages(m.to_id, limit=0)).total)
        ph = str((await m.client.get_messages(m.to_id, limit=0, filter=InputMessagesFilterPhotos())).total)
        vi = str((await m.client.get_messages(m.to_id, limit=0, filter=InputMessagesFilterVideo())).total)
        mu = str((await m.client.get_messages(m.to_id, limit=0, filter=InputMessagesFilterMusic())).total)
        vo = str((await m.client.get_messages(m.to_id, limit=0, filter=InputMessagesFilterVoice())).total)
        vv = str((await m.client.get_messages(m.to_id, limit=0, filter=InputMessagesFilterRoundVideo())).total)
        do = str((await m.client.get_messages(m.to_id, limit=0, filter=InputMessagesFilterDocument())).total)
        urls = str((await m.client.get_messages(m.to_id, limit=0, filter=InputMessagesFilterUrl())).total)
        gifs = str((await m.client.get_messages(m.to_id, limit=0, filter=InputMessagesFilterGif())).total)
        geos = str((await m.client.get_messages(m.to_id, limit=0, filter=InputMessagesFilterGeo())).total)
        cont = str((await m.client.get_messages(m.to_id, limit=0, filter=InputMessagesFilterContacts())).total)
        await m.edit(
            ("<b>Всього повідомлень:</b> {}\n" +
             "<b>Фотографій:</b> {}\n" +
             "<b>Відео:</b> {}\n" +
             "<b>Музики:</b> {}\n" +
             "<b>Голосовух:</b> {}\n" +
             "<b>Кругляшків:</b> {}\n" +
             "<b>Файлів:</b> {}\n" +
             "<b>Посилань:</b> {}\n" +
             "<b>Гіфок:</b> {}\n" +
             "<b>Координат:</b> {}\n" +
             "<b>Контактів:</b> {}").format(al, ph, vi, mu, vo, vv, do, urls, gifs, geos, cont))
