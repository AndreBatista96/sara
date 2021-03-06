# -*- coding: utf-8 -*-

from yowsup.layers.protocol_messages.protocolentities import *
import string
from pprint import pprint
from app.mac import mac, signals
from datetime import datetime


@signals.message_received.connect
def __init__(message):
	if message.text == "Não vou hoje":
		now = datetime.now()
		if ((now.hour >= 0) and (now.hour <=12)):
				mac.send_message("Bom dia " + message.who_name + "! Obrigado por avisar", message.conversation)
		if ((now.hour > 12) and (now.hour <= 18)):
				mac.send_message("Boa tarde "+ message.who_name + "! Obrigado por avisar", message.conversation)
		if ((now.hour > 18) and (now.hour <= 24)):
				mac.send_message("Boa noite "+ message.who_name + "! Obrigado por avisar", message.conversation)
	if message.text != "Não vou hoje":
			mac.send_message("Por favor " + message.who_name + ", só responda se irá hoje ou não. Obrigado", message.conversation)
