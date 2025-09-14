# Just a Last


<img width="1918" height="948" alt="JAL Riot" src="https://github.com/user-attachments/assets/d737d32e-2ac5-4f51-9ace-fbc984129bb4" />


Do you know this feeling ?  

*"just a last game"* → another one → suddenly it's 3AM.  

**Just a Last** is a small Windows app that helps you (and your friends) actually stop to play league or valorant when you planned to.  

## Features

- Automatically closes only **Valorant** or **League of Legends**  (+ Riot Client) once your set time limit is reached.  
- Smart detection: it only closes the game **after your match ends** (no mid-game rage quits).  
- **Night mode** enabled by default (blocks gaming past 6 AM).  
  - You can change this in [`main.py`](./main.py) inside the `heure_depassee` function.

### Interface:

<img width="593" height="728" alt="JAL_ui" src="https://github.com/user-attachments/assets/ccb9d285-c6af-4f25-b850-c62470928f37" />

  - Choose your allowed hours  
  - Start/stop the program  
  - See current status  

## How to Use

- Run on **Windows** directly by clicking on /dist directory and then on ui.exe , or  
- Build an `.exe` using [PyInstaller](https://pyinstaller.org/) with `ui.py` if you want a standalone app.  

## *⚠️ Note for Windows users:*
The first time you launch the .exe, Windows may warn you with a blue screen ("Windows protected your PC").
This happens because the app is unsigned (I don’t have a certificate yet).
Just click "More info" → "Run anyway". After the first run, Windows will remember your choice.


## Why I made this
I made this because my friends and I always said *“last game”*… and ended up sleeping way too late.  
This app helps keep gaming fun while respecting your limits.  

## Feedback
This is my first side project, so I’d love to hear what you think.  
If you have ideas or improvements, feel free to open an issue or pull request!  


---
