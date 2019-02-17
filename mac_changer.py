import optparse
import subprocess

subprocess.run(["ifconfig", "eth0", "hw", "ether", "22:33:33:44:55:A2"])