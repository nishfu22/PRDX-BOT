from time import sleep
from userbot import CMD_HELP
from userbot.events import register


@register(outgoing=True, pattern='^.jelek(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    sleep(2)
    await typew.edit("`Pertama-tama kamu jelek`")
    sleep(2)
    await typew.edit("`Kedua kamu emang jelek`")
    sleep(1)
    await typew.edit("`Dan yang terakhir ngapain kamu idup`")

# Create by myself @localheart


@register(outgoing=True, pattern='^.punten(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    await typew.edit("`\n┻┳|―-∩`"
                     "`\n┳┻|     ヽ`"
                     "`\n┻┳|    ● |`"
                     "`\n┳┻|▼) _ノ`"
                     "`\n┻┳|￣  )`"
                     "`\n┳ﾐ(￣ ／`"
                     "`\n┻┳T￣|`"
                     "\n**Punten**")

# Create by myself @localheart


@register(outgoing=True, pattern='^.pantau(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    await typew.edit("`\n┻┳|―-∩`"
                     "`\n┳┻|     ヽ`"
                     "`\n┻┳|    ● |`"
                     "`\n┳┻|▼) _ノ`"
                     "`\n┻┳|￣  )`"
                     "`\n┳ﾐ(￣ ／`"
                     "`\n┻┳T￣|`"
                     "\n**Masih Ku Pantau**")


# Create by myself @localheart


@register(outgoing=True, pattern='^.idiot(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    await typew.edit("\n╭╮╱╱╭╮"
                     "\n┃╰╮╭╯┃"
                     "\n╰╮╰╯╭┻━┳╮╭╮"
                     "\n╱╰╮╭┫╭╮┃┃┃┃"
                     "\n╱╱┃┃┃╰╯┃╰╯┃"
                     "\n╱╱╰╯╰━━┻━━╯"
                     "\nㅤㅤㅤ"
                     "\n╭━━━╮"
                     "\n┃╭━╮┃"
                     "\n┃┃╱┃┣━┳━━╮"
                     "\n┃╰━╯┃╭┫┃━┫"
                     "\n┃╭━╮┃┃┃┃━┫"
                     "\n╰╯╱╰┻╯╰━━╯"
                     "\nㅤㅤㅤ"
                     "\n╭━━━╮╱╭╮╱╱╱╭╮"
                     "\n┃╭━━╯╱┃┃╱╱╭╯╰╮"
                     "\n┃╰━━┳━╯┣┳━┻╮╭╯"
                     "\n┃╭━━┫╭╮┣┫╭╮┃┃"
                     "\n┃╰━━┫╰╯┃┃╰╯┃╰╮"
                     "\n╰━━━┻━━┻┻━━┻━╯"
                     "\nㅤㅤㅤ"
                     "\n╭━╮╱╭╮"
                     "\n┃┃╰╮┃┃"
                     "\n┃╭╮╰╯┣━━╮"
                     "\n┃┃╰╮┃┃╭╮┃"
                     "\n┃┃╱┃┃┃╰╯┃"
                     "\n╰╯╱╰━┻━━╯"
                     "\nㅤㅤㅤ"
                     "\n╭━━━╮╱╱╱╱╱╭╮╱╭╮"
                     "\n╰╮╭╮┃╱╱╱╱╱┃┃╭╯╰╮"
                     "\n╱┃┃┃┣━━┳╮╭┫╰┻╮╭╯"
                     "\n╱┃┃┃┃╭╮┃┃┃┃╭╮┃┃"
                     "\n╭╯╰╯┃╰╯┃╰╯┃╰╯┃╰╮"
                     "\n╰━━━┻━━┻━━┻━━┻━╯")


CMD_HELP.update({
    "animasi2":
    "𝘾𝙤𝙢𝙢𝙖𝙣𝙙: `.sadboy`\
    \n↳ : Biasalah sadboy hikss\
    \n\n𝘾𝙤𝙢𝙢𝙖𝙣𝙙: `.punten` dan `.pantau`\
    \n↳ : Coba aja hehehe.\
    \n\n𝘾𝙤𝙢𝙢𝙖𝙣𝙙: `.idiot`\
    \n↳ : u're ediot xixixi.\
    \n\n𝘾𝙤𝙢𝙢𝙖𝙣𝙙: `kosong`\
    \n↳ : Tunggu update selanjutnya kawan."
})
