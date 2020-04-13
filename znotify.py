import sys
import telepot
import configparser

config = configparser.ConfigParser()
config.read('/usr/lib/zabbix/alertscripts/config.ini')

key = config['TELEGRAM']['key']
user_id = config['TELEGRAM']['user_id']
group_id = config['TELEGRAM']['group_id']

bot = telepot.Bot(key)


def send_telegram(trigger):

    bot.sendMessage(group_id, trigger)


send_telegram(sys.argv[1])
