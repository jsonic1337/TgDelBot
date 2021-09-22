# TgDelBot
Userbot to delete your messages on command

### Installing the script

```
git clone https://github.com/jsonic1337/TgDelBot/

cd TgDelBot

pip3 install -U pyrogram

pip3 install -U tgcrypto
```
### Customization
Open "main.py" and insert data from your account into the signed lines (data must be taken from https://my.telegram.org/apps)

### Launch

```
python3 main.py
```
After this command, enter all the data for authorization

For the script to work permanently, we use pm2:
```
npm install pm2 -g

pm2 start main.py --interprete=python3 --name=TgDelBot
```
### Features
- **Delete all messages in this chat – /delall**
- **Deleting an arbitrary number of messages – oh or oh*number***
- **Deleting an arbitrary number of messages with editing – oh- or oh-*number***
