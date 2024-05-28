class IPV4():
    
    def __init__(self, ip, mask):
        self.ip = ip
        self.mask = mask
        # print("ip: "+ ip)
        # print("mask: "+ mask)


    def dez2bin(self, dez):   # wandelt eine Dezimalzahl in eine Binärzahl um 

        ergebnis_bin = ""

        dez = int(dez)
    
        while dez != 0:  
            # wandle das Ergebnis (den Rest von der Teilung durch 2) in eine String und füge sie dem ErgebinisString hinzu
            ergebnis_bin = str(dez % 2) + ergebnis_bin
            
            # erst am Ende teilen
            dez = dez // 2
        # [(8-len(ergebnis_bin)) * "0"] erstellt einen 8-bit String.
        ergebnis_bin = (8-len(ergebnis_bin)) * "0" + ergebnis_bin
        return ergebnis_bin

    def bin2dez(self, bin):
        # bin2dez wandelt eine Binärzahl in eine Dezimalzahl um

        # Horner-Schema:   
        # der Wert der ersten Ziffer als Anfangswert nehmen
        # danach schrittweise das Ergebnis aus dem vorigen Schritt mit 2 multipliziert
        # und die nächste Ziffer addieren bis alle Ziffern aufgebraucht sind.
    
        ergebnis_dez = 0

        for ziffer in bin:
            if ziffer != '1' and ziffer != '0':
                raise TypeError('Binärzahl hat falsches Format')
            ergebnis_dez = ergebnis_dez * 2 + int(ziffer)
        return ergebnis_dez
   
    def mask_32(self):
        if len(self.mask) > 2:
            # => die Maske hat xxx.xxx.xxx.xxx-Format
            okt_1_dez, okt_2_dez, okt_3_dez, okt_4_dez = self.mask.split(".")

            okt_1_bin = self.dez2bin(okt_1_dez)
            okt_2_bin = self.dez2bin(okt_2_dez)
            okt_3_bin = self.dez2bin(okt_3_dez)
            okt_4_bin = self.dez2bin(okt_4_dez)

            mask = str(okt_1_bin) + str(okt_2_bin) + str(okt_3_bin) + str(okt_4_bin)
            
        else:
            
            #if self.mask < 0 or self.mask > 32:
               
            #else:
            count_one = int(self.mask)
            count_zero = 32 - int(self.mask)
            mask = ""
            # Erstellen der Einser anhand der cidr
            while count_one > 0:
                mask = mask + "1"
                count_one -= 1
        
            # Erstellen der Nullen anhand von 32-cidr
            while count_zero > 0:
                mask = mask + "0"
                count_zero -= 1
        
        return mask

    def ip_32(self):
        #erhält eine IP und wandelt diese in eine 32 Zeichenkette um 
        okt_1_dez, okt_2_dez, okt_3_dez, okt_4_dez = self.ip.split(".")

        okt_1_bin = self.dez2bin(okt_1_dez)
        okt_2_bin = self.dez2bin(okt_2_dez)
        okt_3_bin = self.dez2bin(okt_3_dez)
        okt_4_bin = self.dez2bin(okt_4_dez)

        ip = str(okt_1_bin) + str(okt_2_bin) + str(okt_3_bin) + str(okt_4_bin)
        return ip

    def ip_32_first(self, nid):
        # splitet die NID-Adresse in 4 Oktette auf und subtrahiert Eins  
        # von dem letzten Oktett
        
        okt_1_dez, okt_2_dez, okt_3_dez, okt_4_dez = nid.split(".")

        okt_1_bin = self.dez2bin(okt_1_dez)
        okt_2_bin = self.dez2bin(okt_2_dez)
        okt_3_bin = self.dez2bin(okt_3_dez)

        okt_4_dez = int(okt_4_dez) + 1

        okt_4_bin = self.dez2bin(okt_4_dez)

        first = str(okt_1_bin) + str(okt_2_bin) + str(okt_3_bin) + str(okt_4_bin)
        # print("first: " + first)
        return first

    def ip_32_last(self, bc):
        # splitet die BC-Adresse in 4 Oktette auf und addiert Eins
        # zu dem letzten Oktett hinzu

        okt_1_dez, okt_2_dez, okt_3_dez, okt_4_dez = bc.split(".")

        okt_1_bin = self.dez2bin(okt_1_dez)
        okt_2_bin = self.dez2bin(okt_2_dez)
        okt_3_bin = self.dez2bin(okt_3_dez)
        
        okt_4_dez = int(okt_4_dez) - 1
        
        okt_4_bin = self.dez2bin(okt_4_dez)

        last = str(okt_1_bin) + str(okt_2_bin) + str(okt_3_bin) + str(okt_4_bin)
        # print("last: " + last)
        return last

    def createWC(self, mask_32):
        # Erstellt anhand der ausgerechneten Maske die Wildcard
        # die Wildcard ist die Negation der Maske:
        # also aus allen Nullen werden Einser und umgekehrt

        wildcard = ""

        for i in mask_32:
            
            if i == "0":
                wildcard = wildcard + "1"
            elif i == "1":
                wildcard = wildcard + "0"
        
        return wildcard      

    def createIP(self, ip_32):
        # teilt eine 32er Zeichenkette in 4 Oktette
        
        okt_1 = ip_32[0:8]
        okt_2 = ip_32[8:16]
        okt_3 = ip_32[16:24]
        okt_4 = ip_32[24:32]

        # wandelt diese einzelnen Oktette in eine Dezimalzahl um

        okt_1_dez = self.bin2dez(okt_1)
        okt_2_dez = self.bin2dez(okt_2)
        okt_3_dez = self.bin2dez(okt_3)
        okt_4_dez = self.bin2dez(okt_4)
        
        # da die 4 Oktette Integers sind, müssen sie noch in Strings umgewandelt werden  
        ges_Okt = str(okt_1_dez) + "." + str(okt_2_dez) + "." + str(okt_3_dez) + "." + str(okt_4_dez)

        return ges_Okt

    def get_nid(self):

        ip_32 = str(self.ip_32())
        mask_32 = str(self.mask_32())
                
        nid_32 = ""
        a = 0
        
        for i in ip_32:
        
            if ip_32[a] == "0" and mask_32[a] == "0":
                nid_32 = nid_32 + "0"
        
            elif ip_32[a] == "1" and mask_32[a] == "0":
                nid_32 = nid_32 + "0"
        
            elif ip_32[a] == "0" and mask_32[a] == "1":
                nid_32 = nid_32 + "0"
        
            elif ip_32[a] == "1" and mask_32[a] == "1":
                nid_32 = nid_32 + "1"
        
            a += 1
        
        nid = self.createIP(nid_32)
        # print("nid: "+nid)      
        #   
        return nid
        
    def get_bc(self):
        # Berechnet den BC mit einer ODER-Verknüpfung von der IP und der Wildcard
        # 0 UND 0 ist 0    # 1 UND 0 ist 1    # 0 UND 1 ist 1    # 1 UND 1 ist 1
        
        # Die Wildcard ist die Negation von der Maske

        # Bsp:
        # MASK:     11111111111111111111111100000000
        # WILDCARD: 00000000000000000000000011111111
        # IP:       10000111010011101011100100001111
        # BC:       10000111010011101011100111111111
        ip_32 = str(self.ip_32())
        mask_32 = str(self.mask_32())

        bc_32 =""

        # wandelt die Maske in eine Wildcard um
        wc_32 = self.createWC(mask_32)
        
        a = 0
        # Notiz an mich: hier ist, denk ich, kein a nötig. kännte mir also eine variable sparen

        # bin and und or
        
        # Logisches ODER der BC und WC
        for i in ip_32:
        
            if ip_32[a] == "0" and wc_32[a] == "0":
                bc_32 = bc_32 + "0"
        
            elif ip_32[a] == "1" and wc_32[a] == "0":
                bc_32 = bc_32 + "1"
        
            elif ip_32[a] == "0" and wc_32[a] == "1":
                bc_32 = bc_32 + "1"
        
            elif ip_32[a] == "1" and wc_32[a] == "1":
                bc_32 = bc_32 + "1"
        
            a += 1
        
        bc = self.createIP(bc_32)
        # print("bc: "+bc)

        return bc

    def get_first(self):
        # berechnet die erste "nutzbare" IP-Adresse in einem Netzwerk
        # und gibt diese zurück

        # berechnet die Netz-Adresse und kommt als IP zurück
        nid = self.get_nid()

        # erstellt aus der zuvor erstellten Netz-Adresse eine 32 bit lange Zeichenkette
        # und fügt dem letzten Oktett 1(Eins) hinzu
        first_32 = self.ip_32_first(nid)

        # wandelt die 32 bit lange Zeichhenkette in eine IP um
        first = self.createIP(first_32)
        
        # print("first: "+ first)

        return first
    
    def get_last(self):
        # berechnet die letzte "nutzbare" IP-Adresse in einem Netzwerk und gibt
        # diese zurück
        
        # die Broadcast-Adresse wird berechnet und kommt als IP zurück
        bc = self.get_bc()

        # erstellt aus der zuvor erstellten Broadcast-IP eine 32 bit lange Zeichenkette
        # und zieht von dem letzten Oktett 1(Eins) ab   
        last_32 = self.ip_32_last(bc)

        # wandelt die 32 bit lange Zeichhenkette in eine IP um
        last = self.createIP(last_32)     
               
        # print("last: "+last)

        return last