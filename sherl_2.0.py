import requests, os, urllib.request, json, random, time
os.system("clear")
ban = random.randint(0, 3)
if ban == 0:
    banner = """
    ░░░░░░░░▄███▄▄▄░░▄▄▄███▄░░░░░░░░
    ░░░░░░░██████████████████░░░░░░░
    ░░░░░░░████VAON4IK_YT████░░░░░░░
    ░░░░░░░██████████████████░░░░░░░
    ░░░░░░░██████████████████░░░░░░░
    ██▄▄▄██▀▀▀▀██████████▀▀▀▀██▄▄▄██
    ░▀██████▄▄▄░░░░░░░░░░▄▄▄██████▀░
    ░░░▀████████████████████████▀░░░
    ░░▄█▀█▀▀▀▀████████████▀▀▀▀█▀█▄░░
    ░░█▀░▀░░░░░▄▄░░░░░░▄▄░░░░░▀░▀█░░
    ░░█▄░░░░░░█░░█░░░░█░░█░░░░░░▄█░░
    ░░░▀██▄░░░░▀▀░░█░░░▀▀░░░░▄██▀░░░
    ░░░░░▀█▄░░░░░░░▀▀░░░░░░░▄█▀░░░░░
    ░░░░░░░██▄▄░░░████░░░▄▄██░░░░░░░
    ░░░░░▄███████▄▄▄▄▄▄███████▄░░░░░
    ░░░░▄██████████████████████▄░░░░
    ░░░▄█████████████SᕼERᒪOᑕK 2.0███▄░░░
    ░░▄██████████████████████████▄░░
    """
elif ban == 1:
    banner = """
       ,_
     ,'  `╲,_
     |_,-'_)
     /##c '╲  (
    ' |'  -{.  )
      /╲__-' ╲[]
     /`-_`╲             ԋҽɾɬσ𝓬ƙ
     '     ╲                VAON4IK
   _____________________________________________________
   |VK: https://vk.com/valery_onishenko  | TG: @vaon4ik |
   ‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾
"""
elif ban == 3:
    banner="""
 ___| |__   ___ _ __| | ___   ___| | __ |___ \  / _ \ 
/ __| '_ \ / _ \ '__| |/ _ \ / __| |/ /   __) || | | |
\__ \ | | |  __/ |  | | (_) | (__|   <   / __/ | |_| |
|___/_| |_|\___|_|  |_|\___/ \___|_|\_\ |_____(_)___/ 
                                                     
        _____________________________________________________
        |VK: https://vk.com/valery_onishenko  | TG: @vaon4ik |
        ‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾
    """
else:
    banner= """
    SᕼERᒪOᑕK 2.0       ,N.
                  _/__ ╲
                   -/o╲_╲
                 __╲_-./
                / / V ╲ U-.
    ())        /, > o <    ╲
    <╲.,.-._.-  [-╲ o /__..-1
    ______________________________________________________
    |VK: https://vk.com/valery_onishenko| TG: @vaon4ik   | 
    ‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾
     """
text = """
[1] - SEARᑕᕼ ᑕAR   [3] - ᑎIᑕK SᑕAᑎ
[2] - ᑭᕼOᑎE IᑎFO          
_______________________________
"""
print(banner)
print(text)
while True:
    numb = input("{Enter the number]-> ")
    if numb == "1":
        car_num = input("|  [enter the number of the machine](example:123xdj2)-> ")
        try:
            car_nums = car_num.upper()
            nc = car_num.lower()
            numb_car = nc[:6] + '.' + nc[6:]
            a_h=requests.get("https://авто-история.рф/num/"+car_nums+"/")
            km=requests.get("https://www.230km.ru/"+numb_car+".nomer")
            an=requests.get("http://avto-nomer.ru/ru/gallery.php?fastsearch="+nc)
            if a_h:
                print("|    |_")
                print("|      |https://авто-история.рф/num/"+car_nums+"/")
                print("|      |")
                if km:
                    print("|      |-https://www.230km.ru/"+numb_car+".nomer")
                    print("|      |")
                else:
                    print("|    |")
                    print("|    |-[ᑎO RESᑌᒪT]")
            else:
                print("|    |")
                print("|    |-[ᑎO RESᑌᒪT]")
                print("|    |")
            if len(nc)<8:
                print("|    |-[ᑎO RESᑌᒪT]")
                print("|    |")
            else:
                print("|    |-http://avto-nomer.ru/ru/gallery.php?fastsearch="+nc)
                print("|    |")


        except:
                print("[ᑎO results]")
    elif numb == "2":
        while True:
            try:
                phone = input("|  |-[EᑎTER ᑭᕼOᑎE]-> ")
                break
            except:
                print("|  |")
                print("|  |-[If you see this message it means there are no results
                print("|  |")

        getInfo = "https://htmlweb.ru/geo/api.php?json&telcod=" + phone
        try:
            infoPhones = urllib.request.urlopen( getInfo )
        except:
            print("|  |")
            print("|  |-[ᑎO RESᑌᒪT]")
            print("|  |")

        infoPhone = json.load( infoPhones )
        try:
            print( u"|  |")
            print( u"|    |-[ᑕOᑌᑎTRY]--->", infoPhone["country"]["name"] )
            print( u"|    |-[REGIOᑎ]---->", infoPhone["region"]["name"] )
            print( u"|    |-[operator]-->", infoPhone["0"]["oper"] )
            print( u"|    |-[ᑕITY]------> ", infoPhone["0"]["name"] )
        except:
            print("|  |")
            print("|  |-[ no results]")
            print("|  |")
    

   
    elif numb == '3':
        nick = input("|  |-[EᑎTER ᑎIᑕK]-> ")
        urls_site = ["https://vk.com/",
        "https://my.mail.ru/mail/",
        "https://www.drive2.ru/users/",
        "https://twitter.com/",
        "https://github.com/",
        "https://instagram.com/",
        "http://forum.3dnews.ru/member.php?username=",
        "https://4pda.ru/forum/index.php?act=search&source=pst&noform=1&username=",
        "https://forums.adobe.com/people/",
        "https://ask.fm/",
        "https://badoo.com/profile/",
        "https://www.bandcamp.com/",
        "https://bitcoinforum.com/profile/",
        "blogspot.com",
        "https://dev.to/",
        "https://www.ebay.com/usr/",
        "https://www.gamespot.com/profile/",
        "https://ok.ru/",
        "https://play.google.com/store/apps/developer?id=",
        "https://pokemonshowdown.com/users/",
        "https://www.reddit.com/user/",
        "https://steamcommunity.com/id/",
        "https://steamcommunity.com/groups/",
        "https://tamtam.chat/",
        "https://t.me/",
        "https://www.tiktok.com/@",
        "https://www.twitch.tv/",
        "https://data.typeracer.com/pit/profile?user=",
        "https://www.wikipedia.org/wiki/User:",
        "https://yandex.ru/collections/user/",
        "https://www.youtube.com/",
        "https://www.baby.ru/u/",
        "https://www.babyblog.ru/user/info/",
        "https://www.geocaching.com/profile/?u=",
        "https://habr.com/ru/users/",
        "https://pikabu.ru/@",
        "https://spletnik.ru/user/",
        "https://www.facebook.com/",
        "hhttps://zen.yandex.ru/",
        "https://ggscore.com/ru/dota-2/player?t=",
        "https://www.facebook.com/public/"]
        set_i = 0
        print("|   |_")
        while True:
            try:
                if set_i==13:
                    scan_s = requests.get("https://"+nick+"."+urls_site[set_i])
                else:
                    scan_s = requests.get(urls_site[set_i]+""+nick)

                if scan_s:
                    if set_i==13:
                        print("|     |- https://"+nick+"."+urls_site[set_i])
                    else:
                        print("|     |- "+urls_site[set_i]+""+nick)
                else:
                    print("|     |-[ᑎO RESᑌᒪT]")
            except:
                print("|     |-[ᑎO RESᑌᒪT]")
            if set_i+1 == len(urls_site):break

            set_i += 1
