from time import strftime
import pywhatkit

heure_actu = strftime("%H:%M")
a = heure_actu.split(":")
hour,minute = int(a[0]), int(a[1])+1

# Same as above but Closes the Tab in 2 Seconds after Sending the Message
pywhatkit.sendwhatmsg("+221771095635", "Hi", hour, minute,15, True, 2)







