from ZabbixCommands import command

class HostCreat:
    def __init__(self) -> None:
        ...

    def get_host_group_id(self, name):
        hg = command('hgg', filter={'name': name})
        return hg[0]['groupid']

    def get_host_id_by_name(self, mac):
        hg = command('hg', filter={'host': mac})
        return hg[0]['hostid']

    def host_creat(self, group, ip, mac, mac_prov, icon, *args : dict):
        if not mac_prov:
            hostname_result = mac
        else:
            hostname_result = mac_prov
        print(list(args[3].values())[0])
        if list(args[3].values())[0] != "":
            descrip = "{}\n{}".format(ip, list(args[4].values())[0])
        else:
            descrip = f'""\n""'
        print(hostname_result)
        return command(
            'hc',
            host = hostname_result,
            description = f"{icon}\n{descrip}",
            interfaces = [{
                "type": 1,
                "main": 1,
                "useip": 1,
                "ip": ip,
                "dns": "stcyr.net",
                "port": "10050" 
            }],
            groups = {
                "groupid" : group
            },
            tags = [{
                "tag": "Host name",
                "value": hostname_result
            }],
            macros = [
                {
                    "macro": "{$USER_ID}",
                    "value": "123321"
                },
                {
                    "macro": "{$USER_LOCATION}",
                    "value": "0:0:0",
                    "description": "latitude, longitude and altitude coordinates"
                }
            ],
            inventory_mode = 0,
            inventory = {
                "macaddress_a"  : mac,
                "macaddress_b"  : mac_prov,
                "name"          : list(args[1].values())[0],
                "alias"         : list(args[4].values())[0],
                "hardware"      : list(args[0].values())[0],
                "software"      : list(args[2].values())[0],
                "hardware_full" : f"Manufacturer: {list(args[7].values())[0]}\nVersion : {list(args[9].values())[0]}\nRoles : {list(args[3].values())[0]}\nBios Version : {list(args[6].values())[0]}\nSystemSKUNumber : {list(args[4].values())[0]}\nUtilisateur : {list(args[5].values())[0]}",
                "serialno_a"    : list(args[8].values())[0],
            }
        )

    
    def host_update(self, group, hostid, ip, mac, mac_prov, icon, *args : dict):
        if not mac_prov:
            hostname_result = mac
        else:
            hostname_result = mac_prov
        if list(args[3].values())[0] != "":
            descrip = "{}\n{}".format(ip, list(args[4].values())[0])
        else:
            descrip = f'""\n""'
        return command(
            'hu',
            hostid = hostid,
            host = hostname_result,
            description = f"{icon}\n{descrip}",
            interfaces = [{
                "type": 1,
                "main": 1,
                "useip": 1,
                "ip": ip,
                "dns": "stcyr.net",
                "port": "10050" 
            }],
            groups = {
                "groupid" : group
            },
            tags = [{
                "tag": "Host name",
                "value": hostname_result
            }],
            macros = [
                {
                    "macro": "{$USER_ID}",
                    "value": "123321"
                },
                {
                    "macro": "{$USER_LOCATION}",
                    "value": "0:0:0",
                    "description": "latitude, longitude and altitude coordinates"
                }
            ],  
            inventory_mode = 0,
            inventory = {
                "macaddress_a"  : mac,
                "macaddress_b"  : mac_prov,
                "name"          : list(args[1].values())[0],
                "alias"         : list(args[4].values())[0],
                "hardware"      : list(args[0].values())[0],    
                "software"      : list(args[2].values())[0],
                "hardware_full" : f"Manufacturer: {list(args[7].values())[0]}\nVersion : {list(args[9].values())[0]}\nRoles : {list(args[3].values())[0]}\nBios Version : {list(args[6].values())[0]}\nSystemSKUNumber : {list(args[4].values())[0]}\nUtilisateur : {list(args[5].values())[0]}",
                "serialno_a"    : list(args[8].values())[0],
            }
        )
 

    def host_verif(self, group, ip, mac, mac_prov, icon, *args):
        group = self.get_host_group_id(group)
        try:
            self.host_creat(group, ip, mac, mac_prov, icon, *args)
        except:
            hostid = self.get_host_id_by_name(mac_prov)
            return self.host_update(group, hostid, ip, mac, mac_prov, icon, *args)


host = HostCreat().host_verif
