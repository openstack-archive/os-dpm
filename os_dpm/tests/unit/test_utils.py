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

from oslotest import base

from os_dpm.tests.unit.config.test_config import VALID_DPM_OBJECT_ID
from os_dpm.tests.unit.config.test_config import VALID_DPM_OBJECT_ID_UC
from os_dpm import utils


class TestUtils(base.BaseTestCase):
    def test_is_valid_object_id(self):
        self.assertTrue(utils.is_valid_dpm_object_id(VALID_DPM_OBJECT_ID))

    def test_is_valid_object_id_invalid(self):
        invalid = ["foo",
                   # Missing -
                   "fa1f246612df311a804c4ed2cc1d6564",
                   # Invalid character 'g'
                   "ga1f2466-12df-311a-804c-4ed2cc1d6564",
                   # Too long
                   "fa1f2466-12df-311a-804c-4ed2cc1d65641",
                   # Upper case is not considered as valid by the HMC
                   VALID_DPM_OBJECT_ID_UC]
        for oid in invalid:
            self.assertFalse(utils.is_valid_dpm_object_id(oid))
