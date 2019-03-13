#A script to easily install and save the file
#onto my HDD so I can access it on my PLEX server.
import subprocess
import sys
import os
import argparse
from crontab import CronTab
import cron



parser = argparse.ArgumentParser()

#Using acton="store_true" keyword allows the optional argument to pass with out added args.



parser.add_argument("-p", "--pause", action="store_true", default=0, help='Pauses all torrents')
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



#this is actually useful, has to be redesigned but the idea is sound
#		if args.time:		
 #		with open ("/home/jay/crons/torrents.sh", "a") as myfile:		
# 			myfile.write('transmission-remote -a {}\n'.format(args.time))		
# 	if args.clear:		
# 		os.system("rm -r /home/jay/crons/torrents.sh")		
# 		f= open("/home/jay/crons/torrents.sh", "w+")


if __name__ == '__main__':
	transmission()


