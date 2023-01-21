import math, os

os.system('cls')

class Cercle:
    def __init__(self):
        pass

    def Rayon_Grand_Cercle(self, nbr_host, Rayon_Host, Pourcentage_Cercle=1):
        taille_cercle = 360//Pourcentage_Cercle
        alpha = (taille_cercle//nbr_host)/2
        haut_div = Rayon_Host
        bas_div  = math.sin(math.radians(alpha))
        result   = haut_div/bas_div
        return round(result)

    
    def Host(self, Diametre_Petit_Cercle, Rayon_Grand_Cercle):
        haut_div1 = -Diametre_Petit_Cercle**2
        haut_div2 = 2*Rayon_Grand_Cercle**2
        bas_div   = 2*Rayon_Grand_Cercle**2
        div       = (haut_div1 + haut_div2) / bas_div
        arcos     = round(math.acos(div)*(180/math.pi), 2)
        result    = 360//arcos
        return result

    def Coodonee_host(self, nbr_hosts, rayon_cercle, centre_x, centre_y):
        alpha  = 360//nbr_hosts
        compte = 0
        result = []
        for i in range(nbr_hosts):
            compte += alpha
            result.append({
                'x': int(centre_x) + round(math.sin(math.radians(compte))*rayon_cercle, 0),
                'y': int(centre_y) + round(math.cos(math.radians(compte))*rayon_cercle, 0)
            })
        return result
    

client = Cercle()
Rayon_Grand_Cercle = client.Rayon_Grand_Cercle
Host               = client.Host
Coodonne_host      = client.Coodonee_host