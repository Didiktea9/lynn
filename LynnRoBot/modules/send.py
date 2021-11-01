

from telegram.ext import run_async


from LynnRoBot import dispatcher

from LynnRoBot.modules.disable import DisableAbleCommandHandler
from LynnRoBot.modules.helper_funcs.alternate import send_message
from LynnRoBot.modules.helper_funcs.chat_status import user_admin


@run_async
@user_admin
def send(update, context):
    args = update.effective_message.text.split(None, 1)
    creply = args[1]
    send_message(update.effective_message, creply)




# Stats Module





ADD_CCHAT_HANDLER = DisableAbleCommandHandler("snd", send)
dispatcher.add_handler(ADD_CCHAT_HANDLER)
__command_list__ = ["snd"]
__handlers__ = [ADD_CCHAT_HANDLER]
