#!/usr/bin/python
# -*- coding: utf-8 -*-
# Copyright 2023 Dell Inc. or its subsidiaries. All Rights Reserved
# GNU General Public License v3.0+
# (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)

#############################################
#                WARNING                    #
#############################################
#
# This file is auto generated by the resource
#   module builder playbook.
#
# Do not edit this file manually.
#
# Changes to this file will be over written
#   by the resource module builder.
#
# Changes should be made in the model used to
#   generate this file or in the resource module
#   builder template.
#
#############################################

"""
The module file for sonic_vlan_mapping
"""

from __future__ import absolute_import, division, print_function
__metaclass__ = type

ANSIBLE_METADATA = {
    'metadata_version': '1.1',
    'status': ['preview'],
    'supported_by': 'community',
    'license': 'Apache 2.0'
}

DOCUMENTATION = """
---
module: sonic_vlan_mapping
author: "Cypher Miller (@Cypher-Miller)"
version_added: "2.1.0"
short_description: Configure vlan mappings on SONiC.
description:
  - This module provides configuration management for vlan mappings on devices running SONiC.
  - Vlan mappings only available on TD3 and TD4 devices.
  - For TD4 devices must enable vlan mapping first (can enable in config-switch-resource).
options:
  config:
    description:
      - Specifies the vlan mapping related configurations.
    type: list
    elements: dict
    suboptions:
      name:
        description:
          - Full name of the interface, i.e. Ethernet8, PortChannel2, Eth1/2.
        required: true
        type: str
      mapping:
        description:
          - Defining a single vlan mapping.
        type: list
        elements: dict
        suboptions:
          service_vlan:
            description:
              - Configure service provider VLAN ID.
              - VLAN ID range is 1-4094.
            required: true
            type: int
          vlan_ids:
            description:
              - Configure customer VLAN IDs.
              - If mode is double tagged translation then this VLAN ID represents the outer VLAN ID.
              - If mode is set to stacking can pass ranges and/or multiple list entries.
              - Individual VLAN ID or (-) separated range of VLAN IDs.
            type: list
            elements: str
          dot1q_tunnel:
            description:
              - Specify whether it is a vlan stacking or translation (false means translation; true means stacking).
            type: bool
            default: false
          inner_vlan:
            description:
              - Configure inner customer VLAN ID.
              - VLAN IDs range is 1-4094.
              - Only available for double tagged translations.
            type: int
          priority:
            description:
              - Set priority level of the vlan mapping.
              - Priority range is 0-7.
            type: int
  state:
    description:
      - Specifies the operation to be performed on the vlan mappings configured on the device.
      - In case of merged, the input configuration will be merged with the existing vlan mappings on the device.
      - In case of deleted, the existing vlan mapping configuration will be removed from the device.
      - In case of overridden, all existing vlan mappings will be deleted and the specified input configuration will be add.
      - In case of replaced, the existing vlan mappings on the device will be replaced by the configuration for each vlan mapping.
    type: str
    default: merged
    choices:
      - merged
      - deleted
      - replaced
      - overridden
"""
EXAMPLES = """
# Using deleted
#
# Before State:
# -------------
#
#sonic# show running-configuration interface
#!
#interface Ethernet8
# mtu 9100
# speed 400000
# fec RS
# unreliable-los auto
# shutdown
# switchport vlan-mapping 623 2411
# switchport vlan-mapping 392 inner 590 2755
#!
#interface Ethernet16
# mtu 9100
# speed 400000
# fec RS
# unreliable-los auto
# shutdown
# switchport vlan-mapping 400-402,404,406,408,410,412,420,422,430-432 dot1q-tunnel 2436 priority 3
# switchport vlan-mapping 300 dot1q-tunnel 2567 priority 3
#!


  - name: Delete vlan mapping configurations
    sonic_vlan_mapping:
      config:
        - name: Ethernet8
          mapping:
            - service_vlan: 2755
        - name: Ethernet16
          mapping:
            - service_vlan: 2567
              priority: 3
            - service_vlan: 2436
              vlan_ids:
                - 404
                - 401
                - 412
                - 430-431
              priority: 3
      state: deleted

# After State:
# ------------
#
#sonic# show running-configuration interface
#!
#interface Ethernet8
# mtu 9100
# speed 400000
# fec RS
# unreliable-los auto
# shutdown
# switchport vlan-mapping 623 2411
#!
#interface Ethernet16
# mtu 9100
# speed 400000
# fec RS
# unreliable-los auto
# shutdown
# switchport vlan-mapping 400,402,406,408,410,420,422,432 dot1q-tunnel 2436
# switchport vlan-mapping 300 dot1q-tunnel 2567
#!


# Using deleted
#
# Before State:
# -------------
#
#sonic# show running-configuration interface
#!
#interface Ethernet8
# mtu 9100
# speed 400000
# fec RS
# unreliable-los auto
# shutdown
# switchport vlan-mapping 623 2411
# switchport vlan-mapping 392 inner 590 2755
#!
#interface Ethernet16
# mtu 9100
# speed 400000
# fec RS
# unreliable-los auto
# shutdown
# switchport vlan-mapping 400-402,404,406,408,410,412,420,422,430-431 dot1q-tunnel 2436
# switchport vlan-mapping 300 dot1q-tunnel 2567 priority 3
#!


  - name: Delete vlan mapping configurations
    sonic_vlan_mapping:
      config:
        - name: Ethernet8
        - name: Ethernet16
          mapping:
            - service_vlan: 2567
      state: deleted

# After State:
# ------------
#
#sonic# show running-configuration interface
#!
#interface Ethernet8
# mtu 9100
# speed 400000
# fec RS
# unreliable-los auto
# shutdo#!
#interface Ethernet16
# mtu 9100
# speed 400000
# fec RS
# unreliable-los auto
# shutdown
# switchport vlan-mapping 400-402,406,408,410,420,422,431 dot1q-tunnel 2436
#!


# Using merged
#
# Before State:
# -------------
#
#sonic# show running-configuration interface
#!
#interface Ethernet8
# mtu 9100
# speed 400000
# fec RS
# unreliable-los auto
# shutdown
# switchport vlan-mapping 623 2411
#!
#interface Ethernet16
# mtu 9100
# speed 400000
# fec RS
# unreliable-los auto
# shutdown
#!
#interface PortChannel 2
# switchport vlan-mapping 345 2999 priority 0
# switchport vlan-mapping 500,540 dot1q-tunnel 3000
# no shutdown
#!

  - name: Add vlan mapping configurations
    sonic_vlan_mapping:
      config:
        - name: Ethernet8
          mapping:
            - service_vlan: 2755
              vlan_ids:
                - 392
              dot1q_tunnel: false
              inner_vlan: 590
        - name: Ethernet16
          mapping:
            - service_vlan: 2567
              vlan_ids:
                - 300
              dot1q_tunnel: true
              priority: 3
            - service_vlan: 2436
              vlan_ids:
                - 400-402
                - 404
                - 406
                - 408
                - 410
                - 412
                - 420
                - 422
                - 430-431
              dot1q_tunnel: true
        - name: Portchannel 2
          mapping:
            - service_vlan: 2999
              priority: 4
            - service_vlan: 3000
              vlan_ids:
                - 506-512
                - 561
              priority: 5
      state: merged

# After State:
# ------------
#
#sonic# show running-configuration interface
#!
#interface Ethernet8
# mtu 9100
# speed 400000
# fec RS
# unreliable-los auto
# shutdown
# switchport vlan-mapping 623 2411
# switchport vlan-mapping 392 inner 590 2755
#!
#interface Ethernet16
# mtu 9100
# speed 400000
# fec RS
# unreliable-los auto
# shutdown
# switchport vlan-mapping 400-402,404,406,408,410,412,420,422,430-431 dot1q-tunnel 2436
# switchport vlan-mapping 300 dot1q-tunnel 2567 priority 3
#!
#interface PortChannel 2
# switchport vlan-mapping 345 2999 priority 4
# switchport vlan-mapping 500,506-512,540,561 dot1q-tunnel 3000 priority 5
# no shutdown
#!


# Using replaced
#
# Before State:
# -------------
#
#sonic# show running-configuration interface
#!
#interface Ethernet8
# mtu 9100
# speed 400000
# fec RS
# unreliable-los auto
# shutdown
# switchport vlan-mapping 623 2411
# switchport vlan-mapping 392 inner 590 2755
#!
#interface Ethernet16
# mtu 9100
# speed 400000
# fec RS
# unreliable-los auto
# shutdown
# switchport vlan-mapping 400-402,404,406,408,410,412,420,422,430-431 dot1q-tunnel 2436
# switchport vlan-mapping 300 dot1q-tunnel 2567 priority 3
#!
#interface PortChannel 2
# switchport vlan-mapping 345 2999 priority 0
# no shutdown
#!

  - name: Replace vlan mapping configurations
    sonic_vlan_mapping:
      config:
        - name: Ethernet8
          mapping:
            - service_vlan: 2755
              vlan_ids:
                - 390
              dot1q_tunnel: false
              inner_vlan: 593
        - name: Ethernet16
          mapping:
            - service_vlan: 2567
              vlan_ids:
                - 310
                - 330-340
              priority: 5
        - name: Portchannel 2
          mapping:
            - service_vlan: 2999
              vlan_ids:
                - 345
              dot1q_tunnel: true
              priority: 1
      state: replaced


# After State:
# ------------
#
#sonic# show running-configuration interface
#!
#interface Ethernet8
# mtu 9100
# speed 400000
# fec RS
# unreliable-los auto
# shutdown
# switchport vlan-mapping 623 2411
# switchport vlan-mapping 390 inner 593 2755
#!
#interface Ethernet16
# mtu 9100
# speed 400000
# fec RS
# unreliable-los auto
# shutdown
# switchport vlan-mapping 400-402,404,406,408,410,412,420,422,430-431 dot1q-tunnel 2436
# switchport vlan-mapping 310,330-340 dot1q-tunnel 2567 priority 5
#!
#interface PortChannel 2
# switchport vlan-mapping 345 dot1q_tunnel 2999 priority 1
# no shutdown
#!


# Using overridden
#
# Before State:
# -------------
#
#sonic# show running-configuration interface
#!
#interface Ethernet8
# mtu 9100
# speed 400000
# fec RS
# unreliable-los auto
# shutdown
# switchport vlan-mapping 623 2411
#!
#interface Ethernet16
# mtu 9100
# speed 400000
# fec RS
# unreliable-los auto
# shutdown
# switchport vlan-mapping 400-402,404,406,408,410,412,420,422,430-431 dot1q-tunnel 2436
#!

  - name: Overwrite the vlan mapping configurations
    sonic_vlan_mapping:
      config:
        - name: Ethernet8
          mapping:
            - service_vlan: 2755
              vlan_ids:
                - 392
              dot1q_tunnel: false
              inner_vlan: 590
        - name: Ethernet16
          mapping:
            - service_vlan: 2567
              vlan_ids:
                - 300
              dot1q_tunnel: true
              priority: 3
        - name: Portchannel 2
          mapping:
            - service_vlan: 2999
              vlan_ids:
                - 345
              priority: 0
      state: overridden

# After State:
# ------------
#
#sonic# show running-configuration interface
#!
#interface Ethernet8
# mtu 9100
# speed 400000
# fec RS
# unreliable-los auto
# shutdown
# switchport vlan-mapping 392 inner 590 2755
#!
#interface Ethernet16
# mtu 9100
# speed 400000
# fec RS
# unreliable-los auto
# shutdown
# switchport vlan-mapping 300 dot1q-tunnel 2567 priority 3
#!
#interface PortChannel 2
# switchport vlan-mapping 345 2999 priority 0
# no shutdown
#!


"""
RETURN = """
before:
  description: The configuration prior to the model invocation.
  returned: always
  type: list
  sample: >
    The configuration returned will always be in the same format
     of the parameters above.
after:
  description: The resulting configuration model invocation.
  returned: when changed
  type: list
  sample: >
    The configuration returned will always be in the same format
     of the parameters above.
commands:
  description: The set of commands pushed to the remote device.
  returned: always
  type: list
  sample: ['command 1', 'command 2', 'command 3']
"""


from ansible.module_utils.basic import AnsibleModule
from ansible_collections.dellemc.enterprise_sonic.plugins.module_utils.network.sonic.argspec.vlan_mapping.vlan_mapping import Vlan_mappingArgs
from ansible_collections.dellemc.enterprise_sonic.plugins.module_utils.network.sonic.config.vlan_mapping.vlan_mapping import Vlan_mapping


def main():
    """
    Main entry point for module execution

    :returns: the result form module invocation
    """
    module = AnsibleModule(argument_spec=Vlan_mappingArgs.argument_spec,
                           supports_check_mode=True)

    result = Vlan_mapping(module).execute_module()
    module.exit_json(**result)


if __name__ == '__main__':
    main()
