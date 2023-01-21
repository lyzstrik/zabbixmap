import wmi

class WMI_infomation:
    def __init__(self, ip, username, password):
        self.ip        = ip
        self.username  = username
        self.password  = password

    def Connection(self):
        try:
            Verif = wmi.WMI(self.ip, user=self.username, password=self.password)
            return Verif
        except wmi.x_wmi:
            return False

    def Computer_infos(self):
        Connection = self.Connection()
        if Connection == False:
            return {'Model': "", 'Name' : "", 'PrimaryOwnerName' : "", 'Roles' : "", 'SystemSKUNumber' : "", 'UserName' : "", 'TotalPhysicalMemory' : "", 'BIOSVersion' : "", 'Manufacturer' : "", 'SerialNumber' : "", 'Version' : ""}
        else:
            c = Connection.Win32_ComputerSystem
            computer = c()[0]
            computer_elements = ['Model', 'Name', 'PrimaryOwnerName', 'Roles', 'SystemSKUNumber', 'UserName', 'TotalPhysicalMemory']
            final = {'Model': "", 'Name' : "", 'PrimaryOwnerName' : "", 'Roles' : "", 'SystemSKUNumber' : "", 'UserName' : "", 'TotalPhysicalMemory' : "", 'BIOSVersion' : "", 'Manufacturer' : "", 'SerialNumber' : "", 'Version' : ""}
            for i in sorted(list(c.properties)):
                if i in computer_elements:
                    final[0][i] = f'{getattr(computer, i)}'
            b = Connection.Win32_Bios
            bios = b()[0]
            bios_elements = ['BIOSVersion', 'Manufacturer', 'SerialNumber', 'Version']
            for i in sorted(list(b.properties)):
                if i in bios_elements:
                    final[0][i] = f'{getattr(bios, i)}'
            return final
