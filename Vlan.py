import subprocess

class Vlan:
    def Vlan_change(vlan):
            subprocess.run(["powershell", 'Set-NetAdapter','-Name', '"Ethernet"', "-vlanID", str(vlan), '-Confirm:$false'])