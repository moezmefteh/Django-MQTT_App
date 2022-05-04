import random
import time
from paho.mqtt import client as mqtt_client

broker = 'localhost'
port = 1883
# generate client ID with pub prefix randomly
client_id = f'python-mqtt-{random.randint(0, 1000)}'
username = 'client0'
password = 'hivemq0'

def connect_mqtt():
    def on_connect(client, userdata, flags, rc):
        if rc == 0:
            print("Connected to MQTT Broker!")
        else:
            print("Failed to connect, return code %d\n", rc)

    client = mqtt_client.Client(client_id)
    client.username_pw_set(username, password)
    client.on_connect = on_connect
    client.connect(broker, port)
    return client


def publish(client):
    msg_count = 0
    action=0
    while True:
        time.sleep(4)
        action=not(action)
        msg = f"{msg_count}"
        temp=float(msg)+0.2
        motor = int(action)
        result = client.publish("presion", msg)
        result = client.publish("action", action)
        result = client.publish("temp", temp)
        result = client.publish("motor", motor)

        # result: [0, 1]
        status = result[0]
        if status == 0:
            print(f"Send `{msg}` to topic `{'presion'}`")
            print(f"Send `{action}` to topic `{'action'}`")
            print(f"Send `{temp}` to topic `{'temp'}`")
            print(f"Send `{motor}` to topic `{'motor'}`")

        else:
            print(f"Failed to send messages")
        msg_count += 1

def run():
    client = connect_mqtt()
    client.loop_start()
    publish(client)

if __name__ == '__main__':
    run()

