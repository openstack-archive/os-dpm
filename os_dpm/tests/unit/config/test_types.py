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

VALID_DPM_OBJECT_ID = "fa1f2466-12df-311a-804c-4ed2cc1d656b"
VALID_DPM_OBJECT_ID_UC = "FA1F2466-12DF-311A-804C-4ED2CC1D656B"


class TestDPMObjectIdType(base.BaseTestCase):
    conf_type = types.DPMObjectIdType()

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
        t = types.DPMObjectIdType()
        self.assertEqual(
            "String(regex='^[a-f0-9]{8}-([a-f0-9]{4}-){3}[a-f0-9]{12}$')",
            repr(t))


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
