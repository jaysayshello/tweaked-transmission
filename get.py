#A script to easily install and save the file
#onto my HDD so I can access it on my PLEX server.
import subprocess
import sys
import os
import argparse


#Options like where to save the torrent
#wiLL run tranmssion on whatever host it is active on so will use this tool for lyr most likely


parser = argparse.ArgumentParser()


#By typing python3 NAME -add instead of python3 NAME -a the former will not need arguments.

parser.add_argument("-p", "--pause", default=0, help='Pauses all torrents')
parser.add_argument("-a", "--add", help="Adds and starts the torrent")
#parser.add_argument("-r", "--remove", help="Remove all torrents from list completed and incomplete")
parser.add_argument("-t", "--time", help="Appends a cronjob of the command")
parser.add_argument("-c", "--clear", help="Clears all torrents in cron")


args = parser.parse_args()

def transmission():
	if args.pause:
		os.system('transmission-remote -t all -S')
	if args.add:
		subprocess.call(["transmission-remote","-a", args.add])
	#if args.remove: 
		#os.system("transmission-remote --torrent all --stop")
	if args.time:
		with open ("/home/jay/crons/torrents.sh", "a") as myfile:
			myfile.write('transmission-remote -a {}\n'.format(args.time))
	if args.clear:
		os.system("rm -r /home/jay/crons/torrents.sh")
		f= open("/home/jay/crons/torrents.sh", "w+")


if __name__ == '__main__':
	transmission()


#Has to add itself to crontab -e to the bottom of the file
#OR
#Overwrites a .sh file with the command output and then just have a cronjob just run that file always
#	- Con would you be that if you don't clear/delete the .sh file cron will run that will keep running that .sh 

#There will be a preset cronjob that points to a file, so we'll just append to that file
#The torrent will start around 2 AM, brother should be offline by then.

#Will have to stop the rsync cronjob on lord from running the option that checks and deletes files if it doesn't match what lord.


#NEXT MOVE
#Create config file for all the directory shit, maybe make it a dictionary??? So wherever there is a directory it'll use that.
#Also will have to make a config option people can use to setup there shit

#to write the dictionary file (json) to a file to read from
#https://stackoverflow.com/questions/36965507/writing-a-dictionary-to-a-text-file-in-python