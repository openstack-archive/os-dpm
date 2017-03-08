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

from os_dpm.config import cfg


class TestDPMObjectIdOpt(base.BaseTestCase):
    def test_object_id_opt(self):
        opt = cfg.DPMObjectIdOpt("foo-name", help="foo-help")
        self.assertEqual("foo-help", opt.help)
        self.assertEqual("foo-name", opt.name)
        self.assertEqual(cfg.DPMObjectIdType, type(opt.type))
