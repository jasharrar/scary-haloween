# scary-haloween
python script to play a spooky sound when a PIR sensor triggers via GPIO 

Fun way to scare someone at haloween or just anytime they walk into a room!!
Uses a PIR sensor and a raspberry pi.  When the PIR detects someone it plays a wav file, you can chose from a number of random files or just one.   This has been put together using lots of different sites online.  Wav files and Ogg files work but i havent been able to use MP3s so use an online tool to convert them.
I used a set of cheap-o USB speakers, you will need to enable them by editing the alsa.conf.
sudo nano /usr/share/alsa/alsa.conf
Find - 
defaults.ctl.card 0
defaults.pcm.card 0
Change both “0” to “1” and then save the file. 

Pre-requisites:
sudo apt-get install python-pip, 
sudo pip install gpiozero, 
sudo apt-get install python-pygame

To wire the PIR sensor:
VCC to 5v on the Pi
GND to GND
Signal Pin to GPIO 18
