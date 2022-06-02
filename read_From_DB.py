import sqlite3
from paho.mqtt import client as mqtt_client
import random

#params of mqtt client
broker = 'localhost'
port = 1883
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

def publish(client,topic,msg):
    result = client.publish(topic, msg)
    # result: [0, 1]
    status = result[0]
    if status == 0:
        print(f"Send '{msg}' to topic `{topic}`")
    else:
        print(f"Failed to send message to topic '{topic}'")

# Database Manager Class
con = sqlite3.connect("db.sqlite3")
cur = con.cursor()

cur.execute('SELECT id,value,cmdfromapp FROM MqttApp_motor ORDER BY id DESC LIMIT 1')
motor0 = cur.fetchall()
id_motor0=motor0[0][0]
value_motor0=motor0[0][1]
command_motor0=motor0[0][2]

cur.execute('SELECT id,value,cmdfromapp FROM MqttApp_action ORDER BY id DESC LIMIT 1')
action0 = cur.fetchall()
id_action0=action0[0][0]
value_action0=action0[0][1]
command_action0=action0[0][2]

cur.execute('SELECT id,value,cmdfromapp FROM MqttApp_vanne ORDER BY id DESC LIMIT 1')
vanne0 = cur.fetchall()
id_vanne0=vanne0[0][0]
value_vanne0=vanne0[0][1]
command_vanne0=vanne0[0][2]

cur.close()
#===============================================================
client = connect_mqtt()

while(1):
    con = sqlite3.connect("db.sqlite3")
    cur = con.cursor()
    #function to publish motor data if changed from app
    cur.execute('SELECT id,value,cmdfromapp FROM MqttApp_motor ORDER BY id DESC LIMIT 1')
    myresult = cur.fetchall()
    id_motor=myresult[0][0]
    if(id_motor!=id_motor0):
        id_motor0=id_motor
        value_motor=myresult[0][1]
        command_motor=myresult[0][2]
        if((value_motor!=value_motor0) and (command_motor=='1')):
            publish(client,'motor/cmd',value_motor)
            value_motor0=value_motor

    #function to publish vanne data if changed from app
    cur.execute('SELECT id,value,cmdfromapp FROM MqttApp_vanne ORDER BY id DESC LIMIT 1')
    myresult = cur.fetchall()
    id_vanne=myresult[0][0]
    if(id_vanne!=id_vanne0):
        id_vanne0=id_vanne
        value_vanne=myresult[0][1]
        command_vanne=myresult[0][2]
        if((value_vanne!=value_vanne0) and (command_vanne=='1')):
            publish(client,'vanne/cmd',value_vanne)
            value_vanne0=value_vanne

    #function to publish action data if changed from app
    cur.execute('SELECT id,value,cmdfromapp FROM MqttApp_action ORDER BY id DESC LIMIT 1')
    myresult = cur.fetchall()
    id_action=myresult[0][0]
    if(id_action!=id_action0):
        id_action0=id_action
        value_action=myresult[0][1]
        command_action=myresult[0][2]
        if((value_action!=value_action0) and (command_action=='1')):
            publish(client,'action/cmd',value_action)
            value_action0=value_action