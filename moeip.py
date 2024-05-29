class IP(object):
    class Version(object):
        ipv4 = 1
        ipv6 = 2
        error = 99

    def __init__(self, adress, mask="", version=Version.ipv4):
        if version==self.Version.ipv4:
            if  adress.isdigit():           # BigInt Adresse
                self.addr = self.comp_addr(int(adress))
                self.cidr = "24"
                self.version = version
            elif "/" in adress:
                addr_cut = adress.split("/") # "192.196.0.1/24"
                self.addr=addr_cut[0]
                if  addr_cut[1].isdigit():   
                    self.cidr=addr_cut[1]
                else:                        # "192.166.0.1/255.255.255.0"
                    self.cidr = str(self.comp_mask_to_cidr(addr_cut[1]))
                self.version = version
            else:                            # "192.168.0.1","255.255.255.0"
                self.addr = adress
                self.cidr = str(self.comp_mask_to_cidr(mask))             
            if not self.testipv4():          # Test nicht bestanden
                self.addr=""
                self.cidr=""
                self.version = self.Version.error


    def __str__(self):
        if self.version == self.Version.ipv4:
            return f"{self.addr}/{self.cidr}"
        elif self.version == self.Version.error:
            return self.error
        
    def testipv4(self):

        self.error = ""
        if self.addr.count('.') != 3: # 4 Oktetts
            self.error += "Fehler im Addressbereich (falsche Anzahl '.'.)\n"
        else:
            add_cut = self.addr.split('.')
            for counter, addr in enumerate(add_cut):
                if  not addr.isdigit() or int(addr) < 0 or int(addr) > 255:
                    self.error += f"Fehler im {counter+1}. Oktett.\n"
        if  not self.cidr.isdigit() or int(self.cidr) < 0 or int(self.cidr) > 32:
            self.error += "Fehler in der CIDR.\n"
        return True if len(self.error)==0 else False
    
    def get_int(self):
        if self.version == self.Version.ipv4:
            add_cut = self.addr.split('.')
            number = 0
            for addr in add_cut:
                number = number * 256 + int(addr)
            return number
        else:
            return -1
        
    def get_nid(self):

        return '.'.join([str(int(addr) & int(mask)) for addr, mask in zip(self.addr.split('.'), self.get_mask().split('.'))])
        
    def get_bc(self):

        return '.'.join([str(256+(int(addr) | ~int(mask))) for addr, mask in zip(self.addr.split('.'), self.get_mask().split('.'))])
        
    
    def get_mask(self):
        # return mask as string
        number = int(self.cidr)
        mask = ""
        for i in range(3):
            if number >= 8:
                mask += "255"
                number -= 8
            else:
                mask += str([0, 128, 192, 224, 240, 248, 252, 254, 255][number])
                number = 0
            mask += "."
        mask += str([0, 128, 192, 224, 240, 248, 252, 254, 255][number])
        return mask

    def calc_addr(self, number):
        # calc a address from int to string
        add = ""
        for i in range(3):
            add = "."+str(number % 256) + add
            number = number // 256
        add = str(number)+add
        return add

    def calc_mask_to_cidr(self,mask):
        # calc a string mask from a cdir
        mask_split = mask.split('.')
        cidr = 0
        for i in range(3):
            cidr += [0, 128, 192, 224, 240, 248, 252, 254, 255].index(int(mask_split[i]))
        return cidr
    
    def add_range(self, range):
        number2 = IP(str(self.get_int() + range))
        return str(number2)

if __name__== '__main__':
    ip1 = IP('128.244.23.130/25')
    print(ip1,ip1.get_int())
    print(ip1.get_nid(), ip1.get_bc())