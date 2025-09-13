# Just a Last

Do you know this feeling ?  

*"just a last game"* → another one → suddenly it's 3AM.  

**Just a Last** is a small Windows app that helps you (and your friends) actually stop to play league or valorant when you planned to.  

## Features
- 🛑 Automatically closes only **Valorant** or **League of Legends** once your set time limit is reached.  
- ✅ Smart detection: it only closes the game **after your match ends** (no mid-game rage quits).  
- 🌙 **Night mode** enabled by default (blocks gaming past 6 AM).  
  - You can change this in [`main.py`](./main.py) inside the `heure_depassee` function.  
- Interface:
  - Choose your allowed hours  
  - Start/stop the program  
  - See current status in real time  

## ⚙️ How to Use
- Run on **Windows** directly, or  
- Build an `.exe` using [PyInstaller](https://pyinstaller.org/) with `ui.py` if you want a standalone app.  

## *⚠️ Note for Windows users:*
The first time you launch the .exe, Windows may warn you with a blue screen ("Windows protected your PC").
This happens because the app is unsigned (I don’t have a certificate yet).
Just click "More info" → "Run anyway". After the first run, Windows will remember your choice.


## 💡 Why I made this
I made this because my friends and I always said *“last game”*… and ended up sleeping way too late.  
This app helps keep gaming fun while respecting your limits.  

## 📩 Feedback
This is just a side project, so I’d love to hear what you think.  
If you have ideas or improvements, feel free to open an issue or pull request!  


---
