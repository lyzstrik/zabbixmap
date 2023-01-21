from ZabbixCommands import command

class HostGroupCreat:
    def __init__(self):
        ...

    def get_host_group_id(self, name):
        hg = command('hgg', filter={'name': name})
        return hg[0]['groupid']

    def host_group_creat(self, hostname):
        return command('hgc',
            name = hostname
        )

    def host_group_update(self, hostname):
        id = self.get_host_group_id(hostname)
        return command('hgu',
            groupid = id,
            name = hostname
        )
    
    def verif_host_group(self, hostname):
        try:
            return self.host_group_creat(hostname)
        except:
            return self.host_group_update(hostname)


host_group = HostGroupCreat().verif_host_group