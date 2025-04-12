# DiscordDeleteMessageSelfBot

This is a simple project for a moderator who is a lazy boi and wants to delete the scam message!
It's a self-bot that runs on your account! This is for educational purpose and moderate purpose only!

⚠️ Warning: Self-bots are against Discord's Terms of Service, and using one can result in your account being permanently banned.
Use it with your own risk! I'll not be responsible for any modifications of the bots!

# Run it by :
 -1. Download this Git as a ZIP
 
  0. Extract the zip
  1. right-click on the folder
  2. Click "Open in Therminal"
  3. run it by typing "python delete_scam.py" (if you run .py directly it will not read the config file yaya)

**Use "Config.json" to config the settings (Config Guide below Command Guides)**

That's it! It can only be monitoring 1 server. I'll update later.

# Command Guides : (Commands can be used in any channel of that sever!)

  •Type "!botpause" to pause, and "!botresume" to resume. Obiuvsly .> ~ <.
  
  •Type "!reloadconfig" "!botrefresh" "!botreload" to make it read config files again after you edit it. So no restart!
  
  •Type "!scanpast" "!botscan" to scan past message in the server!
  

  # Config Guide :
This is what "Config.json" inculdes!

  {
  
    "token": "AAAAAAAAAAAAAAAAAAAAAAA", << Enter your discord token yaya! Don't worry i won't steal it! becuz the code has nothing that does with it other than login. 
    "guild_id": 123123123, << Ts supposed to be a server ID, So put your server ID in! BUT ONLY. ONE. SERVER.
    "scam_keywords": [ << This is a keyword that when bot see, It deletes that message. and don't forget the "," after a keyword, and leave the last one without it. otherwise no work :>
      "steamcommunity.cfd", 
      "Steam Gift Activation",
      "50$ gift",
      "This is a scam link test lul.com"
    ],
    "blocked_user_ids": [], << Input user IDs here (could be more than one), This one will make that user bypass the fliter of deletion!
    "blocked_channel_ids": [], << Input channel IDs here (Could be more than one), This will make the bot not filter that channel
    "active": true , << Just for !botpause and !botresume command. Default is true. just leave it be, if set to false, Your bot will need to !botresume every start.
    "ignore_self": false, << Make it ignore your message if you set it to true.
    "scan_on_startup": true << Recommended to be turned on. cuz it'll scan the past message when startup.
  }


# BOT REQUIREMENTS :
  • GIT (DOWNLOAD : https://git-scm.com/download/win , And click next next next next next and install! MUST ADD TO PATH!! )
  
  • Phython (Add to PATH too xd)
  
  • Use "pip install -U git+https://github.com/dolfies/discord.py-self" when first time start-up.
  
  • YOUR DISCORD TOKEN. ( GUIDE : https://gist.github.com/MarvNC/e601f3603df22f36ebd3102c501116c6 )




