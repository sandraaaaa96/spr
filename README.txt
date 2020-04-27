0. set up sopare
1. git clone repo into sopare
2. copy out files into sopare
3. Permissions:
	chmod +x writefiles.py
	chmod +x logging.sh
4. cronjob
	crontab -e
	in the last line input:
	@reboot bash logging.sh