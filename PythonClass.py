class Personel():
    ad=str()
    departman=str()
    calismaYil=int()
    maas=int()
    def __init__(self,ad,departman,calismaYil,maas):
        self.ad=ad
        self.departman=departman
        self.calismaYil=calismaYil
        self.maas=maas
    
class Firma():
    
    personel_listesi=[]    
    def personel_ekle(self,kisi):
        self.personel_listesi.append(kisi)
    
    
    
    def personel_listele(self):
        for personel in self.personel_listesi:
            print("Ad:", personel.ad)
            print("Departman:", personel.departman)
            print("Çalışma Yılı:", personel.calismaYil)
            print("Maaş:", personel.maas)
            print()
    
    
    def maas_zammi(self,kisi,zam_oran):
        yeni_maas=kisi.maas*(1+zam_oran)
        kisi.maas=yeni_maas
    
    
    def personel_cikart(self,kisi):
        self.personel_listesi.remove(kisi)    





    







  