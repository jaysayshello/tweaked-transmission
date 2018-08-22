#A script to easily install and save the file
#onto my HDD so I can access it on my PLEX server.
import subprocess
import sys
import os
import argparse

#Has to be done by Tuesdaaay
#Options like where to save the torrent
#Pass the torrent link
#wiLL run tranmssion on whatever host it is active on so will use this tool for lyr most likely

#will this fucking update ???



parser = argparse.ArgumentParser()


#By typing python3 NAME -add instead of python3 NAME -a the former will not need arguments.

parser.add_argument("-p", "--pause", default=0, help='Pauses all torrents')
parser.add_argument("-a", "--add", help="Adds and starts the torrent")
parser.add_argument("-r", "--remove", help="Remove all torrents")


args = parser.parse_args()

def transmission():
	if args.pause:
		os.system('transmission-remote -t all -S')
	if args.add:
		#torrentLink = input('Please enter the torrent link \n')
		p2 = subprocess.call(["transmission-remote","-a", args.add])
	if args.remove:
		os.system("transmission-remote -n 'transmission:transmission' -r")


if __name__ == '__main__':
	transmission()

