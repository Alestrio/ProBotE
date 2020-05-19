# ProBotE
ProBotE is a Discord bot to automate actions linked to Pronote and Google Drive used on my classrooms' Discord server to automate manual tasks such as
transfering files from Pronote to Google Drive and gathering homeworks.

# Dependencies
- pronotepy by @bain3 and @Xiloe
- discord.py
- PyDrive

# How to use ?
- Install python3 and pip3
- Clone that repo
- Install dependencies (pip3 install discord pronotepy pydrive)
- Edit credentials.py.sample with your own values and rename it credential.py
- Download your API key in .json, and copy it there under the name "client_secrets.json"
- Start that bot with python3 probote.py

# How to contribute ?
You can contribute by submitting pull requests, or opening an issue to describe the feature you want to add.

# Features we want to add
- Google drive sync :
  - [ ] Upload files from Pronote (in adapted folder)
  - [ ] Upload files from ENT (in adapted folder)
  - [x] Upload files from Discord (in adapted folder)
  - [ ] Create evaluations that can be uploaded and then gathered by teacher
  - [x] Files list
  - [ ] File delete
  - [x] Folders list
  - [x] Subfolder creation
  - [ ] File uploading in subfolders deeper in the tree (actual : 2 levels)

- Pronote :
  - [x] Lessons content
  - [ ] Messages (only broadcast messages)
  - [ ] Auto sync (every x minutes or when a new homework is published)

- Misc :
  - [x] Version number in help command


# Author
Alexis LEBEL (@Alestrio0)
