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
        time.sleep(3)
        action=not(action)
        msg = f"{msg_count}"
        temp=float(msg)+0.2
        presion = int(action)
        result = client.publish("presion/cmd", msg)
        result = client.publish("action/cmd", msg)
        result = client.publish("temp/cmd", msg)
        result = client.publish("motor/cmd", action)
        result = client.publish("vanne/cmd", action)
        result = client.publish("msg/cmd", msg)

        # result: [0, 1]
        status = result[0]
        if status == 0:
            print(f"Send `{presion}` to topic `{'presion/cmd'}`")
            print(f"Send `{msg}` to topic `{'action/cmd'}`")
            print(f"Send `{temp}` to topic `{'temp/cmd'}`")
            print(f"Send `{action}` to topic `{'motor/cmd'}`")
            print(f"Send `{action}` to topic `{'vanne/cmd'}`")
            print(f"Send `{msg}` to topic `{'msg/cmd'}`")
        else:
            print(f"Failed to send messages")
        msg_count += 1

def run():
    client = connect_mqtt()
    client.loop_start()
    publish(client)

if __name__ == '__main__':
    run()

