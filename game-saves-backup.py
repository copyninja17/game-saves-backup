import os
import logging
import shutil
import config
from datetime import datetime
from pathlib import Path as PATH


try:
    os.mkdir(f"{PATH(__file__).parent.absolute()}/logs")
except:
    pass

d1 = (f"{datetime.now().year}_{datetime.now().month}_{datetime.now().day}")
i = 0
while True:
    if f'server_{d1}_{i}.log' in os.listdir(f"{PATH(__file__).parent.absolute()}/logs"):
        i+=1
    else:
        logname = f'{PATH(__file__).parent.absolute()}/logs/saves_{d1}_{i}.log'
        break

logging.basicConfig(filename=logname,
                    filemode='a',
                    format="[ {asctime} ][ {levelname} ] {message}",
                    level=logging.DEBUG,
                    style='{')


# Variables

SAVES_LIST_PATH = 'games_list.txt'
BACKUP_LOCATION = 'backups'

with open (SAVES_LIST_PATH, 'r+') as f:
    games_list = f.read().split('\n')
    games_list = [ {'name':i.split('>')[0], 'path':i.split('>')[1]} for i in games_list ]

for game in games_list:
    try:
        shutil.rmtree(f"{BACKUP_LOCATION}\{game['name']}\old")
    except Exception as e:
        logging.error(str(e))

    try:
        shutil.move(f"{BACKUP_LOCATION}\{game['name']}\latest", f"{BACKUP_LOCATION}\{game['name']}\old")
    except Exception as e:
        logging.error(str(e))

    try:
        shutil.copytree(game['path'], f"{BACKUP_LOCATION}\{game['name']}\latest")
        logging.info(f"Backed up {game['name']}")
    except Exception as e:
        logging.error(str(e))
