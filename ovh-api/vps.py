# -*- coding: utf-8 -*-

####################################################################################################

from OvhApi import Client, dump_json

####################################################################################################

client = Client()

services = client.get_vps()
for service in services:
    print 'VPS:', service
    dump_json(client.get_vps(service))
    dump_json(client.get_vps(service, 'datacenter'))
    dump_json(client.get_vps(service, 'ips'))
    dump_json(client.get_vps(service, 'serviceInfos'))
    # dump_json(client.get_vps(service, 'models'))

    # templates = client.get_vps(service, 'templates')
    # dump_json(client.get_vps(service, 'templates', templates[-1], 'software'))

    disk_id = client.get_vps(service, 'disks')[0]
    dump_json(client.get_vps(service, 'disks', disk_id))
    # dump_json(client.get_vps(service, 'disks', disk_id, 'monitoring', period='lastday', type='used'))
    dump_json(client.get_vps(service, 'use', type='mem:used'))
    # dump_json(client.get_vps(service, 'monitoring', period='lastday', type='mem:used'))

    # dump_json(client.post_vps(service, 'openConsoleAccess', protocol='VNC'))
    # vncviewer/krdc ['host'] # ['password'] ['port']
    # dump_json(client.post_vps(service, 'openConsoleAccess', protocol='VNCOverWebSocket'))

    # dump_json(client.get_vps(service, 'status'))

    # dump_json(client.post_vps(service, 'start'))
    # dump_json(client.post_vps(service, 'stop'))
    # dump_json(client.post_vps(service, 'reboot'))

####################################################################################################
# 
# End
# 
####################################################################################################
