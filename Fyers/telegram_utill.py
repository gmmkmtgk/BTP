import telegram
import logging as logger
import traceback as trace
from ..core.config import TELEGRAM_TOKEN


#Get Group Chat ID and further details from below given  API link
#https://api.telegram.org/bot704938461:AAEZI6YfeRHIEVW3hTfdvKQXU4ss5KNpWSI/getme
#https://api.telegram.org/bot704938461:AAEZI6YfeRHIEVW3hTfdvKQXU4ss5KNpWSI/getUpdates


def strategyExec(payload,data=None,parse_mode=None):

    bot = telegram.Bot(TELEGRAM_TOKEN)

    #print("Message to be notified.",data)


    #Below coce is for general notification
    message = "<strong>STOCKBUDDY 2.0 NOTIFICATION !!</strong> \n"
    message += " Just now <strong>"+payload.username+"</strong> have executed strategy : <strong>"+payload.strategy_name+"</strong>."
    message += "\n Here is a Application <a href='https://tinyurl.com/stockbuddy'> link</a> for your quick access."

    #bot.send_message(chat_id=DEV_CHAT_ID,text=message,parse_mode=telegram.ParseMode.HTML)

    #Below code to send generated signal notifications
    if(data != None):
        signal_data = data['data']
        for index, signal in enumerate(signal_data, 1):
            #print(signal)
            signal_generated = signal['date']
            signal_type = signal['signal']
            symbol = signal['symbol']
            entry = signal['entry_val']
            exit = signal['exit_stop_loss_val']

            message = "<strong>STOCKBUDDY 2.0 NOTIFICATION !!</strong> \n"
            message += "Signal Generated for strategy : <strong>"+payload.strategy_name+"</strong> of <strong>"+payload.username+"</strong> user."
            message += "<strong>\n Symbol : "+symbol
            message += "\n Identified On : "+signal_generated
            message += "\n Signal : "+signal_type
            message += "\n Suggested Entry : "+ str(entry)
            message += "\n Suggested Exit : "+ str(exit)+"</strong>"
            message += "\n Here is a Application <a href='https://tinyurl.com/stockbuddy'> link</a> for your quick access."

            bot.send_message(chat_id=STOCK_BUDDY_CORE_CHAT_ID,text=message,parse_mode=telegram.ParseMode.HTML)

def sendOrderNotification(order_info,user_chat_id):

    try:
        bot = telegram.Bot(TELEGRAM_TOKEN)

        if(len(order_info)>0):
            #Below coce is for general notification
            message = "<strong>STOCKBUDDY 2.0 NOTIFICATION !!</strong> \n"
            for info in order_info:
                message += "\n "+info
                message += "\n ==============="
            #message += order_info
            #message += "\n Here is a Application <a href='https://tinyurl.com/stockbuddy'> link</a> for your quick access."
            for chat_id in user_chat_id:
                bot.send_message(chat_id=chat_id,text=message,parse_mode=telegram.ParseMode.HTML)
                #logger.info("Sending Message :"+str(chat_id))

    except Exception as e:
        logger.error("An error occured during sending a notification ..")
        logger.error(e)
        logger.error(trace.print_exc())


def sendMemberNotification(message_info,user_chat_id):

    try:
        bot = telegram.Bot(TELEGRAM_TOKEN)

        #Below coce is for general notification
        #message = "<strong>STOCKBUDDY 2.0 NOTIFICATION !!</strong>"
        message = message_info
        #message += "\n Here is a Application <a href='https://tinyurl.com/stockbuddy'> link</a> for your quick access."

        for chat_id in user_chat_id:
            bot.send_message(chat_id=chat_id,text=message,parse_mode=telegram.ParseMode.HTML)
            #logger.info("Sending Message :"+str(chat_id))

    except Exception as e:
        logger.error("An error occured during sending a notification ..")
        logger.error(e)
        logger.error(trace.print_exc())
