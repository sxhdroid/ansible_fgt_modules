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
module: fortios_system_email_server
short_description: Configure the email server used by the FortiGate various things. For example, for sending email messages to users to support user
   authentication features in Fortinet's FortiOS and FortiGate.
description:
    - This module is able to configure a FortiGate or FortiOS by
      allowing the user to configure system feature and email_server category.
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
    system_email_server:
        description:
            - Configure the email server used by the FortiGate various things. For example, for sending email messages to users to support user authentication
               features.
        default: null
        suboptions:
            authenticate:
                description:
                    - Enable/disable authentication.
                choices:
                    - enable
                    - disable
            password:
                description:
                    - SMTP server user password for authentication.
            port:
                description:
                    - SMTP server port.
            reply-to:
                description:
                    - Reply-To email address.
            security:
                description:
                    - Connection security used by the email server.
                choices:
                    - none
                    - starttls
                    - smtps
            server:
                description:
                    - SMTP server IP address or hostname.
            source-ip:
                description:
                    - SMTP server IPv4 source IP.
            source-ip6:
                description:
                    - SMTP server IPv6 source IP.
            ssl-min-proto-version:
                description:
                    - Minimum supported protocol version for SSL/TLS connections (default is to follow system global setting).
                choices:
                    - default
                    - SSLv3
                    - TLSv1
                    - TLSv1-1
                    - TLSv1-2
            type:
                description:
                    - Use FortiGuard Message service or custom email server.
                choices:
                    - custom
            username:
                description:
                    - SMTP server user name for authentication.
            validate-server:
                description:
                    - Enable/disable validation of server certificate.
                choices:
                    - enable
                    - disable
'''

EXAMPLES = '''
- hosts: localhost
  vars:
   host: "192.168.122.40"
   username: "admin"
   password: ""
   vdom: "root"
  tasks:
  - name: Configure the email server used by the FortiGate various things. For example, for sending email messages to users to support user authentication
     features.
    fortios_system_email_server:
      host:  "{{ host }}"
      username: "{{ username }}"
      password: "{{ password }}"
      vdom:  "{{ vdom }}"
      system_email_server:
        authenticate: "enable"
        password: "<your_own_value>"
        port: "5"
        reply-to: "<your_own_value>"
        security: "none"
        server: "192.168.100.40"
        source-ip: "84.230.14.43"
        source-ip6: "<your_own_value>"
        ssl-min-proto-version: "default"
        type: "custom"
        username: "<your_own_value>"
        validate-server: "enable"
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


def filter_system_email_server_data(json):
    option_list = ['authenticate', 'password', 'port',
                   'reply-to', 'security', 'server',
                   'source-ip', 'source-ip6', 'ssl-min-proto-version',
                   'type', 'username', 'validate-server']
    dictionary = {}

    for attribute in option_list:
        if attribute in json and json[attribute] is not None:
            dictionary[attribute] = json[attribute]

    return dictionary


def system_email_server(data, fos):
    vdom = data['vdom']
    system_email_server_data = data['system_email_server']
    filtered_data = filter_system_email_server_data(system_email_server_data)
    return fos.set('system',
                   'email-server',
                   data=filtered_data,
                   vdom=vdom)


def fortios_system(data, fos):
    login(data)

    methodlist = ['system_email_server']
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
        "system_email_server": {
            "required": False, "type": "dict",
            "options": {
                "authenticate": {"required": False, "type": "str",
                                 "choices": ["enable", "disable"]},
                "password": {"required": False, "type": "str"},
                "port": {"required": False, "type": "int"},
                "reply-to": {"required": False, "type": "str"},
                "security": {"required": False, "type": "str",
                             "choices": ["none", "starttls", "smtps"]},
                "server": {"required": False, "type": "str"},
                "source-ip": {"required": False, "type": "str"},
                "source-ip6": {"required": False, "type": "str"},
                "ssl-min-proto-version": {"required": False, "type": "str",
                                          "choices": ["default", "SSLv3", "TLSv1",
                                                      "TLSv1-1", "TLSv1-2"]},
                "type": {"required": False, "type": "str",
                         "choices": ["custom"]},
                "username": {"required": False, "type": "str"},
                "validate-server": {"required": False, "type": "str",
                                    "choices": ["enable", "disable"]}

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

    is_error, has_changed, result = fortios_system(module.params, fos)

    if not is_error:
        module.exit_json(changed=has_changed, meta=result)
    else:
        module.fail_json(msg="Error in repo", meta=result)


if __name__ == '__main__':
    main()
