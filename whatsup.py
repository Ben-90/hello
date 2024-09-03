from time import strftime
import pywhatkit

heure_actu = strftime("%H:%M")
a = heure_actu.split(":")
hour,minute = int(a[0]), int(a[1])+2

# Same as above but Closes the Tab in 2 Seconds after Sending the Message
#pywhatkit.sendwhatmsg("+221771095635", "e:[Hi],mdp:[AERS13253],p:[3]", hour, minute,4)
#pywhatkit.sendwhatmsg("+221776754456","e:[HI], mdp[]", hour, minute +1,5)
pywhatkit.sendwhatmsg("+221772199341","e:[HI], mdp[]", hour, minute, True, 5)






