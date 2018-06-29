import RPi.GPIO as GPIO
import time
import datetime
import json
import paho.mqtt.client as mqtt

GPIO.setwarnings(False)
SENSOR_PIN = 12
GPIO.setmode(GPIO.BOARD)
GPIO.setup(SENSOR_PIN, GPIO.IN, pull_up_down=GPIO.PUD_UP)

msg = {}
IP_MQTT='127.0.0.1'

while True:
	ts = time.time()
	st = datetime.datetime.fromtimestamp(ts).strftime('%d/%m/%Y %H:%M:%S')
	if (GPIO.input(SENSOR_PIN) == 0):
		print('Luz acessa')
		msg['horario'] = st
		msg['estado'] = 'acessa'
	else:
		print('Luz apagada')
		msg['horario'] =  st
		msg['estado'] = 'apagada'
	try:
		mqttc = mqtt.Client()
		mqttc.connect(IP_MQTT, 1883)
		mqttc.publish('sensor-ldr', json.dumps(msg))
		print('enviou mensagem')
		#mqttc.loop(2)
	except Exception:
		print('MQTT fora do ar')
	time.sleep(10)

