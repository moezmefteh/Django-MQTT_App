from datetime import datetime
import pytz
import sqlite3
from pathlib import Path
# SQLite DB Name
BASE_DIR = Path(__file__).resolve().parent.parent
DB_Name =  BASE_DIR / 'db.sqlite3'

#===============================================================
# Database Manager Class

class DatabaseManager():
	def __init__(self):
		self.conn = sqlite3.connect(DB_Name)
		self.conn.execute('pragma foreign_keys = on')
		self.conn.commit()
		self.cur = self.conn.cursor()
		
	def add_del_update_db_record(self, sql_query, args=()):
		self.cur.execute(sql_query, args)
		self.conn.commit()
		return

	def __del__(self):
		self.cur.close()
		self.conn.close()

#===============================================================
# Functions to push Sensor Data into Database

# Function to save presion to DB Table
def presion_Data_Handler(jsonData):
	#Parse Data 
	#json_Dict = json.loads(jsonData)
	#SensorID = json_Dict['Sensor_ID']
	#Data_and_Time = datetime.now().strftime("%d-%m-%Y %H:%M:%S")
	tz_London = pytz.timezone('Europe/London')
	Data_and_Time = datetime.now(tz_London)
	presion = jsonData
	
	#Push into DB Table
	dbObj = DatabaseManager()
	dbObj.add_del_update_db_record("insert into MqttApp_presion(pub_date,value) values (?,?)",[Data_and_Time,presion])
	del dbObj
	print ("Inserted presion Data into Database.")

# Function to save msg to DB Table
def msg_Data_Handler(jsonData):

	tz_London = pytz.timezone('Europe/London')
	Data_and_Time = datetime.now(tz_London)
	msg = jsonData
	
	#Push into DB Table
	dbObj = DatabaseManager()
	dbObj.add_del_update_db_record("insert into MqttApp_msg(pub_date,value) values (?,?)",[Data_and_Time,msg])
	del dbObj
	print ("Inserted msg Data into Database.")
	print ("")

# Function to save action to DB Table
def action_Data_Handler(jsonData):
	tz_London = pytz.timezone('Europe/London')
	Data_and_Time = datetime.now(tz_London)
	action = jsonData
	
	#Push into DB Table
	dbObj = DatabaseManager()
	dbObj.add_del_update_db_record("insert into MqttApp_action(pub_date,value) values (?,?)",[Data_and_Time,action])
	del dbObj
	print ("Inserted action Data into Database.")
	print ("")

# Function to save temperature to DB Table
def temp_Data_Handler(jsonData):
	tz_London = pytz.timezone('Europe/London')
	Data_and_Time = datetime.now(tz_London)
	temp = jsonData
	
	#Push into DB Table
	dbObj = DatabaseManager()
	dbObj.add_del_update_db_record("insert into MqttApp_temp(pub_date,value) values (?,?)",[Data_and_Time,temp])
	del dbObj
	print ("Inserted temp Data into Database.")
	print ("")
#===============================================================
# Master Function to Select DB Funtion based on MQTT Topic

def sensor_Data_Handler(Topic, jsonData):
	if Topic == "presion":
		presion_Data_Handler(jsonData)
	elif Topic == "msg":
		msg_Data_Handler(jsonData)	
	elif Topic == "action":
		action_Data_Handler(jsonData)
	elif Topic == "temp":
		temp_Data_Handler(jsonData)

#===============================================================
