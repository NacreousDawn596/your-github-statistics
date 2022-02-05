it's used to know what language you practiced a lot along your career :)

# HOW TO INSTALL 
```sh
sudo apt-get install git
git clone https://github.com/NacreousDawn596/your-github-statistics
cd your-github-statistics
pip install -r requirements.txt
```

# HOW TO USE IT

```sh
python3 main.py <username>
```

# NOTE: 
github may block your requests if you abuse due to some security reasons of their server, but if you want, you can create here a file named token.txt where you gonna put your github token ^^

# TIP/CHEAT:
if you have used a language and you want github to hide it
just create a file named ".gitattributes"
and write: *for example you want to hide all html files*
```.gitattributes
*.html linguist-detectable=false
```

*or if you want to hide just one file*
```.gitattributes
index.html linguist-detectable=false
```

***enjoy!***
