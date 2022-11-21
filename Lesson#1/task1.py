""""
Написать функцию host_ping(), в которой с помощью утилиты ping будет проверяться доступность сетевых узлов.
Аргументом функции является список, в котором каждый сетевой узел должен быть представлен именем хоста или ip-адресом.
В функции необходимо перебирать ip-адреса и проверять их доступность с выводом соответствующего сообщения («Узел доступен», «Узел недоступен»).
 При этом ip-адрес сетевого узла должен создаваться с помощью функции ip_address()
 """

from ipaddress import ip_address, ip_network
from subprocess import PIPE, Popen

import chardet


def host_ping(urls: []):
    for url in urls:
        IPv4 = ip_address(url)
        if IPv4 in ip_network('192.168.0.0/24'):
            testip = Popen(['ping', url], shell=True, stdout=PIPE, stderr=PIPE)
            stdout_data, stderr_data = testip.communicate()
            result = chardet.detect(stdout_data)
            out = stdout_data.decode(result.get('encoding', None))
            print(out)
            print('Узел доступен')
        else:
            print('Узел недоступен')


host_ping(['192.168.0.1', '192.168.0.2'])
