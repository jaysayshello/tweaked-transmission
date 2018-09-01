#A script to easily install and save the file
#onto my HDD so I can access it on my PLEX server.
import subprocess
import sys
import os
import argparse
from crontab import CronTab
import cron



parser = argparse.ArgumentParser()



parser.add_argument("-p", "--pause", default=0, help='Pauses all torrents')
parser.add_argument("-a", "--add", help="Adds and starts the torrent")
parser.add_argument("-r", "--remove", help="Remove all torrents from list completed and incomplete")
parser.add_argument("-t", "--time", help="Appends a cronjob of the command")
parser.add_argument("-s", "--setup", help="Configuration of tool")
parser.add_argument("-c", "--comment", help="Comment to torrent")
parser.add_argument("-z", "--clearall", help="clear all torrents")
#parser.add_agrument("--config", help="Sets up the cron directory")


args = parser.parse_args()

def transmission():
	if args.pause:
		os.system('transmission-remote -t all -S')
	if args.add:
		subprocess.call(["transmission-remote","-a", args.add])
	if args.remove: 
		cron.removeTorrent(args.remove)
	if args.time:
		cron.newTorrent(args.time,args.comment)
	if args.clearall:
		cron.removeAllTorrents(args.clearall)

	#if args.setup:
		#some dictionary shit saved to a file in the same directory as the python script


if __name__ == '__main__':
	transmission()


