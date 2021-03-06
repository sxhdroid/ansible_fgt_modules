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
module: fortios_switch_controller_vlan
short_description: Configure VLANs for switch controller in Fortinet's FortiOS and FortiGate.
description:
    - This module is able to configure a FortiGate or FortiOS by
      allowing the user to configure switch_controller feature and vlan category.
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
    switch_controller_vlan:
        description:
            - Configure VLANs for switch controller.
        default: null
        suboptions:
            state:
                description:
                    - Indicates whether to create or remove the object
                choices:
                    - present
                    - absent
            auth:
                description:
                    - Authentication.
                choices:
                    - radius
                    - usergroup
            color:
                description:
                    - Color of icon on the GUI.
            comments:
                description:
                    - Comment.
            name:
                description:
                    - Switch VLAN name.
                required: true
            portal-message-override-group:
                description:
                    - Specify captive portal replacement message override group.
            portal-message-overrides:
                description:
                    - Individual message overrides.
                suboptions:
                    auth-disclaimer-page:
                        description:
                            - Override auth-disclaimer-page message with message from portal-message-overrides group.
                    auth-login-failed-page:
                        description:
                            - Override auth-login-failed-page message with message from portal-message-overrides group.
                    auth-login-page:
                        description:
                            - Override auth-login-page message with message from portal-message-overrides group.
                    auth-reject-page:
                        description:
                            - Override auth-reject-page message with message from portal-message-overrides group.
            radius-server:
                description:
                    - Authentication radius server. Source user.radius.name.
            security:
                description:
                    - Security.
                choices:
                    - open
                    - captive-portal
                    - 8021x
            selected-usergroups:
                description:
                    - Selected user group.
                suboptions:
                    name:
                        description:
                            - User group name. Source user.group.name.
                        required: true
            usergroup:
                description:
                    - Authentication usergroup. Source user.group.name.
            vdom:
                description:
                    - Virtual domain,
            vlanid:
                description:
                    - VLAN ID.
'''

EXAMPLES = '''
- hosts: localhost
  vars:
   host: "192.168.122.40"
   username: "admin"
   password: ""
   vdom: "root"
  tasks:
  - name: Configure VLANs for switch controller.
    fortios_switch_controller_vlan:
      host:  "{{ host }}"
      username: "{{ username }}"
      password: "{{ password }}"
      vdom:  "{{ vdom }}"
      switch_controller_vlan:
        state: "present"
        auth: "radius"
        color: "4"
        comments: "<your_own_value>"
        name: "default_name_6"
        portal-message-override-group: "<your_own_value>"
        portal-message-overrides:
            auth-disclaimer-page: "<your_own_value>"
            auth-login-failed-page: "<your_own_value>"
            auth-login-page: "<your_own_value>"
            auth-reject-page: "<your_own_value>"
        radius-server: "<your_own_value> (source user.radius.name)"
        security: "open"
        selected-usergroups:
         -
            name: "default_name_16 (source user.group.name)"
        usergroup: "<your_own_value> (source user.group.name)"
        vdom: "<your_own_value>"
        vlanid: "19"
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


def filter_switch_controller_vlan_data(json):
    option_list = ['auth', 'color', 'comments',
                   'name', 'portal-message-override-group', 'portal-message-overrides',
                   'radius-server', 'security', 'selected-usergroups',
                   'usergroup', 'vdom', 'vlanid']
    dictionary = {}

    for attribute in option_list:
        if attribute in json and json[attribute] is not None:
            dictionary[attribute] = json[attribute]

    return dictionary


def switch_controller_vlan(data, fos):
    vdom = data['vdom']
    switch_controller_vlan_data = data['switch_controller_vlan']
    filtered_data = filter_switch_controller_vlan_data(switch_controller_vlan_data)
    if switch_controller_vlan_data['state'] == "present":
        return fos.set('switch-controller',
                       'vlan',
                       data=filtered_data,
                       vdom=vdom)

    elif switch_controller_vlan_data['state'] == "absent":
        return fos.delete('switch-controller',
                          'vlan',
                          mkey=filtered_data['name'],
                          vdom=vdom)


def fortios_switch_controller(data, fos):
    login(data)

    methodlist = ['switch_controller_vlan']
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
        "switch_controller_vlan": {
            "required": False, "type": "dict",
            "options": {
                "state": {"required": True, "type": "str",
                          "choices": ["present", "absent"]},
                "auth": {"required": False, "type": "str",
                         "choices": ["radius", "usergroup"]},
                "color": {"required": False, "type": "int"},
                "comments": {"required": False, "type": "str"},
                "name": {"required": True, "type": "str"},
                "portal-message-override-group": {"required": False, "type": "str"},
                "portal-message-overrides": {"required": False, "type": "dict",
                                             "options": {
                                                 "auth-disclaimer-page": {"required": False, "type": "str"},
                                                 "auth-login-failed-page": {"required": False, "type": "str"},
                                                 "auth-login-page": {"required": False, "type": "str"},
                                                 "auth-reject-page": {"required": False, "type": "str"}
                                             }},
                "radius-server": {"required": False, "type": "str"},
                "security": {"required": False, "type": "str",
                             "choices": ["open", "captive-portal", "8021x"]},
                "selected-usergroups": {"required": False, "type": "list",
                                        "options": {
                                            "name": {"required": True, "type": "str"}
                                        }},
                "usergroup": {"required": False, "type": "str"},
                "vdom": {"required": False, "type": "str"},
                "vlanid": {"required": False, "type": "int"}

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

    is_error, has_changed, result = fortios_switch_controller(module.params, fos)

    if not is_error:
        module.exit_json(changed=has_changed, meta=result)
    else:
        module.fail_json(msg="Error in repo", meta=result)


if __name__ == '__main__':
    main()
