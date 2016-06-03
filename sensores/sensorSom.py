import mraa
import time

print (mraa.getVersion())

try:
    #x = mraa.Aio(0)
    while True:
    	x = mraa.Aio(0)
        print (x.read())
        print ("%.5f" % x.readFloat())
        time.sleep(0.5)
except:
    print ("Are you sure you have an ADC?")