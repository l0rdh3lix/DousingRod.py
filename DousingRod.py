from sys import argv
import subprocess

prompt = '> '

print "What is the SSID of target AP? (case sensitive) "
Rssid = raw_input(prompt)

print "What is the MAC address of the target AP? format input aa:bb:cc:dd:ee:ff "
Rmac_addr = raw_input(prompt)

"Searching for SSID: %r" % Rssid
"At MAC Address: %r" % Rmac_addr

subprocess.call (["kismet", "-l", "-c", "wlan0", "--use-gpsd-gps", "/dev/ttyACM0"])
