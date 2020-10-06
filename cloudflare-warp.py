import urllib.request
import json
import datetime
import random
import string
import time
import os
import sys
os.system("title Warp+ Script")
os.system('cls' if os.name == 'nt' else 'clear')

print ("[+] ABOUT SCRIPT:")
print ("[-] With this script, you can get unlimited GB on Warp+.")
print ("--------")
print ("[+] Credits to the respectful owners") 
print ("[-] Github : https://github.com/cl4ra") 
print ("[-] Phcorner : https://phcorner.net/members/6six6.1300228/")
print ("--------")
print ("[~]You can find your ID on Advanced/Diagnostics")
referrer = input("[#] Enter the WARP+ ID:")
def genString(stringLength):
	try:
		letters = string.ascii_letters + string.digits
		return ''.join(random.choice(letters) for i in range(stringLength))
	except Exception as error:
		print(error)		    
def digitString(stringLength):
	try:
		digit = string.digits
		return ''.join((random.choice(digit) for i in range(stringLength)))    
	except Exception as error:
		print(error)	
url = f'https://api.cloudflareclient.com/v0a{digitString(3)}/reg'
def run():
	try:
		install_id = genString(22)
		body = {"key": "{}=".format(genString(43)),
				"install_id": install_id,
				"fcm_token": "{}:APA91b{}".format(install_id, genString(134)),
				"referrer": referrer,
				"warp_enabled": False,
				"tos": datetime.datetime.now().isoformat()[:-3] + "+02:00",
				"type": "Android",
				"locale": "es_ES"}
		data = json.dumps(body).encode('utf8')
		headers = {'Content-Type': 'application/json; charset=UTF-8',
					'Host': 'api.cloudflareclient.com',
					'Connection': 'Keep-Alive',
					'Accept-Encoding': 'gzip',
					'User-Agent': 'okhttp/3.12.1'
					}
		req         = urllib.request.Request(url, data, headers)
		response    = urllib.request.urlopen(req)
		status_code = response.getcode()	
		return status_code
	except Exception as error:
		print(error)	

g = 0
b = 0
while True:
	result = run()
	if result == 200:
		g = g + 1
		os.system('cls' if os.name == 'nt' else 'clear')
		print("")
		print(r"""

    __      _        __  
   / /     (_)      / /  
  / /_  ___ ___  __/ /_  
 | '_ \/ __| \ \/ / '_ \ 
 | (_) \__ \ |>  <| (_) |
  \___/|___/_/_/\_\\___/ 
                         
                         



            """)
		print("")
		animation = ["[Please wait.] 10%","[Please wait..] 20%", "[Please wait...] 30%", "[Please wait....] 40%", "[Please wait.....] 50%", "[Please wait......] 60%", "[Please wait.......] 70%", "[Please wait........] 80%", "[Please wait.........] 90%", "[Completed!] 100%"] 
		for i in range(len(animation)):
			time.sleep(0.5)
			sys.stdout.write("\r[+] Initializing script " + animation[i % len(animation)])
			sys.stdout.flush()
		print(f"\n[-] Sending GB to: {referrer}")    
		print(f"[:)] {g} GB has been successfully added to your account.")
		print(f"[#] Total: {g} Good {b} Bad")
		print("[*] After 18 seconds, a new request will be sent to prevent error.")
		time.sleep(18)
	else:
		b = b + 1
		os.system('cls' if os.name == 'nt' else 'clear')
		print("")
		print(r"""\

                               ._ o o
                               \_`-)|_
                            ,""       \ 
                          ,"  ## |   ಠ ಠ. 
                        ," ##   ,-\__    `.
                      ,"       /     `--._;)
                    ,"     ## /
                  ,"   ##    /


            """)

		print("[:(] Error when connecting to server.")
		print(f"[#] Total: {g} Good {b} Bad")	
