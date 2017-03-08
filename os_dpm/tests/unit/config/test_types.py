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

from os_dpm.config import types


class TestMultiMappingType(base.BaseTestCase):

    def setUp(self):
        super(TestMultiMappingType, self).setUp()
        self.mm_type = types.MultiStringWithKwargsType()

    def test_format_default_none(self):
        result = self.mm_type.format_defaults(None)
        self.assertEqual([''], result)

    def test_format_defaults_default_only(self):
        result = self.mm_type.format_defaults(['foo', 'bar'])
        self.assertEqual(['foo', 'bar'], result)

    def test_format_defaults_sample_default_over_default(self):
        result = self.mm_type.format_defaults(['foo', 'bar'], ['sample'])
        self.assertEqual(['sample'], result)

    def test_quote_trailing_and_leading_space_default(self):
        result = self.mm_type.format_defaults([' foo ', ' bar '])
        self.assertEqual(['" foo "', '" bar "'], result)

    def test_quote_trailing_and_leading_space_sample_default(self):
        result = self.mm_type.format_defaults([' foo ', ' bar '], [' sample '])
        self.assertEqual(['" sample "'], result)
