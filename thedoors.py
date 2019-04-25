#!/usr/bin/python3
import os, sys, argparse
from subprocess import call


def get_user():
    return os.getcwd().split('/')[2]

def thedoors():
    parser = argparse.ArgumentParser(description="Insert output ports into IPTABLES includes within a file called $USER.output.")

    parser.add_argument("-p", "--port", metavar="", action="store", type=str, help="The number of the output port to be open.")

    args = parser.parse_args()

    user = get_user()
    #out_file = "/etc/firewall/conf/includes/"+user+".output"
    out_file = user+".output"
    if args.port:
        ports_array = args.port.split(",")
        for key in range(0, len(ports_array)):
            with open(out_file, "a") as text_file:
                thedoors = ports_array[key]
                text_file.write("-p tcp --dport %s -m owner --uid-owner %s -j ACCEPT\n" % (thedoors, user))

        call(["service", "firewall", "restart"])
    else:
        print("\n  Sorry, use -h for the options.\n")

thedoors()
