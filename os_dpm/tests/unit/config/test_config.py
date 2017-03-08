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

VALID_DPM_OBJECT_ID = "fa1f2466-12df-311a-804c-4ed2cc1d656b"
VALID_DPM_OBJECT_ID_UC = "FA1F2466-12DF-311A-804C-4ED2CC1D656B"


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


class TestDPMObjectIdOpt(base.BaseTestCase):
    def test_object_id_opt(self):
        opt = config.DPMObjectIdOpt("foo-name", help="foo-help")
        self.assertEqual("foo-help", opt.help)
        self.assertEqual("foo-name", opt.name)
        self.assertEqual(config.DPMObjectIdType, type(opt.type))


class TestDPMObjectIdType(base.BaseTestCase):
    conf_type = config.DPMObjectIdType()

    def test_empty_value_fail(self):
        self.assertRaises(ValueError, self.conf_type, '')

    def test_invalid_value_fail(self):
        self.assertRaises(ValueError, self.conf_type, 'foobar')

    def test_valid_object_id(self):
        self.assertEqual(VALID_DPM_OBJECT_ID,
                         self.conf_type(VALID_DPM_OBJECT_ID))

    def test_valid_object_id_ignore_case(self):
        self.assertEqual(VALID_DPM_OBJECT_ID,
                         self.conf_type(VALID_DPM_OBJECT_ID_UC))

    def test_object_id_too_long(self):
        self.assertRaises(ValueError, self.conf_type,
                          VALID_DPM_OBJECT_ID + "1")

    def test_repr(self):
        t = config.DPMObjectIdType()
        self.assertEqual(
            "String(regex='^[a-f0-9]{8}-([a-f0-9]{4}-){3}[a-f0-9]{12}$')",
            repr(t))

    def test_equal(self):
        self.assertTrue(config.DPMObjectIdType() == config.DPMObjectIdType())
