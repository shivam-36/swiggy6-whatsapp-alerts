import requests
import time
from datetime import datetime
import notification_service
import selenium


def timestamp_exists(comm):
    key = 'timestamp'
    if key in comm:
        return float(comm[key])
    else:
        return float(-1);

def is_six(line_of_comm):
    key = 'evt'
    if key in line_of_comm and line_of_comm[key] == 'six':
        return True
    return False

def send_alert(param):
    param = param/1000
    st = datetime.fromtimestamp(param)
    et = datetime.fromtimestamp(param + 360)
    msg = "Six hit at " + st.strftime('%H:%M:%S') + "  Use coupon code SWIGGY6 before  " + et.strftime(' %H:%M:%S') + " \n Hurry!"
    print datetime.fromtimestamp(param)
    print "\n"
    print msg

    notification_service.send_alert(msg)
    pass

lastSix = float(-1)

while 1:
    try:
        data = requests.get("http://mapps.cricbuzz.com/cbzios/match/22476/commentary").json()
        print datetime.fromtimestamp(time.time())
        for item in data['comm_lines']:
            if timestamp_exists(item) > 0:
                if is_six(item):
                    time_of_six = timestamp_exists(item)
                    if lastSix < 0 or time_of_six > lastSix:
                        send_alert(time_of_six)
                        lastSix = time_of_six
                        break
        time.sleep(45)
    except requests.exceptions.RequestException as e:
        print e
        time.sleep(10)
    except Exception as e:
        print e
        time.sleep(10)
