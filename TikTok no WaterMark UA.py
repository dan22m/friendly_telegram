from .. import loader, utils


def register(cb):
    cb(TikTokMod())

class TikTokMod(loader.Module):
    """Завантажуємо відео без їбаної реклами тт"""
    strings = {'name': 'TikTok no WaterMark'}

    async def tikcmd(self, message):
        """Кидає тобі в їбало відео без їбаної реклами тт"""
        await utils.answer(message, 'Та зачекай...')
        args = utils.get_args_raw(message)
        if not args:
            await utils.answer(message, "А лінк я звідки візьму? А? Забув?")
            return
        r = await message.client.inline_query('tikdobot', args)
        await message.client.send_file(message.to_id, r[1].result.content.url)
        await message.delete()
