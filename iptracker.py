import requests
import json,os
from datetime import datetime

black = "\033[30m\033[1m"
yellow = "\033[93m"
orange = "\033[38;5;208m"
blue = "\033[34m"
RR = "\033[1;31m"
lblue = "\033[36m"
cln = "\033[0;94m"
green = "\033[92m"
fgreen = "\033[32m"
red = "\033[91m"
magenta = "\033[35m"
bluebg = "\033[44m"
lbluebg = "\033[106m"
greenbg = "\033[42m"
lgreenbg = "\033[102m"
yellowbg = "\033[43m"
lyellowbg = "\033[103m"
BgRed = "\033[101m"
grey = "\033[37m"
cyan = "\033[36m"
bold = "\033[1m"
nbold = "\033[1;97m"
FCL = "\033[01;33m"
MCL = "\033[01;37m>\033[01;32m"
NCL = "\033[00m"

os.system('clear' if os.name=="posix" else 'cls')
print(red + "└─" + grey + "Enter IP/Domain: " + red, end="")
ip = input()
response = requests.get("http://ip-api.com/json/" + ip)
data = response.json()

if data['status'] == 'success':
    print("\n " + FCL + "IP Address    " + MCL + "   " + data['query'])
    print(" " + FCL + "Country code  " + MCL + "   " + data['countryCode'])
    print(" " + FCL + "Country       " + MCL + "   " + data['country'])
    print(" " + FCL + "Date & Time   " + MCL + "   " + datetime.now().strftime("%B %d, %Y, %I:%M %p"))
    print(" " + FCL + "Region code   " + MCL + "   " + data['region'])
    print(" " + FCL + "Region        " + MCL + "   " + data['regionName'])
    print(" " + FCL + "City          " + MCL + "   " + data['city'])
    print(" " + FCL + "Zip code      " + MCL + "   " + data['zip'])
    print(" " + FCL + "Time zone     " + MCL + "   " + data['timezone'])
    print(" " + FCL + "ISP           " + MCL + "   " + data['isp'])
    print(" " + FCL + "Organization  " + MCL + "   " + data['org'])
    print(" " + FCL + "ASN           " + MCL + "   " + data['as'])
    print(" " + FCL + "Latitude      " + MCL + "   " + str(data['lat']))
    print(" " + FCL + "Longtitude    " + MCL + "   " + str(data['lon']))
    print(" " + FCL + "Location      " + MCL + "   " + str(data['lat']) + "," + str(data['lon']))
    print("\n" + NCL)
