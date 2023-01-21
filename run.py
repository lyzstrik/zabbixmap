from base64 import b85decode
from Vlan import Vlan
from Scan import Scan
from Zabbix_Host_Group import host_group
from Zabbix_Host import host
from Map import Map
import subprocess, threading, time, json


def decrypt():
    f = open("conf", "r")
    all_lignes = f.read().split("\n")
    f.close()
    return [b85decode(all_lignes[3]).decode(), b85decode(all_lignes[4]).decode(), b85decode(all_lignes[5]).decode()]

class ELscaner:
    def ex(packets):
        for index, elements in enumerate(json.loads(packets[2])):
            Vlan.Vlan_change(elements[0])
            scan = Scan(elements[2], packets[0], packets[1])
            scan.ping()
            scan.mass_scan()
            host_group(elements[1])
            host(elements[1], scan.stock[index][0], scan.stock[index][1], scan.stock[index][2], scan.stock[index][3], *[{i:j} for i,j in scan.stock[index][4].items()])
        Map("Test", json.loads(packets[2]), scan.stock_2).verif_map()

ELscaner.ex(decrypt())