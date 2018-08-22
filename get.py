#A script to easily install and save the file
#onto my HDD so I can access it on my PLEX server.
import subprocess
import sys
import os

#Has to be done by Tuesdaaay
#Options like where to save the torrent
#Pass the torrent link
#wiLL run tranmssion on whatever host it is active on so will use this tool for lyr most likely


#Going to make this a CLT instead, so it will work with cron jobs better
#Also going to make a repo for this



def getLink():
	#magnetLink = input('Enter the mangent link. \n')
	#os.system('sudo service transmission-daemon status')
	



	print ('Enter 1; to stop the torrents.')
	print('Enter 2; start a new torrent')
	print ('Enter 3; to exit.')

	choice = int(input('Enter your choice\n'))

	if (choice == 1):
		os.system('transmission-remote -t all -S')
	if (choice == 2):
		torrentLink = input('Please enter the torrent link \n')
		p2 = subprocess.call(["transmission-remote","-a",torrentLink])
	print("Process started.")

	if (choice == 3):
		exit()
		#os.chdir work solely in this program won't change the active directory in terminal.
		#os.chdir("/mnt/backup/media/")
		#os.system("pwd")

	#p1 = subprocess.call(["transmiåssion-remote", "--auth", "transmission:transmission","-a", "{}".format(magnetLink)])
	#p.kill()
    #p2 = subprocess.Popen(["curl", "icanhazip.com"])

def main():
    print ("Transmission-Remote")
    getLink()




if  __name__ == "__main__":
    main()
