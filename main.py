import subprocess
import os
import time
import socket
import struct


class ping_loop():

    def __init__(self):
        pass

    def number_ip(
            self, iprange1, iprange2):

        # split the number in ip address
        ip_range1 = iprange1.split(".")
        ip_range2 = iprange2.split(".")
        list_numb = []

        # detect ip change in range
        for i in range(0, 4):
            if ip_range1[
                    i] == ip_range2[i]:
                iprange = None
            if ip_range1[
                    i] < ip_range2[i]:
                iprange = int(
                    ip_range2[i]) - int(ip_range1[i])
            if ip_range1[
                    i] > ip_range2[i]:
                iprange = int(
                    ip_range1[i]) - int(ip_range2[i])

            # if ip is determine
            if iprange is not None:
                if i == 0:
                    # xxx.000.000.000
                    # range (^32)
                    iprange0 = iprange * 254 * 254 * 254
                    iprange0 += int(iprange0)
                    list_numb.append(
                        iprange0)

                if i == 1:
                    # xxx.xxx.000.000
                    # range (^24)
                    iprange1 = iprange * 254 * 254
                    iprange1 += int(iprange1)
                    list_numb.append(
                        iprange1)

                if i == 2:
                    # xxx.xxx.xxx.000
                    # range (^16)
                    iprange2 = iprange * 254
                    iprange2 += int(iprange2)
                    list_numb.append(
                        iprange2)

                if i == 3:
                    # xxx.xxx.xxx.xxx
                    # range (^8)
                    iprange3 = int(
                        iprange)
                    list_numb.append(
                        iprange3)

        Total = sum(list_numb)
        print(
            " {:,}{}".format(
                Total,
                " Total ip in range"))
        return int(Total)

    def ips(self, start, end):
        start = struct.unpack(
            '>I', socket.inet_aton(start))[0]
        end = struct.unpack(
            '>I', socket.inet_aton(end))[0]
        return [socket.inet_ntoa(struct.pack(
            '>I', i)) for i in range(start, end)]

    def ping(self, ip_start, ip_stop):

        print(
            " start {0}".format(ip_start))
        print(
            " end {0}".format(ip_stop))

        list_ip = self.ips(
            ip_start, ip_stop)
        print(
            "------------------------")
        for ip in list_ip:
            proc = subprocess.Popen(
                ['ping', '-c', '1', '-w', '1', ip], stdout=subprocess.PIPE)
            stdout, stderr = proc.communicate()
            if proc.returncode == 0:
                print(
                    '{} is UP'.format(ip))
                #print('ping output:')
                # print(stdout.decode('ASCII'))
            else:
                print(
                    '{} is DOWN'.format(ip))
                #print('ping output:')
                # print(stdout.decode('ASCII'))

        return True

ip_calc = ping_loop()
ip_calc.number_ip(
    "192.168.0.1",
    "192.168.0.255")
ip_calc.ping(
    "192.168.0.1",
    "192.168.0.255")
