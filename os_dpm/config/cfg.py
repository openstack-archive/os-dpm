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

from os_dpm.config.types import DPMObjectIdType


class DPMObjectIdOpt(cfg.Opt):
    def __init__(self, name, help=None):
        """Option with DPM Object-Id type

           Option with ``type`` :class:`DPMObjectIdType`

        :param name: the option's name
        :param help: an explanation of how the option is used
        """
        super(DPMObjectIdOpt, self).__init__(name, type=DPMObjectIdType(),
                                             help=help)
