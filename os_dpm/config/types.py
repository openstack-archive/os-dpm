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


class MultiStringWithKwargsType(cfg.types.String):
    """Multi String with kwargs type

    This type is basically the same as the oslo_config.types.MultiString type.
    The only difference is that this type allows setting additional attributes
    via **kwargs for the super String type, which the MultiString type does
    not.

    Once **kwargs are allowed in oslo_config.types.MultiString type, this
    type can be eliminated.
    """
    def __init__(self, type_name='multi valued', **kwargs):
        super(MultiStringWithKwargsType, self).__init__(
            type_name=type_name, **kwargs)

    NONE_DEFAULT = ['']

    def format_defaults(self, default, sample_default=None):
        """Return a list of formatted default values.

        Called when generating the description of a config option in the
        config file.
        """
        if sample_default is not None:
            default_list = self._formatter(sample_default)
        elif not default:
            default_list = self.NONE_DEFAULT
        else:
            default_list = self._formatter(default)
        return default_list

    def _formatter(self, value):
        return [self.quote_trailing_and_leading_space(v) for v in value]
