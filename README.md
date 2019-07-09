# scary-haloween
<br>python script to play a spooky sound when a PIR sensor triggers via GPIO 

<br>Fun way to scare someone at haloween or just anytime they walk into a room!!
<br>Uses a PIR sensor and a raspberry pi.  When the PIR detects someone it plays a wav file, you can chose from a number of random files or just one.   This has been put together using lots of different sites online.  Wav files and Ogg files work but i havent been able to use MP3s so use an online tool to convert them.
<br>I used a set of cheap-o USB speakers, you will need to enable them by editing the alsa.conf.

<br>sudo nano /usr/share/alsa/alsa.conf
<br>Find - 
<br>defaults.ctl.card 0
<br>defaults.pcm.card 0
<br>Change both “0” to “1” and then save the file. 

<br>Pre-requisites:
<br>sudo apt-get install python-pip, 
<br>sudo pip install gpiozero, 
<br>sudo apt-get install python-pygame

<br>To wire the PIR sensor:
<br>VCC to 5v on the Pi. 
<br>GND to GND. 
<br>Signal Pin to GPIO 18
