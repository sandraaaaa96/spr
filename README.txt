0. set up sopare
	https://www.bishoph.org/step-by-step-raspberry-pi-offline-voice-recognition-with-sopare/
	Ensure sopare has basic functionality before implementing the other scripts.

1. git clone repo into sopare
	cd sopare
	git clone https://github.com/sandraaaaa96/spr.git
In sopare folder:
	rm -r dict
	rm -r config
	cd spr
In spr folder:
	cp -r dict ~/sopare
	cp -r config ~/sopare
	remember to run ./sopare.py -c to add the dictionary

2. copy out files into sopare
	cd sopare
	cd spr
In spr folder:
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

6. ensure that setup works: (DEBUG)
	cd sopare
	nano writefiles.py
	uncomment out i=0 and i+=1 and while i<3: (just delete the hash)
	comment out while True: (add hash in front of the statement)
	replace maxloops=100 with maxloops=3
	cd
	bash sopare/logging.sh
	after it runs to completion
	bash upload.sh

#in the dropbox folder, you should see 3 logfiles with 3 records from sopare

if everything works, comment out i=0, i+=1 and while i<3 and uncomment while True. The script is back to normal.

7. cronjob
	crontab -e
	in the last line input:
	@reboot bash sopare/logging.sh
	@hourly bash upload.sh

8. sudo reboot
