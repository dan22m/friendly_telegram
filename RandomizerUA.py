#   Coded by D4n13l3k00    #
#     t.me/D4n13l3k00      #
# This code under AGPL-3.0 #
# translate to UA t.me/Daniel_Maklein 
from .. import loader, utils
import re
import random


@loader.tds
class RandomizerMod(loader.Module):
    strings = {"name": "Рандомайзер"}
    prefix = "<b>[Рандомайзер]</b>\n"

    @loader.owner
    async def rndintcmd(self, m):
        ".rndint <int> <int> - рандомне число з вказаного діапазону"
        args = utils.get_args_raw(m)
        check = re.compile(r"^(\d+)\s+(\d+)$")
        if check.match(args):
            fr, to = check.match(args).groups()
            if int(fr) < int(to):
                rndint = random.randint(int(fr), int(to))
                await m.edit(self.prefix+f"<b>Режим:</b> Рандомне число з діапазону\n<b>Діапазон:</b> <code>{fr}-{to}</code>\n<b>Випало число:</b> <code>{rndint}</code>")
            else:
                await m.edit(self.prefix+"Вася, вкажи діапазон чисел!")
        else:
            await m.edit(self.prefix+"Вася, вкажи діапазон чисел!")

    @loader.owner
    async def rndelmcmd(self, m):
        ".rndelm <елементи через кому> - рандомний елемент з списку"
        args = utils.get_args_raw(m)
        if not args:
            await m.edit(self.prefix+"Вася, напиши список елементів через кому!")
            return
        lst = [i.strip() for i in args.split(",") if i]
        await m.edit(self.prefix+f"<b>Режим:</b> Рандомний елемент з списку\n<b>Список:</b> <code>{', '.join(lst)}</code>\n<b>Випало:</b> <code>{random.choice(lst)}</code>")

    @loader.owner
    async def rndusercmd(self, m):
        ".rnduser - вибір рандомного юзера з чата"
        if not m.chat:
            await m.edit(self.prefix+"<b>Це не чат</b>")
            return
        users = await m.client.get_participants(m.chat)
        user = random.choice(users)
        await m.edit(self.prefix+f"<b>Режим:</b> Рандомний юзер з чату\n<b>Юзер:</b> <a href=\"tg://user?id={user.id}\">{user.first_name}</a> | <code>{user.id}</code>")
