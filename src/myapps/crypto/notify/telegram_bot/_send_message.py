# -*- coding: utf-8 -*-
from telegram.ext import Updater
from myapps.crypto.notify.telegram_bot._conf import TOKEN, CHAT_ID

from myapps.crypto.models import Stat, RuleMap, Notification


def send(token, chat_id, text):
    # Create the EventHandler and pass it your bot's token.
    updater = Updater(token=token)

    # Send single message (no bot looping)
    updater.bot.send_message(chat_id=chat_id, text=text)


# Must be refactored
def rule_manager(rule, notify_list, **kwargs):

    send_message = str()

    if rule == 'pump_dump':
        current = notify_list[0].rule.get_res_data()
        condition = notify_list[0].condition
        pair = notify_list[0].rule.stat
        period = kwargs['period'] if 'period' in kwargs else None

        if abs(float(current['result'])) >= float(condition['target']):
            send_message = '{0}; {1}; period {2}; {3}%'.format(pair, 'pump_dump', period, current['result'])

    elif rule == 'price_change_percent':
        current = float(notify_list[0].rule.result['priceChangePercent'])
        target = float(notify_list[0].condition['target'])
        pair = notify_list[0].rule.stat

        if target >= 0.0:
            if current >= target:
                send_message = '{0}; {1}; {2}%'.format(pair, '24h_price_change', current)

        else:
            if current <= target:
                send_message = '{0}; {1}; {2}%'.format(pair, '24h_price_change', current)

    return send_message or None


def get_message():

    # Get list of Stat objects with [Send notification = ON]
    stats_notify_on = Stat.objects.filter(notification='ON').filter(status='AC')

    # Get list of RuleMaps for each Stat objects (status=AC)
    if len(stats_notify_on) > 0:

        for current_stat in stats_notify_on:
            rule_maps = RuleMap.objects.filter(stat=current_stat).filter(status='AC')

            # Get notification data
            if len(rule_maps) > 0:

                for current_rule in rule_maps:
                    notify_list = Notification.objects.filter(rule=current_rule).filter(status='AC')

                    # rule name = current.rule.rule
                    if len(notify_list) > 0:

                        message_to_send = rule_manager(current_rule.rule.rule, notify_list, period=current_stat.period)

                        # Send message if it exists
                        if message_to_send:

                            # Send to telegram
                            if str(notify_list[0].send_to) == 'telegram':
                                send(TOKEN, CHAT_ID, message_to_send)


def run():
    print('1. Send message process is started')
    get_message()
    print('2. Send message process is completed')
