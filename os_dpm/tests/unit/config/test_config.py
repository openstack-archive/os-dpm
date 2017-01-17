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
from oslo_config.fixture import Config

from os_dpm.config import config
from os_dpm.tests import base


class TestNetworkingDpm(base.TestCase):

    def test_register_opts(self):
        conf = Config()
        conf.load_raw_values(group="dpm", hmc='host')
        conf.load_raw_values(group="dpm", hmc_username='username')
        conf.load_raw_values(group="dpm", hmc_password='password')
        conf.load_raw_values(group="dpm", cpc_uuid='uuid')

        config.register_opts()
        self.assertEqual('host', cfg.CONF.dpm.hmc)
        self.assertEqual('username', cfg.CONF.dpm.hmc_username)
        self.assertEqual('password', cfg.CONF.dpm.hmc_password)
        self.assertEqual('uuid', cfg.CONF.dpm.cpc_uuid)
