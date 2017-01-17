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


DPM_GROUP = cfg.OptGroup('dpm',
                         title='DPM options',
                         help="""
Configurations for the IBM z Systems and Linux One hypervisor (PR/SM) in
DPM (Dynamic Partition Manager) mode. The hypervisor is managed by the
ReST APIs hosted on the HMC (Hardware Management Console of the system.
""")


COMMON_DPM_OPTS = [
    cfg.StrOpt('hmc', help="""
    Hostname or IP address for connection to HMC via zhmcclient"""),
    cfg.StrOpt('hmc_username', help="""
    User name for connection to HMC Host."""),
    cfg.StrOpt('hmc_password', help="""
    Password for connection to HMC Host."""),
    cfg.StrOpt('cpc_uuid', help="""
    Uuid of the CPC"""),
]


def register_opts():
    cfg.CONF.register_group(DPM_GROUP)
    cfg.CONF.register_opts(COMMON_DPM_OPTS, group=DPM_GROUP)
