# Copyright (c) 2017 IBM Corp.
#
# All Rights Reserved.
#
#    Licensed under the Apache License, Version 2.0 (the "License"); you may
#    not use this file except in compliance with the License. You may obtain
#    a copy of the License at
#
#         http://www.apache.org/licenses/LICENSE-2.0
#
#    Unless required by applicable law or agreed to in writing, software
#    distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
#    WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
#    License for the specific language governing permissions and limitations
#    under the License.

import re

from os_dpm import constants as const


def is_valid_dpm_object_id(object_id):
    """Validates if the argument is a valid object-id

    Returns True if the argument has the format of a DPM object-id. It's not
    being checked whether the object-id exists on the HMC.

    :param object_id: potential object id to test
    :return: True if argument is a valid object-id, else False
    """
    match = re.search("^" + const.OBJECT_ID_REGEX + "$", object_id)
    if match:
        return True
    return False
