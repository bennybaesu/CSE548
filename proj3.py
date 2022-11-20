# BENJAMIN BAESU
# PROJECT 3
# CSE 548

import re
import subprocess

ovs_result = subprocess.check_output(['sh', 'test.sh'])

split_result = str(ovs_result).split('cookie')

port_table = {}

for result in split_result:
	src_macs = re.findall("dl_src=[\d:]+", str(result))
	src_ips = re.findall("nw_src=[\d\.]+", str(result))

	print('\nPRINTING RESULTS')
	print(src_macs)
	print(src_ips)

	if len(src_macs) > 0 and len(src_ips) > 0:
		print('PRINTING FINAL RESULTS')
		src_mac = src_macs[0].split('=')[1]
		src_ip = src_ips[0].split('=')[1]
		print (src_mac)
		print (src_ip)

		if src_mac in port_table and not port_table[src_mac] == src_ip:
			print('ALERT! WE FOUND A MAC ADDRESS WITH A DIFFERENT IP ADDRESS!')
	
			f = open('pox/l2firewall.config', 'r')
			index = 0
			for x in f:
				print(x)
				index += 1
			print(index)
			f.close()
			f = open('pox/l2firewall.config', 'a')
			f.write(str(index) + ',' + src_mac + ',00:00:00:00:00:02')
			break
		else:
			port_table[src_mac] = src_ip

		print('PORT TABLE:')
		print (port_table)
