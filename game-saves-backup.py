import os
import logging
import shutil
from datetime import datetime
from pathlib import Path as PATH

# logging function
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


# initialize variables
SAVES_LIST_PATH = 'games_list.txt'
BACKUP_LOCATION = 'backups'


# read settings from settings.conf
try:
    with open ('settings.conf', 'r+') as f:
        settings = f.read().split('\n')
        for option in settings:
            option_name = option.split('>')[0]
            option_path = option.split('>')[1]

            if option_name == 'SAVES_LIST_PATH' and option_path != '':
                SAVES_LIST_PATH = option_path
                if SAVES_LIST_PATH[0] == SAVES_LIST_PATH[-1] and SAVES_LIST_PATH[0] in ['\"', "\'"]:
                    SAVES_LIST_PATH = SAVES_LIST_PATH[1:-1]

            if option_name == 'BACKUP_LOCATION' and option_path != '':
                BACKUP_LOCATION = option_path
                if BACKUP_LOCATION[0] == BACKUP_LOCATION[-1] and BACKUP_LOCATION[0] in ['\"', "\'"]:
                    BACKUP_LOCATION = BACKUP_LOCATION[1:-1]
                    
except Exception as e:
    logging.error("Error in paths in settings.conf")
    exit(1)


# read games list
with open (SAVES_LIST_PATH, 'r+') as f:
    games_list = f.read().split('\n')
    games_list = [ {'name':i.split('>')[0], 'path':i.split('>')[1]} for i in games_list ]


# backup saves
for game in games_list:
    if game['name'][0] == game['name'][-1] and game['name'][0] in ['\"', "\'"]:
        game['name'] = game['name'][1:-1]
    if game['path'][0] == game['path'][-1] and game['path'][0] in ['\"', "\'"]:
        game['path'] = game['path'][1:-1]

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

logging.info("Session ended")