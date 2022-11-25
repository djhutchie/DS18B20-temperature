import os
import glob
import time
import datetime
import sqlite3
 
os.system('modprobe w1-gpio')
os.system('modprobe w1-therm')
 
base_dir = '/sys/bus/w1/devices/'
device_folder = glob.glob(base_dir + '28*')[0]
device_file = device_folder + '/w1_slave'
 
def read_temp_raw():
    f = open(device_file, 'r')
    lines = f.readlines()
    f.close()
    return lines
 
def read_temp():
    lines = read_temp_raw()
    while lines[0].strip()[-3:] != 'YES':
        time.sleep(0.2)
        lines = read_temp_raw()
    equals_pos = lines[1].find('t=')
    if equals_pos != -1:
        temp_string = lines[1][equals_pos+2:]
        temp_c = float(temp_string) / 1000.0
        # temp_f = temp_c * 9.0 / 5.0 + 32.0
        return temp_c

def create_sqlite_table():
    conn = sqlite3.connect('/home/pi/DS18B20-temperature/temperature_readings.sqlite')
    conn.execute("CREATE TABLE IF NOT EXISTS temperature_readings ( id INTEGER PRIMARY KEY, created_at DATETIME NOT NULL, temperature FLOAT NOT NULL );")
    conn.commit()
    conn.close()

value = round(float(read_temp()), 1)

create_sqlite_table()

conn = sqlite3.connect('/home/pi/DS18B20-temperature/temperature_readings.sqlite')
conn.execute("INSERT INTO temperature_readings values (NULL, CURRENT_TIMESTAMP, " + str(value) + ")")
conn.commit()
conn.close()

print(value)