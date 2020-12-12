#credits to @kraken_the_badass
#beautification credits to @sensei_nex for @senseiMAXprojects

#IMG CREDITS: @WhySooSerious
import asyncio
from telethon import events
from ..utils import admin_cmd, edit_or_reply, sudo_cmd
from . import ALIVE_NAME
from telethon.tl.types import ChannelParticipantsAdmins

# uptime = get_readable_time((time.time() - Lastupdate))
DEFAULTUSER = str(ALIVE_NAME) if ALIVE_NAME else "Unknown"

""" =======================CONSTANTS====================== """
PM_IMG = "https://telegra.ph/file/0a7af73976cdb316feb3f.jpg" 
""" =======================CONSTANTS====================== """
pm_caption = "➣    **🔥 𝐇𝐘𝐏𝐄𝐑-𝐗 𝐁𝐎𝐓 🔥** \n\n"

pm_caption +=  f"➥       **//__↼🄼🄰🅂🅃🄴🅁⇀__//**      \n 『{DEFAULTUSER}』 \n"
pm_caption += " \n"
pm_caption += "✘ ΔβØỮŦ Μ¥ Ş¥ŞŦ€Μ ✘\n\n"
pm_caption += "➾ **𝐓𝐄𝐋𝐄𝐓𝐇𝐎𝐍**  ➣ 𝟏.𝟏𝟕.𝟓\n"
pm_caption += "➾ **𝐂𝐑𝐄𝐀𝐓𝐎𝐑** ➣ ㄒ乇卂爪 卄ㄚ卩乇尺-乂\n"
pm_caption += "➾ **𝐒𝐔𝐏𝐏𝐎𝐑𝐓 ** ➣ [𝐉𝐎𝐈𝐍](https://t.me/joinchat/VhpqURitfHVMgXMeENMPJA)\n"
pm_caption += "➾ **𝐒𝐎𝐂𝐈𝐀𝐋  **  ➣ [𝐉𝐎𝐈𝐍](https://t.me/joinchat/VhpqUVNqdEPbtti4oFovEA)\n"
pm_caption += " \n\n"
pm_caption += "[✨𝔻𝔼ℙ𝕃𝕆𝕐 ℍ𝕐ℙ𝔼ℝ-𝕏 𝔹𝕆𝕋✨](https://github.com/sameerpanthi/HYPER-X) \n"

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
