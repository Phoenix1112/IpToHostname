import re
import os
import sys
import requests
import argparse
import threading
from colorama import *
from concurrent.futures import ThreadPoolExecutor

requests.packages.urllib3.disable_warnings()

class HostFind():
    
    def __init__(self):
        
        init(autoreset=True)
        self.ip_list = []
        self.print_lock = threading.Lock()
    
        if args.list:
    
            if not os.path.exists(args.list):
                print(Fore.MAGENTA + "Ip List Not Found In This Path: {}".format(args.list))
                sys.exit()

            x = open(args.list, "r").read().split("\n")
            self.ip_list.extend(list(set(filter(None, x))))

            if not len(self.ip_list) > 0:
                print(Fore.MAGENTA + "Ip List Is Empty: {}".format(args.list))
                sys.exit()

            del x

        else:
            print(Fore.MAGENTA + "You Need To Use --list Param")
            sys.exit()

        if args.target:

            self.reg_target = args.target.replace(".", "\.").replace("-", "\-").replace("_", "\_")
            self.reg_target = "[a-zA-Z0-9._-]+" + self.reg_target + "|" + self.reg_target

        else:
            print(Fore.MAGENTA + "You Need To Use --target Param")
            sys.exit()

        with ThreadPoolExecutor(max_workers=args.thread) as executor:
            executor.map(self.start, self.ip_list)

    def start(self,ip):

        try:

            response = requests.get("https://www.ip-tracker.org/locator/ip-lookup.php?ip="+str(ip), verify=False, timeout=args.timeout, allow_redirects=False,headers={"User-Agent": "Mozilla Firefox 66.00"})

            if args.target in response.text:

                regex = re.findall(self.reg_target,response.text)

                with self.print_lock:

                    print(Fore.GREEN + "[" + Fore.MAGENTA + "FOUND" + Fore.GREEN + "]", Fore.YELLOW + str(ip), Fore.MAGENTA + ">>>", Fore.CYAN + str(regex[0]))

                if args.output:
                    self.print_output(ip,regex[0])

        except:
            pass

    def print_output(self,ip,sub):

        with open(args.output, "a+") as file:

            file.write(str(ip) + "," + str(sub) + "\n")


if __name__ == "__main__":

    ap = argparse.ArgumentParser()
    ap.add_argument("--list", metavar="", required=True, help="Path Of Ip Address List")
    ap.add_argument("--output", metavar="", required=False, help="Save Output")
    ap.add_argument("--target", metavar="", required=True, help="Match Target Name")
    ap.add_argument("--thread", metavar="", required=False, default=50, type=int, help="Thread Number(Default-50)")
    ap.add_argument("--timeout", metavar="", required=False, default=8, type=int, help="Requests Timeout(Default-8)")
    args= ap.parse_args()

    run = HostFind()
