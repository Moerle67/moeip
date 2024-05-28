

class IP(object):
    class Version(object):
        ipv4 = 1
        ipv6 = 2
        error = 99

    def __init__(self, adress, mask="", version=Version.ipv4):
        if "/" in adress:
            addr_cut = adress.split("/")
            self.addr=addr_cut[0]
            self.cidr=addr_cut[1]
            self.version = version
            if self.version == self.Version.ipv4:
                if not self.testipv4():
                    self.addr=""
                    self.cidr=""
                    self.version = self.version = self.Version.error
                    


    def __str__(self):
        if self.version == self.Version.ipv4:
            return f"{self.addr}/{self.cidr}"
        elif self.version == self.Version.error:
            return self.error
        
    def testipv4(self):

        self.error = ""
        if self.addr.count('.') != 3:
            self.error += "Fehler im Addressbereich (falsche Anzahl '.'.)\n"
        else:
            add_cut = self.addr.split('.')
            for counter, addr in enumerate(add_cut):
                if  not addr.isdigit() or int(addr) < 0 or int(addr) > 255:
                    self.error += f"Fehler im {counter+1}. Oktett.\n"
        if  not self.cidr.isdigit() or int(self.cidr) < 0 or int(self.cidr) > 32:
            self.error += f"Fehler in der CIDR.\n"
        return True if len(self.error)==0 else False
    
    def getint(self):
        if self.version == self.Version.ipv4:
            add_cut = self.addr.split('.')
            number = 0
            for addr in add_cut:
                number = number * 256 + int(addr)
            return number
        else:
            return -1
    
    def compaddr(number):
        add = ""
        for i in range(3):
            add = "."+str(number % 256) + add
            number = number // 256
        add = str(number)+add
        return add


if __name__== '__main__':
    ip1 = IP('192.244.23.1/24')
    print(ip1,ip1.getint())
    print(IP.compaddr(3237222145))