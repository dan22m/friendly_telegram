# @Sekai_Yoney
# translate tg @Daniel_Maklein | git dan22m
﻿from .. import loader, utils


def register(cb):
    cb(TikTokMod())

class TikTokMod(loader.Module):
    """Качаємо відео без водяного знаку в Тік Ток."""
    strings = {'name': 'TikTok'}

    async def tikcmd(self, message):
        """.tik посилання на відео."""
        await utils.answer(message, 'Щя...')
        args = utils.get_args_raw(message)
        if not args:
            await utils.answer(message, "А де посилання??")
            return
        r = await message.client.inline_query('tikdobot', args)
        await message.client.send_file(message.to_id, r[1].result.content.url)
        await message.delete() 
