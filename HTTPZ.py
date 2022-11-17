import requests
import os
import sys
from colorama import Fore
import getpass as gt
from requests import exceptions
from time import sleep


OS = sys.platform
user = gt.getuser()
ROOT_DIR = os.path.abspath(os.curdir)



def is_There_a_File(entery):
    from colorama import Fore
    try:
        open(f'{entery}', 'r')
    except FileNotFoundError:
        print(Fore.RED+'\n[!]'+Fore.WHITE+' File not found')
        exit(1)
    except OSError:
        if '"' in entery:
            resualt = entery.replace('"','')
            return resualt
        if "'" in entery:
            resualt = entery.replace("'",'')
            return resualt
        else:
            raise OSError

    except Exception:
        print(Fore.RED+'\n[!]'+Fore.WHITE+' Error in locating your File/Domain')
        exit(1)
    else:
        return True


# def File_or_Domain(entery):
#     import sys
#     import os
#     if "'" in entery:
#         entery = entery.replace("'","")
#     if '"' in entery:
#         entery = entery.replace('"','')
#     if sys.platform == 'linux':
#         if '/' in entery:
#             return True
#         else:
#             print("\ninvalid input")
#             exit(1)
#     else:
#         return False



def OS_commands_of_httpz(entery):
    OS = sys.platform
    entery = entery.strip().lower().replace(' ','')
    if entery == 'dir' or entery == 'ls':
        if 'win' in OS:
            os.system('dir')
            print("\n")
            return True
        if 'linux' in OS:
            os.system('ls')
            print("\n")
            return True
        else:
            return False
    else:
        return False



def is_There_http_in_file(entery):
    try:
        request = requests.get(entery)
    except exceptions.MissingSchema:
        return False
    else:
        return True

def main_work():
    urls = input(Fore.RED+"┌─["+Fore.LIGHTGREEN_EX+"HTTPZ"+Fore.BLUE+"~"+Fore.WHITE+f"{user}"+Fore.RED+"]-("+Fore.LIGHTCYAN_EX+f"{ROOT_DIR}"+Fore.RED+")\n└──╼ "+Fore.WHITE)
    while True:
        if OS_commands_of_httpz(urls) == True:
            pass
            urls = input(Fore.RED+"┌─["+Fore.LIGHTGREEN_EX+"HTTPZ"+Fore.BLUE+"~"+Fore.WHITE+f"{user}"+Fore.RED+"]-("+Fore.LIGHTCYAN_EX+f"{ROOT_DIR}"+Fore.RED+")\n└──╼ "+Fore.WHITE)    
        elif OS_commands_of_httpz(urls) == None:
            urls = input(Fore.RED+"┌─["+Fore.LIGHTGREEN_EX+"HTTPZ"+Fore.BLUE+"~"+Fore.WHITE+f"{user}"+Fore.RED+"]-("+Fore.LIGHTCYAN_EX+f"{ROOT_DIR}"+Fore.RED+")\n└──╼ "+Fore.WHITE)
            continue
        elif OS_commands_of_httpz(urls) == False:
            break
    
    ###/. IS THERE ANY ['] OR [""] IN URLS? ###
    
    if is_There_a_File(urls) == True:
        file1 = open(f'{urls}', 'r')
    if is_There_a_File(urls) != True:
        resualt = is_There_a_File(urls)
        file1 = open(f'{resualt}', 'r')
    
    ### IS THERE ANY ['] OR [""] IN URLS? ./###
    
    Lines = file1.readlines()
    count = 0

    ###/. PRINTING MISSING SCHEMA OF THE URL ###

    striped_line_index_zero = (Lines[0]).strip()
    if is_There_http_in_file(striped_line_index_zero) == True:
        pass
    elif is_There_http_in_file(striped_line_index_zero) == False:
        print(Fore.YELLOW+"\n[!] Warning\n"+Fore.WHITE)
        sleep(2.5)
        print(Fore.YELLOW+"[!] the list you entered have no "+Fore.RED+"SCHEMA"+Fore.WHITE)
        sleep(2)
        print(Fore.YELLOW+"So im adding "+Fore.RED+'"https://"'+Fore.YELLOW+" to it\n\n"+Fore.WHITE)

    ### PRINTING MISSING SCHEMA OF THE URL ./###

    for i in Lines:
        count += 1
        i = i.strip()
        try:
            r = requests.get(i)
        except exceptions.ConnectionError:
            r.status_code = "Connection refused"
            print(Fore.RED+"[-] "+i+" Connection refused"+Fore.WHITE)
            pass
        
        ###/. HANDELING MISSING SCHEMA OF THE URL ###
        
        except exceptions.MissingSchema:
            i = "https://"+i
            pass
            try:
                r = requests.get(i)
            except Exception:
                print(Fore.LIGHTYELLOW_EX+"[!] "+Fore.WHITE+"There was a "+Fore.RED+"ERROR "+Fore.WHITE+"in requesting to your Target"+Fore.WHITE)
        
        ### HANDELING MISSING SCHEMA OF THE URL ./###
        
        except Exception:
            print(Fore.RED+"[!] "+Fore.WHITE+"There was a "+Fore.RED+"ERROR"+Fore.WHITE+"in requesting to your "+Fore.RED+"LIST"+Fore.WHITE)
        if r.status_code == 200:
            print(Fore.GREEN+"[+] "+i+" Found"+Fore.LIGHTMAGENTA_EX+f" [{r.status_code}]"+Fore.WHITE)
        else:
            print(Fore.RED+"[-] "+i+" Not Found"+Fore.LIGHTMAGENTA_EX+f" [{r.status_code}]"+Fore.WHITE)


if __name__ == "__main__":
    main_work()
