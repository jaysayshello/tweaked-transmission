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


parser = argparse.ArgumentParser()


#By typing python3 NAME -add instead of python3 NAME -a the former will not need arguments.

parser.add_argument("-p", "--pause", default=0, help='Pauses all torrents')
parser.add_argument("-a", "--add", help="Adds and starts the torrent")
parser.add_argument("-r", "--remove", help="Remove all torrents")
parser.add_argument("-t", "--time", help="Appends a cronjob of the command")


args = parser.parse_args()

def transmission():
	if args.pause:
		os.system('transmission-remote -t all -S')
	if args.add:
		subprocess.call(["transmission-remote","-a", args.add])
	if args.remove: #not working atm
		os.system("transmission-remote -n 'transmission:transmission' -r")
	if args.time:
		with open ("/home/jay/crons/torrents.sh", "a") as myfile:
			myfile.write('python3 /home/jay/python3/get.py -t {}\n'.format(args.time))


if __name__ == '__main__':
	transmission()


#Has to add itself to crontab -e to the bottom of the file
#OR
#Overwrites a .sh file with the command output and then just have a cronjob just run that file always
#	- Con would you be that if you don't clear/delete the .sh file cron will run that will keep running that .sh 

#There will be a preset cronjob that points to a file, so we'll just append to that file
#The torrent will start around 2 AM, brother should be offline by then.

#Will have to stop the rsync cronjob on lord from running the option that checks and deletes files if it doesn't match what lord.