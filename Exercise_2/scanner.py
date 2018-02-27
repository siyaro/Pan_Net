#!/usr/bin/python
import sys
from scapy.all import *
import ipaddress
import json

#Sample Json File:
#
# result = {
#     "IP_Address_1" : ["open_port_1", "open_port_2", ... , "open_port_n"],
#     "IP_Address_2" : ["open_port_1", "open_port_2", ... , "open_port_n"],
#     ...,
#     "IP_Address_n" : ["open_port_1", "open_port_2", ... , "open_port_n"]
# }


# scanner.py 10.2.2.1
# scanner.py 10.2.2.0/24
# scammer.py 10.2.2.0 255.255.255.0


dst_list = [80, 123, 443, 8080, 1024, 8443, 22, 53, 631]
scanRes = {}
readRes = {}
fileEx = True



def net_to_host(network):
    print network
    print (list(network.hosts()))
    scan(list(network.hosts()))


def scan(ip_list):
    for dst_ip in ip_list:
        for dst_port in dst_list:
            src_port = RandShort()
            stealth_scan_resp = sr1(IP(dst=str(dst_ip))/TCP(sport=src_port, dport=dst_port, flags="S"), timeout=10, verbose=0)
            if (str(type(stealth_scan_resp)) == "<type 'NoneType'>"):
                pass
            elif (stealth_scan_resp.haslayer(TCP)):
                if (stealth_scan_resp.getlayer(TCP).flags == 0x12):
                    send_rst = sr(IP(dst=str(dst_ip))/TCP(sport=src_port, dport=dst_port, flags="R"), timeout=10, verbose=0)
                    open_res(str(dst_ip), str(dst_port))
                elif (stealth_scan_resp.getlayer(TCP).flags == 0x14):
                    pass
            elif (stealth_scan_resp.haslayer(ICMP)):
                if (int(stealth_scan_resp.getlayer(ICMP).type) == 3 and int(stealth_scan_resp.getlayer(ICMP).code) in [1, 2, 3, 9, 10,13]):
                    pass
        check(str(dst_ip))
    store()

def open_res(IP, port):
    global scanRes
    if IP not in scanRes.keys():
	scanRes[IP] = [port]
    else:
	scanRes[IP].append(port)

def other_res(IP, port):
    pass

def check(IP):
    #print ("Checker")
    # *Target - 10.1.1.1: Full scan results:*
    # Host: 10.1.1.1      Ports: 22/open/tcp////
    # Host: 10.1.1.1      Ports: 25/open/tcp////
    # Host: 10.1.1.1      Ports: 80/open/tcp////
    global fileEx
    global scanRes
    global readRes
    priRep = {}
    if fileEx :
        if IP in scanRes.keys():
            for port in scanRes[IP]:
                if port not in readRes[IP]:
                    priRep[IP].append(port)
            if len(priRep) == 0:
                printer(False,IP)
            else:
                printer(True, priRep)
    else:
	if IP in scanRes.keys():
            for port in scanRes[IP]:
                if IP not in priRep.keys():
		    priRep[IP] = [port]
		else:
                    priRep[IP].append(port)
            printer(True,priRep)

def printer(Rec, dic):
    if Rec :
        print ("*Target - " + dic.keys()[0] + ": Full scan results:*")
        for key in dic.keys():
            for port in dic[key]:
                print ("Host: " + str(key) + "\t\t" + "Ports: " + str(port) + "/open/tcp////")
    else:
        print ("*Target - " + str(dic) + ": No new records found in the last scan.*")


def store():
    global scanRes
    with open('result.json', 'w') as fp:
        json.dump(scanRes, fp)

def readFile():
    global readRes
    global fileEx
    try:
        readRes = json.load(open('result.json'))
    except IOError:
        fileEx = False

#MAIN
args = sys.argv
readFile()
if len(args) > 1 :
    if "/" in args[1] :
        scRan = ipaddress.ip_network(unicode(args[1]))
        net_to_host(scRan)
    elif len(args) == 3 :
        scRan = ipaddress.ip_network(unicode(args[1] + "/" + args[2]))
        net_to_host(scRan)
    else:
        scRan = [ipaddress.IPv4Address(unicode(args[1]))]
        scan(scRan)
else:
    print("USAGE: scanner.py <IP_address> OR <Address/subnetmask>")
