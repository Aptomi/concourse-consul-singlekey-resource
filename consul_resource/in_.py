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
import common
import os
import errno

def in_(destdir, instream):
    input = json.load(instream)

    # see which value we need to fetch
    version = input.get('version')
    if not 'value' in version:
        common.msg("[in] consul singlekey resource didn't receive which value to fetch, exiting...")
        exit(1)

    # put on a file system
    value = version['value']
    common.msg("[in] consul singlekey resource, getting value '{0}' and storing in directory {1}".format(value, destdir))
    with safe_open(os.path.join(destdir, "value"), 'w') as f:
        f.write(value.encode("utf-8"))

    return {'version': {'value': value}}

def safe_open(path, mode):
    mkdir_p(os.path.dirname(path))
    return open(path, mode)

def mkdir_p(path):
    try:
        os.makedirs(path)
    except OSError as exc:
        if exc.errno == errno.EEXIST and os.path.isdir(path):
            pass
        else:
            raise

def main():
    print(json.dumps(in_(sys.argv[1], sys.stdin)))

if __name__ == '__main__':
    main()
