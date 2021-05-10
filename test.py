from classes.calcipv4 import CalcIPv4

if __name__ == '__main__':
    
    calc_ipv4 = CalcIPv4(ip="192.168.0.1", mask='255.255.255.192')

    print(f'IP: {calc_ipv4.ip}')
    print(f'Mask: {calc_ipv4.mask}')
    print(f'Net: {calc_ipv4.net}')
    print(f'Broadcast: {calc_ipv4.broadcast}')
    print(f'Prefix: {calc_ipv4.prefix}')
    print(f'Numbers of IPs: {calc_ipv4.num_of_ips}')
