from base64 import b85decode
from pyzabbix import ZabbixAPI

def decrypt():
    f = open("conf", "r")
    all_lignes = f.read().split("\n")
    f.close()
    return [b85decode(all_lignes[0]).decode(), b85decode(all_lignes[1]).decode(), b85decode(all_lignes[2]).decode()]

class ZapiCommands:
    def __init__(self, *args):
        self.zapi = ZabbixAPI(args[0], user=args[1], password=args[2])
        self.commands = {
            'ac'   : 'action.create',
            'ad'   : 'action.delete',
            'ag'   : 'action.get',
            'au'   : 'action.update',
            'alg'  : 'alert.get',
            'dc'   : 'dashboard.create',
            'dd'   : 'dashboard.delete',
            'dg'   : 'dashboard.get',
            'du'   : 'dashboard.update',
            'gc'   : 'graph.create',
            'gd'   : 'graph.delete',
            'gg'   : 'graph.get',
            'gu'   : 'graph.update',
            'hc'   : 'host.create',
            'hd'   : 'host.delete',
            'hg'   : 'host.get',
            'hu'   : 'host.update',
            'hma'  : 'hostmassadd',
            'hmr'  : 'hostmassremove',
            'hmu'  : 'hostmassupdate',
            'hgc'  : 'hostgroup.create',
            'hgd'  : 'hostgroup.delete',
            'hgg'  : 'hostgroup.get',
            'hgma' : 'hostgroup.massadd',
            'hgmr' : 'hostgroup.massremove',
            'hgmu' : 'hostgroup.massupdate',
            'hgu'  : 'hostgroup.update',
            'hig'  : 'hostinterface.get',
            'ic'   : 'iconmap.create',
            'id'   : 'iconmap.delete',
            'ig'   : 'iconmap.get',
            'iu'   : 'iconmap.update',
            'itg'  : 'item.get',
            'hic'  : 'hostinterface.create',
            'hid'  : 'hostinterface.delete',
            'hig'  : 'hostinterface.get',
            'hima' : 'hostinterface.massadd',
            'himr' : 'hostinterface.massremove',
            'hiri' : 'hostinterface.replacehostinterfaces',
            'hiu'  : 'hostinterface.update',
            'mg'   : 'map.get',
            'mu'   : 'map.update',
            'mc'   : 'map.create',
            'md'   : 'map.delete',
            'tdc'  : 'templatedashboard.create',
            'tdd'  : 'templatedashboard.delete',
            'tdg'  : 'templatedashboard.get',
            'tdu'  : 'templatedashboard.update',
            't'    : 'trigger.get',
        }

    def command(self, command_name, **kwarg):
        method = self.zapi
        fonction_name = self.commands[command_name]
        fonction_name = fonction_name.split('.')
        for i in fonction_name:
            method = getattr(method, i)
        return method(**kwarg)

command = ZapiCommands(*decrypt()).command