# Copyright 2017 IBM Corp. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from oslo_config import cfg

from os_dpm.config.cfg import DPMObjectIdOpt

DPM_GROUP = cfg.OptGroup('dpm',
                         title='DPM options',
                         help="""
Configuration options for IBM z Systems and IBM LinuxONE in DPM (Dynamic
Partition Manager) administrative mode. A z Systems or LinuxONE machine is
termed "CPC" (Central Processor Complex). The CPCs are managed via the Web
Services API exposed by the "HMC" (Hardware Management Console). One HMC can
manage multiple CPCs.
""")


COMMON_DPM_OPTS = [
    cfg.StrOpt('hmc', help="""
    Hostname or IP address of the HMC that manages the target CPC"""),
    cfg.StrOpt('hmc_username', help="""
    User name for connection to the HMC"""),
    cfg.StrOpt('hmc_password', secret=True, help="""
    Password for connection to the HMC"""),
    DPMObjectIdOpt('cpc_object_id', help="""
    DPM Object-id of the target CPC"""),
]


def register_opts():
    cfg.CONF.register_group(DPM_GROUP)
    cfg.CONF.register_opts(COMMON_DPM_OPTS, group=DPM_GROUP)
