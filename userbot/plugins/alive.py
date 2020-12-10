import asyncio
from telethon import events
from uniborg.util import admin_cmd
from userbot import ALIVE_NAME
from telethon.tl.types import ChannelParticipantsAdmins

# uptime = get_readable_time((time.time() - Lastupdate))
DEFAULTUSER = str(ALIVE_NAME) if ALIVE_NAME else "Unknown"

""" =======================CONSTANTS====================== """
        PM_IMG = "https://telegra.ph/file/c2c44df2e47dd6934ad75.jpg" 
""" =======================CONSTANTS====================== """
        pm_caption += pm_caption +=  f"➥       **//__↼🄼🄰🅂🅃🄴🅁⇀__//**      \n 『{DEFAULTUSER}』 \n"
        pm_caption += " \n\n"
        pm_caption += "✘ ΔβØỮŦ Μ¥ Ş¥ŞŦ€Μ ✘\n\n"
        pm_caption += "➾ **𝐓𝐄𝐋𝐄𝐓𝐇𝐎𝐍**  ➣ 𝟏.𝟏𝟕.𝟓\n"
        pm_caption += "➾ **𝐒𝐔𝐏𝐏𝐎𝐑𝐓 ** ➣ [𝐉𝐎𝐈𝐍](https://t.me/joinchat/VhpqURitfHVMgXMeENMPJA)\n"
        pm_caption += "➾ **𝐒𝐎𝐂𝐈𝐀𝐋  **  ➣ [𝐉𝐎𝐈𝐍](https://t.me/joinchat/VhpqUVNqdEPbtti4oFovEA)\n"
        pm_caption += "➾ **𝐂𝐑𝐄𝐀𝐓𝐎𝐑** ➣ [⚡𝐒𝐀𝐌𝐄𝐄𝐑⚡](@sameer_795)\n\n" 
        pm_caption += "➾ **𝐌𝐀𝐈𝐍𝐓𝐀𝐈𝐍 𝐁𝐘** ➣ ⭐🌟 T͙E͙A͙M͙ N͙E͙X͙T͙ L͙E͙V͙E͙L͙ 🌟⭐\n\n" 
        pm_caption += " \n\n"
        pm_caption += "[✨ 𝐑𝐄𝐏𝐎 ✨](@SAMEER_795) \n"

        @borg.on(admin_cmd(pattern=r"alive"))
async def friday(alive):
    chat = await alive.get_chat()
    """ For .alive command, check if the bot is running.  """
    
    await borg.send_file(alive.chat_id, PM_IMG,caption=pm_caption)
    await alive.delete()


    
@borg.on(admin_cmd(pattern=r"Alive", allow_sudo=True))
async def friday(alive):
    chat = await alive.get_chat()
    """ For .alive command, check if the bot is running.  """
    await borg.send_file(alive.chat_id, PM_IMG,caption=pm_caption)
