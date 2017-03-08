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
from oslotest import base

from os_dpm.config import config
from os_dpm.config.types import DPMObjectIdType
from os_dpm.tests.unit.config.test_types import VALID_DPM_OBJECT_ID
from os_dpm.tests.unit.config.test_types import VALID_DPM_OBJECT_ID_UC


class TestConfig(base.BaseTestCase):

    def setUp(self):
        super(TestConfig, self).setUp()
        self.conf = Config()

    def test_register_opts(self):
        self.conf.load_raw_values(group="dpm", hmc='host')
        self.conf.load_raw_values(group="dpm", hmc_username='username')
        self.conf.load_raw_values(group="dpm", hmc_password='password')
        self.conf.load_raw_values(group="dpm",
                                  cpc_object_id=VALID_DPM_OBJECT_ID)

        config.register_opts()
        self.assertEqual('host', cfg.CONF.dpm.hmc)
        self.assertEqual('username', cfg.CONF.dpm.hmc_username)
        self.assertEqual('password', cfg.CONF.dpm.hmc_password)
        self.assertEqual(VALID_DPM_OBJECT_ID, cfg.CONF.dpm.cpc_object_id)

    def test_register_opts_cpc_object_id_upper_case(self):
        self.conf.load_raw_values(group="dpm",
                                  cpc_object_id=VALID_DPM_OBJECT_ID_UC)
        config.register_opts()
        self.assertEqual(VALID_DPM_OBJECT_ID, cfg.CONF.dpm.cpc_object_id)

    def test_invalid_opt(self):
        self.conf.load_raw_values(group="dpm", cpc_object_id="foo")
        config.register_opts()
        # self.assertRaises can only be used with method calls
        try:
            cfg.CONF.dpm.cpc_object_id
            self.fail()
        except ValueError:
            pass
