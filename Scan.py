import subprocess, os, ipaddress, socket
from WMI import WMI_infomation

os.system('cls')

class Stockage:
    boite_de_pandore = []

class Stokage:
    le_2 = []

class Network:
    def __init__(self, network : str):
        self.network = [str(ip) for ip in list(ipaddress.IPv4Network(network, strict=False))][2:-1]

    def __iter__(self):
        return (i for i in self.network)

class Path:
    def __init__(self, file, depth = -1):
        self.file = file
        self.depth = depth

    def get_file(self):
        base = os.path.dirname(__file__).split("\\")[:self.depth]
        base.append(f"{self.file}")
        return "/".join(base)

class Icon:
    def get_info(ip) -> str:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(0.1)
        result = ""
        if sock.connect_ex((ip, 9100)) == 0:
            result = "83"                      #Number of Printer Icon
        elif sock.connect_ex((ip, 22)) == 0:   
            result = "54"                      #Number of FTP server (change number of icon as you want)
        else:
            result = "68"
        sock.close()
        return result

class Scan(Network):
    def __init__(self, network: str, user="admin", password="C'est une feinte"):
        super().__init__(network)
        self.gateway = self.network[0]
        self.user = user
        self.password = password
        self.stock = Stockage.boite_de_pandore
        self.stock_2 = Stokage.le_2
        
    def ping(self):
        for ip in self.network:
            if "octets=" not in str(subprocess.run(['ping', '-n', '1', str(ip)], capture_output=True, shell=False).stdout):
                self.network.remove(ip)
        self.network.remove("10.1.78.3")

    
    def mass_scan(self):
        rand = []
        for ip in self.network:
            print(ip)
            arp = str(subprocess.run(['arp','-a', str(ip)], capture_output=True, shell=False).stdout)
            if "Aucune entr" not in arp:
                mac_name = arp[40:].split(ip)[1].split("dynamique")[0].replace(" ", "").upper()
                f = open("mac.txt", "r", encoding="utf-8")
                rand.append(ip)
                rand.append(mac_name)
                try:
                    rand.append(f.read().split(mac_name[:8])[1][3:].split("\n")[0])
                except:
                    rand.append("")
                f.close()
            rand.append(Icon.get_info(ip))
            rand.append(WMI_infomation(ip, self.user, self.password).Computer_infos())
            self.stock.append(rand)
        self.stock_2.append(self.stock)