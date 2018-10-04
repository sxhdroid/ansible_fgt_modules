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
module: fortios_endpoint_control_registered_forticlient
short_description: Registered FortiClient list.
description:
    - This module is able to configure a FortiGate or FortiOS by
      allowing the user to configure endpoint_control feature and registered_forticlient category.
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
    endpoint_control_registered_forticlient:
        description:
            - Registered FortiClient list.
        default: null
        suboptions:
            state:
                description:
                    - Indicates whether to create or remove the object
                choices:
                    - present
                    - absent
            flag:
                description:
                    - FortiClient registration flag.
            ip:
                description:
                    - Endpoint IP address.
            mac:
                description:
                    - Endpoint MAC address.
            reg-fortigate:
                description:
                    - Registering FortiGate SN.
            status:
                description:
                    - FortiClient registration status.
            uid:
                description:
                    - FortiClient UID.
                required: true
            vdom:
                description:
                    - Registering vdom.
'''

EXAMPLES = '''
- hosts: localhost
  vars:
   host: "192.168.122.40"
   username: "admin"
   password: ""
   vdom: "root"
  tasks:
  - name: Registered FortiClient list.
    fortios_endpoint_control_registered_forticlient:
      host:  "{{ host }}"
      username: "{{ username }}"
      password: "{{ password }}"
      vdom:  "{{ vdom }}"
      endpoint_control_registered_forticlient:
        state: "present"
        flag: "3"
        ip: "<your_own_value>"
        mac: "<your_own_value>"
        reg-fortigate: "<your_own_value>"
        status: "7"
        uid: "<your_own_value>"
        vdom: "<your_own_value>"
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


def filter_endpoint_control_registered_forticlient_data(json):
    option_list = ['flag', 'ip', 'mac',
                   'reg-fortigate', 'status', 'uid',
                   'vdom']
    dictionary = {}

    for attribute in option_list:
        if attribute in json:
            dictionary[attribute] = json[attribute]

    return dictionary


def endpoint_control_registered_forticlient(data, fos):
    vdom = data['vdom']
    endpoint_control_registered_forticlient_data = data['endpoint_control_registered_forticlient']
    filtered_data = filter_endpoint_control_registered_forticlient_data(
        endpoint_control_registered_forticlient_data)
    if endpoint_control_registered_forticlient_data['state'] == "present":
        return fos.set('endpoint-control',
                       'registered-forticlient',
                       data=filtered_data,
                       vdom=vdom)

    elif endpoint_control_registered_forticlient_data['state'] == "absent":
        return fos.delete('endpoint-control',
                          'registered-forticlient',
                          mkey=filtered_data['uid'],
                          vdom=vdom)


def fortios_endpoint_control(data, fos):
    login(data)

    methodlist = ['endpoint_control_registered_forticlient']
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
        "endpoint_control_registered_forticlient": {
            "required": False, "type": "dict",
            "options": {
                "state": {"required": True, "type": "str",
                          "choices": ["present", "absent"]},
                "flag": {"required": False, "type": "int"},
                "ip": {"required": False, "type": "str"},
                "mac": {"required": False, "type": "str"},
                "reg-fortigate": {"required": False, "type": "str"},
                "status": {"required": False, "type": "int"},
                "uid": {"required": True, "type": "str"},
                "vdom": {"required": False, "type": "str"}

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

    is_error, has_changed, result = fortios_endpoint_control(
        module.params, fos)

    if not is_error:
        module.exit_json(changed=has_changed, meta=result)
    else:
        module.fail_json(msg="Error in repo", meta=result)


if __name__ == '__main__':
    main()