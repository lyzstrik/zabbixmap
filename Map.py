from ZabbixCommands import command
from Cercle import Rayon_Grand_Cercle, Host, Coodonne_host
import json

class Map:
    def __init__(self, name, build, elements):
        self.name = name
        self.build = build
        self.elements = elements

    def get_map_id(self):
        zapi_map = command('mg')
        result = [i['sysmapid'] for i in zapi_map if i['name']==self.name]
        return result

    def central_element(self):
        return {
            "selementid"    : "1" ,
            "elements"      : []  , 
            "elementtype"   : "4" ,
            "iconid_off"    : "129" ,
            "x"             : 1400,                     # Change those elements
            "y"             : 850 ,                     # 
            'label'         : 'Gateway'  ,
            'label_location': '-1'
        }

    def get_host_group_id(self, groupname):
        result = []
        hg = command('hg', output=['hostid'], selectGroups="extend")
        for i in hg:
            if i['groups'][0]['name'] == groupname:
                result.append(i["hostid"])
        return result

    def get_all_host(self, hostgroup):
        zapi_host = command('hg', selectGroups="extend")
        result    = {}
        name_id   = {}
        for vlan in self.build:
            name_id[vlan[1]] = vlan[3]['selementid']
        for host in zapi_host:
            print(host['host'])
            if host['groups'][0]['name'] == hostgroup:
                description = host['description'].split('\n')
                icon = description[0]
                ip   = description[1]
                utilisateur = description[2]
                result[host['host']] = [host['hostid'], icon, name_id[host['groups'][0]['name']], ip, utilisateur, host['host']]
        return result


    def around_central(self):
        x, y = self.central_element()["x"], self.central_element()["y"]
        compte = 0
        for i in self.build:
            compte += 1
        rayon = Rayon_Grand_Cercle(compte, 32, Pourcentage_Cercle=2)  #valeur à ajuster
        return Coodonne_host(compte, rayon, x, y)

    def around_vlan(self, vlan):
        result  = []
        print("DEBUG DE FOU")
        x, y  = vlan[3]["x"],vlan[3]["y"]
        print(x, y)
        compte = 0
        for allo in self.get_host_group_id(vlan[1]):
            compte += 1
        rayon = Rayon_Grand_Cercle(compte, 20, Pourcentage_Cercle=2)  #valeur à ajuster 
        result.append(Coodonne_host(compte, rayon, x, y))
        return result

    def map_elements(self):
        result_map_elements = []
        result_map_links    = []
        coo_by_name         = []
        coo                 = 0
        result_map_elements.append(self.central_element())
        compte    = 13
        print("GIGA DEBUG")
        print(self.build)
        print(type(self.build))
        for vlan in self.build:
            print('IN THE BOUCLE OF BUILD')
            print(vlan)
            print(vlan[3])
            selementid = vlan[3]['selementid']
            result_map_elements.append(vlan[3])
            result_map_links.append({
                'selementid1' : "1",
                'selementid2' : selementid,
                'color'       : '0040FF',
            })
            for i in self.around_vlan(vlan)[coo]:
                coo_by_name.append([selementid, i['x'], i['y']])
            coo += 1
            get_all_host = self.get_all_host(vlan[1])
            for host in get_all_host:
                id   = get_all_host[host][0]
                icon = get_all_host[host][1]
                se_id = get_all_host[host][2]
                label_ip = get_all_host[host][3]
                label_utilisateur = get_all_host[host][4]
                name = get_all_host[host][5]
                for i in coo_by_name:
                    if se_id == i[0]:
                        x = i[1]
                        y = i[2]
                        coo_by_name.remove(i)
                        break
                result_map_elements.append({
                        "selementid"    : str(compte),
                        "elements"      : [{'hostid': id}],
                        "elementtype"   : "0",
                        "iconid_off"    : icon,
                        "x"             : x,
                        "y"             : y,
                        'label'         : f'{name}\n{label_ip}\n{label_utilisateur}',
                        'label_location': '-1'
                    })
                result_map_links.append({
                    'selementid1' : se_id,
                    'selementid2' : str(compte),
                })
                compte += 1
        return result_map_elements, result_map_links

    def creat_map(self):
        map_elements, link = self.map_elements()
        return command('mc',
            name      = self.name    ,
            width     = "10000"      ,
            height    = "10000"      ,
            selements = map_elements ,
            links     = link,
            label_type = '0' 
            )

    def update_map(self):
        map_id = self.get_map_id()[0]
        map_elements, link = self.map_elements()
        return  command('mu',
                sysmapid  = map_id         ,
                name      = self.name      ,
                width     = "10000"        ,
                height    = "10000"        ,
                selements = map_elements   ,
                links     = link,
                label_type = '0' 
                )

    def verif_map(self):
        self.creat_map()

