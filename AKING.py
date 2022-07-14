import os, platform, time
try:
    import requests
except:
    os.system('pip install requests')
    import requests
bit = platform.architecture()[0]
if bit == '64bit':
    from AKING import login
    login()

