#PYTHON 2.7
import time 
import pyscreenshot as ImageGrab
import datetime


im = ImageGrab.grab()


tempo = int(input('per quanti minuti: '))

if tempo == 0: 

	secondi = 300
	while secondi > 0:
		time.sleep(60)
		print('ogni minuto')
		secondi -= 60

elif tempo != 0:
	minuti = int(input('ogni quanti minuti? default un minuto') * 60)
	files = []

	
	tempo = tempo * 60

	
	while tempo > 0:
		time.sleep(minuti)
		
		print ('file creato')
		im.show()

		ImageGrab.grab_to_file(str(datetime.datetime.now()).split('.')[0].replace(' ', '')+'.png')
		files.append(str(datetime.datetime.now()).split('.')[0].replace(' ', '')+'.png')
		tempo -= minuti

	from ftplib import FTP
	ftp = FTP()
	ftp.connect('ftp.telefonini.altervista.org')
	ftp.login('telefonini', 'cafsemesde77')

	for element in files:
		print element




		ftp_file = open(element, 'rb')
		ftp.storbinary(element, ftp_file)
		ftp_file.close()
		ftp.quit()
