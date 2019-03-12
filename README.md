# Tweaked-Transmission

Eventually this will make using Transmission easier. The main thing of importance is allowing users to set a time in which to start a torrent using cronjobs within this tool. Essentially a better transmission-remote.

#Transmission Settings

Please replace your current transmission settings with the the one provided in the repo, it'll save you from headaches.

OR

First shutdown Transmission

`sudo service transmission-daemon stop`

Then edit your `settings.json`, set the below to false.

`sudo nano /var/lib/transmission-daemon/info/settings.json`

`"rpc-authentication-required": false,`

lastly boot up Transmission again.

`sudo service transmission-daemon start`


# Current requriements
cronjob

# Setup
Must first create a cronjob via crontab -e, that points to a file named torrents.sh, the script will append to torrents.sh.



magnet:?xt=urn:btih:b7383a0b91a478d0570e5a5ad23fedc496dafae1&dn=Linkin+Park+-+Hybrid+Theory+Live+Bonus++2019+ak&tr=udp%3A%2F%2Ftracker.leechers-paradise.org%3A6969&tr=udp%3A%2F%2Fzer0day.ch%3A1337&tr=udp%3A%2F%2Fopen.demonii.com%3A1337&tr=udp%3A%2F%2Ftracker.coppersurfer.tk%3A6969&tr=udp%3A%2F%2Fexodus.desync.com%3A6969