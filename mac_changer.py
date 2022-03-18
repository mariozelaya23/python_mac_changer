#!/usr/bin/env python3

import subprocess
import optparse
# optparse get the arguments from user and parse them to our code

parser = optparse.OptionParser()

parser.add_option("-i", "--interface", dest="interface", help="Interface to change its MAC address")

parser.parse_args()

interface = input("Enter the interface > ")
new_mac = input("New mac > ")

print("[+] Changing MAC address for " + interface + " to " + new_mac)

subprocess.call(["ifconfig", interface, "down"])
subprocess.call(["ifconfig", interface, "hw", "ether", new_mac])
subprocess.call(["ifconfig", interface, "up"])

