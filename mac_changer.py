#/usr/bin/python

"""
author : Deaf_Elephant

Program used to change the mac address in Linux OS
Provide an interface and a mac address to get an expected result
Enjoy!

Program based on an example for the course by Zaid Sabih (credit to this guy)

"""

import optparse
import subprocess
import re

def change_mac(interface, mac_address) :
    #attempt to change the mac address based on user's input
    subprocess.call(["ifconfig", interface, "down"])
    subprocess.call(["ifconfig", interface, "hw", "ether", mac_address])
    subprocess.call(["ifconfig", interface, "up"])
    #verify that the MAC has changed
    output = subprocess.check_output(["ifconfig", interface])
    result = re.search(r"\w\w:\w\w:\w\w:\w\w:\w\w:\w\w", output)
    #announce the result to the user
    if mac_address == result.group(0):
        print("[+] MAC address has been modified")
    else:
        print("[-] There was a problem while trying to modify the MAC address")


def set_options():
    #collect user input and provide --help
    parser = optparse.OptionParser()
    parser.add_option("-i", "--interface", help="interface to change a mac address of", dest="interface")
    parser.add_option("-m", "--mac_address", help="new mac_address", dest="mac_address")
    (options, args) = parser.parse_args()
    #verify that user has provided necessary input
    output = subprocess.check_output(["ifconfig", options.interface])

    if not options.interface:
        parser.error("[-] Please provide an interface value")
    elif not options.mac_address :
        parser.error("[-] Please provide a MAC address")

    return options

#modify the mac address
change_mac(set_options().interface, set_options().mac_address)

