from base64 import b85encode
import json, os

def encoding(value : bytes, encoding="utf-8"):
    return b85encode(bytes(value, encoding))
    
print(""
" ________        __       _______   _______   __     ___  ___      ___      ___       __         _______   \n"
'("      "\      /""\     |   _  "\ |   _  "\ |" \   |"  \/"  |    |"  \    /"  |     /""\       |   __ "\  \n'
' \___/   :)    /    \    (. |_)  :)(. |_)  :)||  |   \   \  /      \   \  //   |    /    \      (. |__) :) \n'
"   /  ___/    /' /\  \   |:     \/ |:     \/ |:  |    \  \/         /\  \/.    |   /' /\  \     |:  ____/   \n"
"  //  \__    //  __'  \  (|  _   \ (|  _   \ |.  |    /\.  \      |: \.        |  //  __'  \    (|  /       \n"
' (:   / "\  /   /  \   \ |: |_)  :)|: |_)  :)/\  |\  /  \   \     |.  \    /:  | /   /  \   \  /|__/ \      \n'
'  \_______)(___/    \___)(_______/ (_______/(__\_|_)|___/\___|    |___|\__/|___|(___/    \___)(_______))\n')

print("\nMay the force be with you young padawan\n")


module = input("\nYou will need some module extention for this programe :\n    pyzabbix\n    WMI\n    ipaddress\nDo you want to install it ? (y/n) : ")
if module == "y":
    os.system('py -m pip install pyzabbix')
    os.system('py -m pip install WMI')
    os.system('py -m pip install ipaddress')

print("\n\n")

def conf() -> list : 
    zabbix_url  : str = encoding(input("Zabbix URL      : ")).decode()
    zabbix_user : str = encoding(input("Zabbix USER     : ")).decode()
    zabbix_pass : str = encoding(input("Zabbix PASSWORD : ")).decode()
    wmi_user    : str = encoding(input("Wmi USER        : ")).decode()
    wmi_pass    : str = encoding(input("Wmi PASSWORD    : ")).decode()
    vlan        = input("Do you have VLAN set up ? (y/n) : ")
    vlan_list : list = []
    if vlan == "y":
        for _ in range(int(input("Who many VLAN do you have : "))):
            vlan_list.append([input("    VLAN number : "), input("    VLAN name : "), input("    Network in this VLAN (192.168.1.0/24) : "), {"selementid": str(_+2), "elementtype": "4", "iconid_off" : "38", "x": input("    X coordinate : "), "y": input("    Y coordinate : "), "label": input("    Label name : "), 'label_location': '-1'}])
            print("    " + "#"*30)
    if vlan == "n":
        networking = input("Do you have multi Network ? (y/n) : ")
        if networking == "y":
            print("Building... Sorry :/")
        if networking == "n":
            print("Then this program is not very useful for u :(")
            exit
    return [zabbix_url, zabbix_user, zabbix_pass, wmi_user, wmi_pass, encoding(json.dumps(vlan_list)).decode()]

f = open('conf', 'w')
f.write("\n".join(conf()))
f.close()