from ipaddress import ip_address, ip_network
from subprocess import PIPE, Popen

import chardet
from tabulate import tabulate


def host_range_ping_tab():
    reachable = {'reachable': []}
    unreachable = {'unreachable': []}
    for i in range(256):
        IPv4 = ip_address(f'192.168.0.{i}')
        if IPv4 in ip_network('192.168.0.0/24'):
            reachable['reachable'].append(f'192.168.0.{i}')
            print(tabulate(reachable, headers=['Reachable']))
            testip = Popen(['ping', f'192.168.0.{i}'], shell=True, stdout=PIPE, stderr=PIPE)
            stdout_data, stderr_data = testip.communicate()
            result = chardet.detect(stdout_data)
            out = stdout_data.decode(result.get('encoding', None))
            print(out)
        else:
            unreachable['unreachable'].append(f'192.168.0.{i}')
            print(tabulate(unreachable, headers=['Unreachable']))


host_range_ping_tab()
