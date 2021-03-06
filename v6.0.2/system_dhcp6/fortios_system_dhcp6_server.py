#!/usr/bin/python
from __future__ import (absolute_import, division, print_function)
# Copyright 2018 Fortinet, Inc.
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.
#
# the lib use python logging can get it if the following is set in your
# Ansible config.

__metaclass__ = type

ANSIBLE_METADATA = {'status': ['preview'],
                    'supported_by': 'community',
                    'metadata_version': '1.1'}

DOCUMENTATION = '''
---
module: fortios_system_dhcp6_server
short_description: Configure DHCPv6 servers in Fortinet's FortiOS and FortiGate.
description:
    - This module is able to configure a FortiGate or FortiOS by
      allowing the user to configure system_dhcp6 feature and server category.
      Examples includes all options and need to be adjusted to datasources before usage.
      Tested with FOS v6.0.2
version_added: "2.8"
author:
    - Miguel Angel Munoz (@mamunozgonzalez)
    - Nicolas Thomas (@thomnico)
notes:
    - Requires fortiosapi library developed by Fortinet
    - Run as a local_action in your playbook
requirements:
    - fortiosapi>=0.9.8
options:
    host:
       description:
            - FortiOS or FortiGate ip adress.
       required: true
    username:
        description:
            - FortiOS or FortiGate username.
        required: true
    password:
        description:
            - FortiOS or FortiGate password.
        default: ""
    vdom:
        description:
            - Virtual domain, among those defined previously. A vdom is a
              virtual instance of the FortiGate that can be configured and
              used as a different unit.
        default: root
    https:
        description:
            - Indicates if the requests towards FortiGate must use HTTPS
              protocol
        type: bool
        default: false
    system_dhcp6_server:
        description:
            - Configure DHCPv6 servers.
        default: null
        suboptions:
            state:
                description:
                    - Indicates whether to create or remove the object
                choices:
                    - present
                    - absent
            dns-search-list:
                description:
                    - DNS search list options.
                choices:
                    - delegated
                    - specify
            dns-server1:
                description:
                    - DNS server 1.
            dns-server2:
                description:
                    - DNS server 2.
            dns-server3:
                description:
                    - DNS server 3.
            dns-service:
                description:
                    -  Options for assigning DNS servers to DHCPv6 clients.
                choices:
                    - delegated
                    - default
                    - specify
            domain:
                description:
                    - Domain name suffix for the IP addresses that the DHCP server assigns to clients.
            id:
                description:
                    - ID.
                required: true
            interface:
                description:
                    - DHCP server can assign IP configurations to clients connected to this interface. Source system.interface.name.
            ip-mode:
                description:
                    - Method used to assign client IP.
                choices:
                    - range
                    - delegated
            ip-range:
                description:
                    - DHCP IP range configuration.
                suboptions:
                    end-ip:
                        description:
                            - End of IP range.
                    id:
                        description:
                            - ID.
                        required: true
                    start-ip:
                        description:
                            - Start of IP range.
            lease-time:
                description:
                    - Lease time in seconds, 0 means unlimited.
            option1:
                description:
                    - Option 1.
            option2:
                description:
                    - Option 2.
            option3:
                description:
                    - Option 3.
            prefix-range:
                description:
                    - DHCP prefix configuration.
                suboptions:
                    end-prefix:
                        description:
                            - End of prefix range.
                    id:
                        description:
                            - ID.
                        required: true
                    prefix-length:
                        description:
                            - Prefix length.
                    start-prefix:
                        description:
                            - Start of prefix range.
            rapid-commit:
                description:
                    - Enable/disable allow/disallow rapid commit.
                choices:
                    - disable
                    - enable
            status:
                description:
                    - Enable/disable this DHCPv6 configuration.
                choices:
                    - disable
                    - enable
            subnet:
                description:
                    - Subnet or subnet-id if the IP mode is delegated.
            upstream-interface:
                description:
                    - Interface name from where delegated information is provided. Source system.interface.name.
'''

EXAMPLES = '''
- hosts: localhost
  vars:
   host: "192.168.122.40"
   username: "admin"
   password: ""
   vdom: "root"
  tasks:
  - name: Configure DHCPv6 servers.
    fortios_system_dhcp6_server:
      host:  "{{ host }}"
      username: "{{ username }}"
      password: "{{ password }}"
      vdom:  "{{ vdom }}"
      system_dhcp6_server:
        state: "present"
        dns-search-list: "delegated"
        dns-server1: "<your_own_value>"
        dns-server2: "<your_own_value>"
        dns-server3: "<your_own_value>"
        dns-service: "delegated"
        domain: "<your_own_value>"
        id:  "9"
        interface: "<your_own_value> (source system.interface.name)"
        ip-mode: "range"
        ip-range:
         -
            end-ip: "<your_own_value>"
            id:  "14"
            start-ip: "<your_own_value>"
        lease-time: "16"
        option1: "<your_own_value>"
        option2: "<your_own_value>"
        option3: "<your_own_value>"
        prefix-range:
         -
            end-prefix: "<your_own_value>"
            id:  "22"
            prefix-length: "23"
            start-prefix: "<your_own_value>"
        rapid-commit: "disable"
        status: "disable"
        subnet: "<your_own_value>"
        upstream-interface: "<your_own_value> (source system.interface.name)"
'''

RETURN = '''
build:
  description: Build number of the fortigate image
  returned: always
  type: string
  sample: '1547'
http_method:
  description: Last method used to provision the content into FortiGate
  returned: always
  type: string
  sample: 'PUT'
http_status:
  description: Last result given by FortiGate on last operation applied
  returned: always
  type: string
  sample: "200"
mkey:
  description: Master key (id) used in the last call to FortiGate
  returned: success
  type: string
  sample: "key1"
name:
  description: Name of the table used to fulfill the request
  returned: always
  type: string
  sample: "urlfilter"
path:
  description: Path of the table used to fulfill the request
  returned: always
  type: string
  sample: "webfilter"
revision:
  description: Internal revision number
  returned: always
  type: string
  sample: "17.0.2.10658"
serial:
  description: Serial number of the unit
  returned: always
  type: string
  sample: "FGVMEVYYQT3AB5352"
status:
  description: Indication of the operation's result
  returned: always
  type: string
  sample: "success"
vdom:
  description: Virtual domain used
  returned: always
  type: string
  sample: "root"
version:
  description: Version of the FortiGate
  returned: always
  type: string
  sample: "v5.6.3"

'''

from ansible.module_utils.basic import AnsibleModule

fos = None


def login(data):
    host = data['host']
    username = data['username']
    password = data['password']

    fos.debug('on')
    if 'https' in data and not data['https']:
        fos.https('off')
    else:
        fos.https('on')

    fos.login(host, username, password)


def filter_system_dhcp6_server_data(json):
    option_list = ['dns-search-list', 'dns-server1', 'dns-server2',
                   'dns-server3', 'dns-service', 'domain',
                   'id', 'interface', 'ip-mode',
                   'ip-range', 'lease-time', 'option1',
                   'option2', 'option3', 'prefix-range',
                   'rapid-commit', 'status', 'subnet',
                   'upstream-interface']
    dictionary = {}

    for attribute in option_list:
        if attribute in json and json[attribute] is not None:
            dictionary[attribute] = json[attribute]

    return dictionary


def system_dhcp6_server(data, fos):
    vdom = data['vdom']
    system_dhcp6_server_data = data['system_dhcp6_server']
    filtered_data = filter_system_dhcp6_server_data(system_dhcp6_server_data)
    if system_dhcp6_server_data['state'] == "present":
        return fos.set('system.dhcp6',
                       'server',
                       data=filtered_data,
                       vdom=vdom)

    elif system_dhcp6_server_data['state'] == "absent":
        return fos.delete('system.dhcp6',
                          'server',
                          mkey=filtered_data['id'],
                          vdom=vdom)


def fortios_system_dhcp6(data, fos):
    login(data)

    methodlist = ['system_dhcp6_server']
    for method in methodlist:
        if data[method]:
            resp = eval(method)(data, fos)
            break

    fos.logout()
    return not resp['status'] == "success", resp['status'] == "success", resp


def main():
    fields = {
        "host": {"required": True, "type": "str"},
        "username": {"required": True, "type": "str"},
        "password": {"required": False, "type": "str", "no_log": True},
        "vdom": {"required": False, "type": "str", "default": "root"},
        "https": {"required": False, "type": "bool", "default": "False"},
        "system_dhcp6_server": {
            "required": False, "type": "dict",
            "options": {
                "state": {"required": True, "type": "str",
                          "choices": ["present", "absent"]},
                "dns-search-list": {"required": False, "type": "str",
                                    "choices": ["delegated", "specify"]},
                "dns-server1": {"required": False, "type": "str"},
                "dns-server2": {"required": False, "type": "str"},
                "dns-server3": {"required": False, "type": "str"},
                "dns-service": {"required": False, "type": "str",
                                "choices": ["delegated", "default", "specify"]},
                "domain": {"required": False, "type": "str"},
                "id": {"required": True, "type": "int"},
                "interface": {"required": False, "type": "str"},
                "ip-mode": {"required": False, "type": "str",
                            "choices": ["range", "delegated"]},
                "ip-range": {"required": False, "type": "list",
                             "options": {
                                 "end-ip": {"required": False, "type": "str"},
                                 "id": {"required": True, "type": "int"},
                                 "start-ip": {"required": False, "type": "str"}
                             }},
                "lease-time": {"required": False, "type": "int"},
                "option1": {"required": False, "type": "str"},
                "option2": {"required": False, "type": "str"},
                "option3": {"required": False, "type": "str"},
                "prefix-range": {"required": False, "type": "list",
                                 "options": {
                                     "end-prefix": {"required": False, "type": "str"},
                                     "id": {"required": True, "type": "int"},
                                     "prefix-length": {"required": False, "type": "int"},
                                     "start-prefix": {"required": False, "type": "str"}
                                 }},
                "rapid-commit": {"required": False, "type": "str",
                                 "choices": ["disable", "enable"]},
                "status": {"required": False, "type": "str",
                           "choices": ["disable", "enable"]},
                "subnet": {"required": False, "type": "str"},
                "upstream-interface": {"required": False, "type": "str"}

            }
        }
    }

    module = AnsibleModule(argument_spec=fields,
                           supports_check_mode=False)
    try:
        from fortiosapi import FortiOSAPI
    except ImportError:
        module.fail_json(msg="fortiosapi module is required")

    global fos
    fos = FortiOSAPI()

    is_error, has_changed, result = fortios_system_dhcp6(module.params, fos)

    if not is_error:
        module.exit_json(changed=has_changed, meta=result)
    else:
        module.fail_json(msg="Error in repo", meta=result)


if __name__ == '__main__':
    main()
