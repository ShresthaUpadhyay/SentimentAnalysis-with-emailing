import time
import threading
import sys
import os
from time import *
from ctypes import windll
from tkinter import *
import NLP
import pyperclip
# from NLP import nameF



def copypaste(filename,time):
    if windll.user32.OpenClipboard(None):
        windll.user32.EmptyClipboard()
    windll.user32.CloseClipboard()

    sys.path.append(os.path.abspath("SO_site-packages"))


    recent_value = ""

# D = time.strftime("%D")
# r = time.strftime("%r")

    
    file_name = filename.strip()

    #timer running in the background 
    

    
    def countdown( ):  
        global my_timer

        my_timer = time 
        for x in range(my_timer):
            my_timer = my_timer - 1
            sleep(1)

    

    countdown_thread = threading.Thread(target= countdown)

    countdown_thread.start()

    while True:
        tmp_value = pyperclip.paste()
        if tmp_value != recent_value:
            recent_value = tmp_value
            print("Value changed: %s" % str(recent_value)[:20])
            with open(file_name+'.txt', '+a') as output:
                try:
                    # output.write("[Start]----------------"+D+" "+r+"----------------\n")
                    output.write("%s\n" % str(tmp_value))
                    # output.write("[End]-----------------------------------------------------------------\n\n\n")
                except:
                    # output.write("[Start]----------------" + D + " " + r+"----------------\n")
                    output.write("%s\n" % str(tmp_value.encode('UTF-8')))
                    # output.write("[End]-----------------------------------------------------------------\n\n\n")
        sleep(0.1)
        if my_timer == 0:
            # return file_name
            # NLP.nameF(file_name+'.txt')
            sys.exit()
    
    

# copypaste('linux',30)



