import random
from paho.mqtt import client as mqtt_client
from store_Sensor_Data_to_DB import sensor_Data_Handler

broker = 'localhost'
port = 1883
# generate client ID with pub prefix randomly
client_id = f'python-mqtt-{random.randint(0, 100)}'
username = 'client11'
password = 'hivemq11'
def connect_mqtt() -> mqtt_client:
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


def subscribe(client: mqtt_client):
    def on_message(client, userdata, msg):
        print(f"Received `{msg.payload.decode()}` from `{msg.topic}` topic")
        sensor_Data_Handler(msg.topic, msg.payload)
    client.subscribe("presion")
    client.on_message = on_message
    client.subscribe("msg")
    client.on_message = on_message
    client.subscribe("action")
    client.on_message = on_message
    client.subscribe("temp")
    client.on_message = on_message
    client.subscribe("motor")
    client.on_message = on_message
    client.subscribe("vanne")
    client.on_message = on_message


def run():
    
    client = connect_mqtt()
    subscribe(client)
    client.loop_forever()


if __name__ == '__main__':
    run()

