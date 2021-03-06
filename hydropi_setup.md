### Wlan
sudo nano /etc/wpa_supplicant/wpa_supplicant.conf

```
network={
    ssid="testing"
    psk="testingPassword"
}
```

### SSH
sudo /etc/init.d/ssh start
sudo update-rc2.d ssh defaults
sudo update-rc2.d ssh enable
sudo systemctl enable ssh

### InfluxDB Grafana
https://www.circuits.dk/install-grafana-influxdb-raspberry/
```
curl -sL https://repos.influxdata.com/influxdb.key | sudo apt-key add -
source /etc/os-release
test $VERSION_ID = "7" && echo "deb https://repos.influxdata.com/debian wheezy stable" | sudo tee /etc/apt/sources.list.d/influxdb.list
test $VERSION_ID = "8" && echo "deb https://repos.influxdata.com/debian jessie stable" | sudo tee /etc/apt/sources.list.d/influxdb.list
```

```
sudo apt-get update && sudo apt-get install influxdb
sudo service influxdb start
```
/etc/influxdb/influxdb.conf

### Python
```
apt-get install python-pip
pip install pyserial
```

### Cron Job
/etc/cron.d/
run-parts /etc/cron.daily
