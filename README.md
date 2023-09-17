# game-saves-backup
A simple python script to backup those save files and never lose your precious progress again!

## Features
- Your current save file once backed up will not overwrite your latest backup.
- This way you will have your latest + one most recent backup (2 backups).

## Usage
- Add your games to the ```games_list.txt``` in following pattern:\
```"game_name">"game_path"```
- Configure your backup folder's path and games list path in ```settings.conf```
- Run the script by running ```game-saves-backup.py``` or get the latest windows executable from Releases
- Alternatively you can compile your own executable by running the following command:
```powershell
pip install pyinstaller
pyinstaller --onefile \path\to\game-saves-backup.py
```
- The executable can be found in ```dist``` folder. Move it to main script's folder and run it

## DOs and DON'Ts
- Double quotes are not necessary but highly recommended. 
- DO NOT USE SINGLE QUOTES (') AROUND THE PATH
- Single quotes present in game's name are okay (Example: Marvel's Spiderman)

## Tips
- You can use Windows Task Scheduler to run this script periodically.