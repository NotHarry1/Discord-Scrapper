import requests, json, time, os, sys, colorama, pystyle
from colorama import Fore
from pystyle import Anime, Add, Colors, Center, System, Write, Colorate
from time import gmtime, strftime
colorama.init(autoreset=True)
os.system("cls")
os.system('title Genius Discord Scrapper - github.com/notharry1')

l = """
   ▄██████▄     ▄████████ ███▄▄▄▄    ▄█  ███    █▄     ▄████████ 
  ███    ███   ███    ███ ███▀▀▀██▄ ███  ███    ███   ███    ███ 
  ███    █▀    ███    █▀  ███   ███ ███▌ ███    ███   ███    █▀  
 ▄███         ▄███▄▄▄     ███   ███ ███▌ ███    ███   ███        
▀▀███ ████▄  ▀▀███▀▀▀     ███   ███ ███▌ ███    ███ ▀███████████ 
  ███    ███   ███    █▄  ███   ███ ███  ███    ███          ███ 
  ███    ███   ███    ███ ███   ███ ███  ███    ███    ▄█    ███ 
  ████████▀    ██████████  ▀█   █▀  █▀   ████████▀   ▄████████▀  
                                                                 

"""

Anime.Fade(text=Center.Center(l), color=Colors.red_to_green, mode=Colorate.Vertical, time=2)

def main(invite):
    os.system("cls")
    response = requests.get(f"https://discord.com/api/v9/invites/{invite}").json()
    name = response["guild"]["name"]
    id = response["guild"]["id"]
    banner_id = response["guild"]["banner"]
    icon_id = response["guild"]["icon"]
    desc = response["guild"]["description"]
    banner = f"https://cdn.discordapp.com/banners/{id}/{banner_id}?size=1024"
    icon = f"https://cdn.discordapp.com/icons/{id}/{icon_id}?size=1024"
    verif = response["guild"]['verification_level']
    vanityurl = response["guild"]['vanity_url_code']
    boost = response["guild"]['premium_subscription_count']
    nsfw = response["guild"]['nsfw']
    nsfw_lvl = response["guild"]['nsfw_level']
    desc2 = None
    if "welcome_screen" in response["guild"]:
        desc2 = response["guild"]['welcome_screen']['description']
    temp = strftime("%Y-%m-%d %H:%M:%S", gmtime())
    print(f"{Fore.LIGHTGREEN_EX}    Guild Name: {name}\n")
    print(f"{Fore.LIGHTGREEN_EX}    Guild Id: {id}\n")
    if banner_id is not None:
        print(f"{Fore.LIGHTGREEN_EX}    Guild Banner: {banner}\n")
    if icon_id is not None:
        print(f"{Fore.LIGHTGREEN_EX}    Guild Icon: {icon}\n")
    print(f"{Fore.LIGHTGREEN_EX}    Guild Description: {desc}\n")
    print(f"{Fore.LIGHTGREEN_EX}    Verification Level: {verif}\n")
    if vanityurl is not None:
        print(f"{Fore.LIGHTGREEN_EX}    Vanity Url: discord.gg/{vanityurl}\n")
    print(f"{Fore.LIGHTGREEN_EX}    Number of Boost: {boost}\n")
    print(f"{Fore.LIGHTGREEN_EX}    Nsfw Guild ?: {nsfw}\n")
    print(f"{Fore.LIGHTGREEN_EX}    Nsfw level: {nsfw_lvl}\n")
    if desc2 is not None:
        print(f"{Fore.LIGHTGREEN_EX}    Guild Welcome Screen Description: {desc2}\n")
    print(f"{Fore.LIGHTGREEN_EX}    Guild Features:\n")
    for i in response["guild"]['features']:
        print(f"{Fore.LIGHTRED_EX}          {i}")
    print("\n")
    
def user(id):
    with open(f"token.txt", 'r') as f:
        token = f.readline()
    headers= {
        "Host": "discord.com",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:107.0) Gecko/20100101 Firefox/107.0",
        "Accept": "*/*",
        "Accept-Language": "fr,fr-FR;q=0.8,en-US;q=0.5,en;q=0.3",
        "Accept-Encoding": "gzip, deflate, br",
        "Authorization": token,
        "X-Super-Properties": "eyJvcyI6IldpbmRvd3MiLCJicm93c2VyIjoiRmlyZWZveCIsImRldmljZSI6IiIsInN5c3RlbV9sb2NhbGUiOiJmciIsImJyb3dzZXJfdXNlcl9hZ2VudCI6Ik1vemlsbGEvNS4wIChXaW5kb3dzIE5UIDEwLjA7IFdpbjY0OyB4NjQ7IHJ2OjEwNy4wKSBHZWNrby8yMDEwMDEwMSBGaXJlZm94LzEwNy4wIiwiYnJvd3Nlcl92ZXJzaW9uIjoiMTA3LjAiLCJvc192ZXJzaW9uIjoiMTAiLCJyZWZlcnJlciI6IiIsInJlZmVycmluZ19kb21haW4iOiIiLCJyZWZlcnJlcl9jdXJyZW50IjoiIiwicmVmZXJyaW5nX2RvbWFpbl9jdXJyZW50IjoiIiwicmVsZWFzZV9jaGFubmVsIjoic3RhYmxlIiwiY2xpZW50X2J1aWxkX251bWJlciI6MTYwNjQ1LCJjbGllbnRfZXZlbnRfc291cmNlIjpudWxsfQ==",
        "X-Discord-Locale": "fr",
        "X-Debug-Options": "bugReporterEnabled",
        "Alt-Used": "discord.com",
        "Connection": "keep-alive",
        "Referer": "https://discord.com/channels/@me",
        "Cookie": "__cfduid=%s; __dcfduid=%s; locale=en-US" % (os.urandom(43).hex(), os.urandom(32).hex()),
        "Sec-Fetch-Dest": "empty",
        "Sec-Fetch-Mode": "cors",
        "Sec-Fetch-Site": "same-origin",
        "TE": "trailers"
    }
    response = requests.get(f"https://discord.com/api/v9/users/{id}/profile?with_mutual_guilds=true", headers=headers).json()
    if "code" in response:
        os.system("cls")
        if str(response['code']) == "50001":
            print(f"{Fore.LIGHTRED_EX}Error : Missing Access. Maybe because you are not friend with the target. Else, retry with someone else. (Discord API limit.)")
        else:
            print(f"{Fore.LIGHTRED_EX}Error : Please check if you put a correct token into the token.txt file. If error persists, please contact the creator (https://github.com/notharry1)")
    else:
        os.system("cls")
        if response['premium_type'] is not None:
            if response['premium_type'] == 1:
                nitro = "User Nitro Type : Classic"
            elif response['premium_type'] == 2:
                nitro = "User Nitro Type : Boost"
            else:
                nitro = "User doesn't have nitro"
        id1 = response['user']['id']
        name = response['user']['username']
        discri = response['user']['discriminator']
        av_id = response['user']['avatar']
        b_id = response['user']['banner']
        flags = response['user']['public_flags']
        banner_color = response["user"]['banner_color']
        acc_color = response["user"]["accent_color"]
        urlp = f"https://cdn.discordapp.com/avatars/{id1}/{av_id}?size=1024"
        urlb = f"https://cdn.discordapp.com/banners/{id1}/{b_id}?size=1024"
        print(f"{Fore.LIGHTGREEN_EX}User info :")
        print(f"    {Fore.LIGHTGREEN_EX}UserName : {name}#{discri}")
        print(f"    {Fore.LIGHTGREEN_EX}User Id : {id1}")
        print(f"    {Fore.LIGHTGREEN_EX}User Avatar : {urlp}")
        if response['user']['banner'] is not None:
            print(f"    {Fore.LIGHTGREEN_EX}User Banner : {urlb}")
        print(f"    {Fore.LIGHTGREEN_EX}User Flag : {flags}")
        print(f"    {Fore.LIGHTGREEN_EX}User Banner Color : {banner_color}")
        print(f"    {Fore.LIGHTGREEN_EX}User Accent Color : {acc_color}")
        print(f"    {Fore.LIGHTGREEN_EX}{nitro}")
        if response["premium_guild_since"] is not None:
            boost_since = response["premium_guild_since"][:10]
            print(f"    {Fore.LIGHTGREEN_EX}User Boost Since : {boost_since}")
        print(f"{Fore.LIGHTGREEN_EX} Mutual Guilds :")
        if response["mutual_guilds"] is not None:
            for i in response["mutual_guilds"]:
                mid = i['id']
                if i['nick'] is not None:
                    nick = i['nick']
                else:
                    nick = "no nickname on this guild"
                print(f"    {Fore.LIGHTGREEN_EX}Server id : {mid}, nickname on the guild : {nick}")
        if (response['user_profile']['bio'] is not None or response['connected_accounts'] is not None):
            print(f"{Fore.LIGHTGREEN_EX}Others infos :")
            if response['user_profile']['bio'] is not None:
                bio = response['user_profile']['bio']
                print(f"    {Fore.LIGHTGREEN_EX}User Bio : {bio}")
            if response['connected_accounts'] != "[]":
                print(f"    {Fore.LIGHTGREEN_EX}Connected account :")
                for i in response['connected_accounts']:
                    type = i['type']
                    name1 = i['name']
                    verif = i["verified"]
                    print(f"        {Fore.LIGHTGREEN_EX}{type}, name : {name1}, account verified ?: {verif}")
        print("\n")    
def inviter(invite):
    response = requests.get(f"https://discord.com/api/v9/invites/{invite}").json()
    if "inviter" in response:
        os.system("cls")
        name = response['inviter']['username']
        disc = response["inviter"]["discriminator"]
        id = response["inviter"]["id"]
        pflag = response["inviter"]['public_flags']
        username = f"{name}#{disc}"
        av_id = response["inviter"]['avatar']
        exp = response["expires_at"][:10]
        url = f"https://cdn.discordapp.com/avatars/{id}/{av_id}?size=1024"
        print(f"    {Fore.LIGHTGREEN_EX}Inviter UserName : {username}")
        print(f"    {Fore.LIGHTGREEN_EX}Inviter Id : {id}")
        print(f"    {Fore.LIGHTGREEN_EX}Public flags : {pflag}")
        print(f"    {Fore.LIGHTGREEN_EX}Inviter Avatar : {url}")
        print(f"    {Fore.LIGHTGREEN_EX}Invite expiration : {exp}\n")
    else:
        os.system("cls")
        print(f"{Fore.LIGHTRED_EX}Error : you maybe enter a vanity url. Retry with another invite url.\n")
    


if __name__ == "__main__":
    check = open("token.txt", 'r').readlines()
    print(f"{Fore.LIGHTCYAN_EX}> [1] Guild Scrapper\n> [2] User Scrapper\n> [3] Inviter Scrapper")
    choice = str(input("\n> Make your choice : "))
    if choice == "1":
        os.system("cls")
        invite = str(input("> Enter the invite code : "))
        main(invite)
        os.system("pause >null")
    elif choice == "2":
        os.system("cls")
        if len(check) == 0:
            print(f"{Fore.LIGHTRED_EX}You need to insert a token into the token.txt file, to use the 2nd option.")
            os.system("pause >null")
        else:
            theid = str(input("> Enter the target id's : "))
            user(theid)
            os.system("pause >null")
    elif choice == "3":
        os.system("cls")
        invite = str(input("> Enter the invite code : "))
        inviter(invite)
        os.system("pause >null")
    else:
        os.system("cls")
        print(f"{Fore.LIGHTRED_EX}Incorrect choice")
        exit()