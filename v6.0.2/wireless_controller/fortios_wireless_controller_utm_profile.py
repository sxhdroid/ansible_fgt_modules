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
module: fortios_wireless_controller_utm_profile
short_description: Configure UTM (Unified Threat Management) profile in Fortinet's FortiOS and FortiGate.
description:
    - This module is able to configure a FortiGate or FortiOS by
      allowing the user to configure wireless_controller feature and utm_profile category.
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
    wireless_controller_utm_profile:
        description:
            - Configure UTM (Unified Threat Management) profile.
        default: null
        suboptions:
            state:
                description:
                    - Indicates whether to create or remove the object
                choices:
                    - present
                    - absent
            antivirus-profile:
                description:
                    - AntiVirus profile name. Source antivirus.profile.name.
            application-list:
                description:
                    - Application control list name. Source application.list.name.
            comment:
                description:
                    - Comment.
            ips-sensor:
                description:
                    - IPS sensor name. Source ips.sensor.name.
            name:
                description:
                    - UTM profile name.
                required: true
            scan-botnet-connections:
                description:
                    - Block or monitor connections to Botnet servers or disable Botnet scanning.
                choices:
                    - disable
                    - block
                    - monitor
            utm-log:
                description:
                    - Enable/disable UTM logging.
                choices:
                    - enable
                    - disable
            webfilter-profile:
                description:
                    - WebFilter profile name. Source webfilter.profile.name.
'''

EXAMPLES = '''
- hosts: localhost
  vars:
   host: "192.168.122.40"
   username: "admin"
   password: ""
   vdom: "root"
  tasks:
  - name: Configure UTM (Unified Threat Management) profile.
    fortios_wireless_controller_utm_profile:
      host:  "{{ host }}"
      username: "{{ username }}"
      password: "{{ password }}"
      vdom:  "{{ vdom }}"
      wireless_controller_utm_profile:
        state: "present"
        antivirus-profile: "<your_own_value> (source antivirus.profile.name)"
        application-list: "<your_own_value> (source application.list.name)"
        comment: "Comment."
        ips-sensor: "<your_own_value> (source ips.sensor.name)"
        name: "default_name_7"
        scan-botnet-connections: "disable"
        utm-log: "enable"
        webfilter-profile: "<your_own_value> (source webfilter.profile.name)"
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


def filter_wireless_controller_utm_profile_data(json):
    option_list = ['antivirus-profile', 'application-list', 'comment',
                   'ips-sensor', 'name', 'scan-botnet-connections',
                   'utm-log', 'webfilter-profile']
    dictionary = {}

    for attribute in option_list:
        if attribute in json and json[attribute] is not None:
            dictionary[attribute] = json[attribute]

    return dictionary


def wireless_controller_utm_profile(data, fos):
    vdom = data['vdom']
    wireless_controller_utm_profile_data = data['wireless_controller_utm_profile']
    filtered_data = filter_wireless_controller_utm_profile_data(wireless_controller_utm_profile_data)
    if wireless_controller_utm_profile_data['state'] == "present":
        return fos.set('wireless-controller',
                       'utm-profile',
                       data=filtered_data,
                       vdom=vdom)

    elif wireless_controller_utm_profile_data['state'] == "absent":
        return fos.delete('wireless-controller',
                          'utm-profile',
                          mkey=filtered_data['name'],
                          vdom=vdom)


def fortios_wireless_controller(data, fos):
    login(data)

    methodlist = ['wireless_controller_utm_profile']
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
        "wireless_controller_utm_profile": {
            "required": False, "type": "dict",
            "options": {
                "state": {"required": True, "type": "str",
                          "choices": ["present", "absent"]},
                "antivirus-profile": {"required": False, "type": "str"},
                "application-list": {"required": False, "type": "str"},
                "comment": {"required": False, "type": "str"},
                "ips-sensor": {"required": False, "type": "str"},
                "name": {"required": True, "type": "str"},
                "scan-botnet-connections": {"required": False, "type": "str",
                                            "choices": ["disable", "block", "monitor"]},
                "utm-log": {"required": False, "type": "str",
                            "choices": ["enable", "disable"]},
                "webfilter-profile": {"required": False, "type": "str"}

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

    is_error, has_changed, result = fortios_wireless_controller(module.params, fos)

    if not is_error:
        module.exit_json(changed=has_changed, meta=result)
    else:
        module.fail_json(msg="Error in repo", meta=result)


if __name__ == '__main__':
    main()
