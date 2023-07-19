import requests
import colorama
import threading
import ctypes
from colorama import Fore, Style
from threading import Thread
from sys import stdout
from requests import Session
import time
from time import strftime, gmtime, sleep
import os
try:
    import colorama
except:
    os.system('pip install colorama')

from colorama import Fore, init
    
import os
from os import system
try:
    import discord
except:
    os.system('pip install discord.py==1.7.3')

from discord.ext import commands

try:
    import colorama
except:
    os.system('pip install colorama')

from colorama import Fore, init

try:
    import asyncio
except:
    os.system('pip install asyncio==3.4.3')
try:
    import random
except:
    os.system('pip install random')
try:
    import fade
except:
    os.system('pip install fade==0.0.9')
try:
    import aiohttp
except:
    os.system('pip install aiohttp')

from discord import Permissions

from discord.utils import get

import string

from discord import Permissions

import inspect

import urllib

import datetime
try:
    import requests as rq
except:
    os.system('pip install requests')
try:
   import time
except:
    os.system('pip install time')
from time import sleep

try:
   import subprocess
except:
    os.system('pip install subprocess')
from subprocess import Popen


with open('token.txt', 'r') as file:
    token = file.read()
    
import requests
import colorama
import threading
import ctypes
from colorama import Fore, Style
from threading import Thread
from sys import stdout
from requests import Session
import time
from time import strftime, gmtime, sleep
import os

print(f"""

{Fore.BLUE}

 ▄▄▄▄    ██▓     ▒█████   ▒█████  ▓█████▄   ██████ ▓█████  ██▓      █████▒
▓█████▄ ▓██▒    ▒██▒  ██▒▒██▒  ██▒▒██▀ ██▌▒██    ▒ ▓█   ▀ ▓██▒    ▓██   ▒ 
▒██▒ ▄██▒██░    ▒██░  ██▒▒██░  ██▒░██   █▌░ ▓██▄   ▒███   ▒██░    ▒████ ░ 
▒██░█▀  ▒██░    ▒██   ██░▒██   ██░░▓█▄   ▌  ▒   ██▒▒▓█  ▄ ▒██░    ░▓█▒  ░ 
░▓█  ▀█▓░██████▒░ ████▓▒░░ ████▓▒░░▒████▓ ▒██████▒▒░▒████▒░██████▒░▒█░    
░▒▓███▀▒░ ▒░▓  ░░ ▒░▒░▒░ ░ ▒░▒░▒░  ▒▒▓  ▒ ▒ ▒▓▒ ▒ ░░░ ▒░ ░░ ▒░▓  ░ ▒ ░    
▒░▒   ░ ░ ░ ▒  ░  ░ ▒ ▒░   ░ ▒ ▒░  ░ ▒  ▒ ░ ░▒  ░ ░ ░ ░  ░░ ░ ▒  ░ ░      
 ░    ░   ░ ░   ░ ░ ░ ▒  ░ ░ ░ ▒   ░ ░  ░ ░  ░  ░     ░     ░ ░    ░ ░    
 ░          ░  ░    ░ ░      ░ ░     ░          ░     ░  ░    ░  ░        
      ░                            ░                                      
""")
def startprint():
      os.system('cls')
      
print(f"""
{Fore.RED} x > {Fore.RESET}Options

{Fore.RED} {1} > {Fore.RESET}illegal Conent {Fore.GREEN}::{Fore.RESET} 1
{Fore.RED} {2} > {Fore.RESET}Harrassment {Fore.GREEN}::{Fore.RESET} 2
{Fore.RED} {3} > {Fore.RESET}Spam or Phishing Links {Fore.GREEN}::{Fore.RESET} 3
{Fore.RED} {4} > {Fore.RESET}Self harm {Fore.GREEN}::{Fore.RESET} 4
{Fore.RED} {5} > {Fore.RESET}NSFW Content {Fore.GREEN}::{Fore.RESET} 5
""")

token = token
headers = {'Authorization': token, 'Content-Type':  'application/json'}  
r = requests.get('https://discord.com/api/v6/users/@me', headers=headers)
if r.status_code == 200:
        pass
else:
        print(f"{Fore.RED} > Invalid Token")
        input()
guild_id1 = input(f"{Fore.BLUE} > Server ID{Fore.RESET}: ")
channel_id1 = input(f"{Fore.BLUE} > Channel ID{Fore.RESET}: ")
message_id1 = input(f"{Fore.BLUE} > Message ID{Fore.RESET}: ")
reason1 = input(f"{Fore.BLUE} > Option{Fore.RESET}: ")


def Main():
  global sent
  headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) discord/0.0.305 Chrome/69.0.3497.128 Electron/4.0.8 Safari/537.36',
        'Authorization': token,
        'Content-Type': 'application/json'
      }

  payload = {
    'channel_id': channel_id1,
    'guild_id': guild_id1,
    'message_id': message_id1,
    'reason': reason1
  }

  while True:
      time.sleep(15)
      r = requests.post('https://discord.com/api/v6/report', headers=headers, json=payload)
      time.sleep(5)
      if r.status_code == 201:
          print(f"{Fore.GREEN} > Sent Report {b+Fore.BLUE}::{Fore.GREEN} ID {message_id1}")
          ctypes.windll.kernel32.SetConsoleTitleW(f"[REPORT BOT] By Voild | Sent: %s" % sent)
          sent += 1

      elif r.status_code == 401:
          print(f"{Fore.RED} > Invalid token")
          input()
          exit()
      else:
          print(f"{Fore.RED} > Error")
os.system('CLS')

