#!/usr/bin/env python

# Copyright (c) 2018 Aptomi, Inc. All Rights Reserved.
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

import json
import sys
import consulate
import common

def check(instream):
    input = json.load(instream)

    # create consul_instance
    consul_instance = consulate.Consul(host=input['source']['host'], port=input['source'].get('port', 443), scheme=input['source'].get('scheme', 'https'), token=input['source']['token'])

    # see which key we need to monitor
    key = input['source']['key']
    if not key or len(key) <= 0:
        common.msg("[check] consul singlekey resource expected a non-empty key name")
        exit(1)

    value = consul_instance.kv[key] if key in consul_instance.kv else ""
    common.msg("[check] consul singlekey resource {0} = {1}".format(key, value))

    # see if the same as previous version, or different
    version = input.get('version')
    valueOld = version.get('value', "") if version is not None else ""
    if valueOld is None or value == valueOld:
        return [{'value': value}]

    return [{'value': valueOld}, {'value': value}]

def main():
    print(json.dumps(check(sys.stdin)))

if __name__ == '__main__':
    main()
