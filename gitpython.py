
class L2vni:
    def __init__(self):
        self.vlan_list = []
        self.name_list = []
        self.tenant_list = []
        self.multi_list = []
        self.ip_list = []
        self.vn_list = []
        self.vn_seg_name = []
        self.name_vlan = []

    def config(self):
        ten = ['PROD', 'DEV', 'STAGE']
        buss = ['SSS', 'TTT', 'JJJ']
        stage = ['DMZ', 'INS', 'DB']
        while True:
            try:
                envir = input('Please enter environment name(PROD/STAGE/DEV): ')
                bus = input('Please enter Business unit(SSS/TTT/JJJ): ')
                stg = input('Please enter stage(DMZ/INS/DB): ')
                if (envir in ten) and (bus in buss) and (stg in stage):
                    tenant = envir + "-" + bus + "-" + stg
                    self.tenant_list.append(tenant)
                    return
                    break
                else:
                    print('Please enter correct environment/business unit again')
            except ValueError:
                continue

    def config1(self):
        cisco1 = self.tenant_list[0]
        total_vlan = input('Please enter total no of vlan required in %s: ' % cisco1 )
        total_vlan = int(total_vlan)
        if total_vlan == 1:
            while True:
                try:
                    no_vlan = int(input('Please enter vlan number: '))
                    if no_vlan < 4096:
                        name_vlan = str(input('Please enter vlan name: '))
                        ip = str(input('Please enter ip address no:  '))
                        multi = str(input('Please enter multicast address no:  '))
                        self.vlan_list.append(no_vlan)
                        self.name_list.append(name_vlan)
                        self.ip_list.append(ip)
                        self.multi_list.append(multi)
                        break
                    else:
                        print("Vlan number is high please reenter vlan less than 4096")

                except ValueError:
                    continue
        else:
            total_vlan > 1
            for i in range(1, total_vlan):
                while (len(self.name_list)) < total_vlan:
                    while True:
                        try:
                            no_vlan = int(input('Please enter vlan %d no: ' % i))
                            if no_vlan < 4096:
                                break
                            else:
                                print("Vlan number is high please reenter vlan should be less than 4096")
                        except ValueError:
                            continue
                    name_vlan = str(input('Please enter vlan name for vlan' + str(no_vlan) + ': '))
                    ip = str(input('Please enter the ip address for vlan' + str(no_vlan) + ': '))
                    multi = str(input('Please enter the multicast address for vlan' + str(no_vlan) + ': '))
                    self.vlan_list.append(no_vlan)
                    self.name_list.append(name_vlan)
                    self.ip_list.append(ip)
                    self.multi_list.append(multi)
                    i = i + 1
        return

    def vnseg(self):
        segment = ['10000', '1000', '100', '10']
        for i in self.vlan_list:
            a = str(i)
            k = len(a)
            if k == 1:
                result = str(segment[0] + a)
            else:
                k = int(k)
                ss = segment[(k-1)]
                result = str(ss + a)
            self.vn_seg_name.append(result)
        return

    def final(self):
        f = len(self.vlan_list)
        print(f)
        for i in range (0,f):
            list = {'id': self.vlan_list[i], 'segment': self.vn_seg_name[i],
                    'name': self.name_list[i], 'multicast': self.multi_list[i], 'tenant':
                        self.tenant_list[0], 'ip': self.ip_list[i]}
            
        final_list = {'L2VNI': list}
        print(final_list)
        return final_list



def main():
    s1 = L2vni()
    s1.config()
    s1.config1()
    s1.vnseg()
    s1.final()
    print(s1.final_list)

    print(s1.tenant_list)
    print(s1.name_list)
    print(s1.vlan_list)
    print(s1.ip_list)
    print(s1.multi_list)
    print(s1.vn_seg_name)


if __name__ == '__main__':
    main()

