"""
Написать функцию host_range_ping() для перебора ip-адресов из заданного диапазона.
Меняться должен только последний октет каждого адреса.
По результатам проверки должно выводиться соответствующее сообщение.
"""
from ipaddress import ip_address, ip_network
from subprocess import PIPE, Popen

import chardet


def host_range_ping():
    for i in range(256):
        IPv4 = ip_address(f'192.168.0.{i}')
        if IPv4 in ip_network('192.168.0.0/24'):
            testip = Popen(['ping', f'192.168.0.{i}'], shell=True, stdout=PIPE, stderr=PIPE)
            stdout_data, stderr_data = testip.communicate()
            result = chardet.detect(stdout_data)
            out = stdout_data.decode(result.get('encoding', None))
            print(out)


host_range_ping()
