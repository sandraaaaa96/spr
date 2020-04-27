0. set up sopare
	https://www.bishoph.org/step-by-step-raspberry-pi-offline-voice-recognition-with-sopare/
1. git clone repo into sopare
	git clone https://github.com/sandraaaaa96/spr.git
2. copy out files into sopare
	cd sopare
	cd spr
	cp cough.log ~/sopare
	cp logging.sh ~/sopare
	cp writefiles.py ~/sopare
	cp upload.sh ~
3. Permissions:
	Ensure you are in sopare folder
	chmod +x writefiles.py
	chmod +x logging.sh
4. Make sure cough.log, logging.sh and writefiles.py are in sopare and logging.sh and writefiles.py have been granted permissions
	i.e. type ls into command prompt > logging.sh and writefiles.py are green, cough.log exists
5. Install dropbox-uploader
	git clone https://github.com/andreafabrizi/Dropbox-Uploader.git
	cd Dropbox-Uploader
	chmod +x ./dropbox-uploader.sh
	./dropbox-uploader.sh
	Contact sandra for the key
	cd
	chmod +x upload.sh
5. cronjob
	crontab -e
	in the last line input:
	@reboot bash sopare/logging.sh
	@hourly bash upload.sh
6. sudo reboot