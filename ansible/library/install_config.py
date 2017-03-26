#!/usr/bin/env python

import os
import json

from distutils.version import LooseVersion
from lxml import etree
from collections import OrderedDict

def main():
    module = AnsibleModule(
        argument_spec=dict(
            source_dir=dict(required=True),
            database=dict(required=True),
            bucket_name=dict(required=False, default='default'),
            logfile=dict(required=False, default=None),
            user=dict(required=False, default=os.getenv('USER')),
            passwd=dict(required=False, default=None, no_log=True),
            ssh_private_key_file=dict(required=False, default=None)),
            supports_check_mode=True)

    m_args = module.params
    m_results = dict(changed=False)

    try:
        import couchbase
        from couchbase.bucket import Bucket
        import xmljson
    except ImportError as ex:
        module.fail_json(msg='ImportError: %s' % ex.message)

    try:
        cb = Bucket('couchbase://%s/%s' % (m_args['database'], m_args['bucket_name']))
    except Exception as ex:
        module.fail_json(msg='couchbase connection error: %s' % ex.message)

    try:
        for filename in os.listdir(m_args['source_dir']):
            file_to_open = m_args['source_dir'] +  "/" + filename
            config_file = open(file_to_open, 'r')
            read_xml = config_file.read()
            config_xml = etree.fromstring(read_xml)
            cb.upsert('150.10.0.3', xmljson.parker.data(config_xml), format=couchbase.FMT_JSON)
    except Exception as ex:
        module.fail_json(msg='failed in document save: %s' % ex.message)

    
    module.exit_json(**m_results)

from ansible.module_utils.basic import *

if __name__ == '__main__':
    main()
