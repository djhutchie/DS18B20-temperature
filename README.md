# DS18B20-temperature

## Wiring

```
pinouts can be found on the web
    pin 1 - 3.3v
    pin 6 - GND
    pin 7 - Data 1 wire interface (dallas)
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
