from crontab import CronTab
cron = CronTab(user='root')



def newTorrent(command, comment):
	job = cron.new(command=command, comment = comment)
	job.enable()
	cron.write_to_user( user='root' )

	for job in cron:
		print(job)

def removeTorrent(job):
	cron.remove_all(comment = '1')
	cron.write_to_user ( user = 'root')

	for job in cron:
		print(job)


def removeAllTorrents(comment):
	cron.remove_all(comment = comment)
	cron.write_to_user( user = 'root')

	for job in cron:
		print(job)