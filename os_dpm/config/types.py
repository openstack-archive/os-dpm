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

from os_dpm import constants as const


class DPMObjectIdType(cfg.types.String):
    def __init__(self):
        """DPM Object-Id Type.

        DPM Object-Id values are returned as lower case str objects.
        If the configuration value is provided as upper case, this type
        converts it to lower case.
        """

        super(DPMObjectIdType, self).__init__(
            type_name='DPM Object-Id value', ignore_case=True, max_length=36,
            regex="^" + const.OBJECT_ID_REGEX + "$")

    def __call__(self, value):
        val = super(DPMObjectIdType, self).__call__(value)
        return val.lower()
