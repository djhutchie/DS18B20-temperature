# DS18B20-temperature

Various python scripts to interface the dallas 1-wire DS18B20 sensor with a Raspberry Pi.

```
temperature_db.py
    logs date and temperature to a sqlite3 db
temperature_file.py
    logs temperature to file (for use with other applications)
temperature_loop.py
    continuous loop outputting to screen
```
## Wiring

```
pinouts for the sensor can be found on the web

pi pins
    rpi pin 1 - 3.3v
    rpi pin 6 - GND
    rpi pin 7 - Data 1 wire interface (dallas)
```

## Enable the One-Wire Interface
```
sudo raspi-config
reboot
sudo modprobe w1-gpio
sudo modprobe w1-therm
cd /sys/bus/w1/devices
ls 
cd 28-{tab}
cat w1_slave
```

## SQL statement
```
select id, datetime(created_at, 'localtime'), temperature from temperature_readings;
```
