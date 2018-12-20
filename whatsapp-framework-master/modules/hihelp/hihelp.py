from app.mac import mac, signals

'''
Signals this module listents to:
1. When a message is received (signals.command_received)
==========================================================
'''
@signals.command_received.connect
def handle(message):
	if message.text == "hi":
	 mac.send_message("Hello", message.conversation)
    
