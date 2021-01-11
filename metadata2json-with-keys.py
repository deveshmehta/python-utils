#!/usr/bin/env python

import requests
import json
import argparse

# Converts AWS EC2 instance metadata to a dictionary
def load():
    parser = argparse.ArgumentParser(
        formatter_class=argparse.RawTextHelpFormatter,
        description='''
            Initial bootstrap for PDU account.
                - kms-key-id        KMS key ID or alias
                - region            Region of the account
        ''')
    parser.add_argument(
        '--key',
        help='Allows for a particular data key to be retrieved individually'
    )
    args = parser.parse_args()

    metaurl = 'http://169.254.169.254/latest'
    # those 3 top subdirectories are not exposed with a final '/'
    metadict = {'dynamic': {}, 'meta-data': {}, 'user-data': {}}

    for subsect in metadict.keys():
        datacrawl('{0}/{1}/'.format(metaurl, subsect), metadict[subsect])

    nested_key = args.key.split('/')
    print(nested_get(metadict,nested_key))

def datacrawl(url, d):
    r = requests.get(url)
    if r.status_code == 404:
        return

    for l in r.text.split('\n'):
        if not l: # "instance-identity/\n" case
            continue
        newurl = '{0}{1}'.format(url, l)
        # a key is detected with a final '/'
        if l.endswith('/'):
            newkey = l.split('/')[-2]
            d[newkey] = {}
            datacrawl(newurl, d[newkey])

        else:
            r = requests.get(newurl)
            if r.status_code != 404:
                try:
                    d[l] = json.loads(r.text)
                except ValueError:
                    d[l] = r.text
            else:
                d[l] = None

def nested_get(input_dict, nested_key):
    internal_dict_value = input_dict
    for k in nested_key:
        internal_dict_value = internal_dict_value.get(k, None)
        if internal_dict_value is None:
            return None
    return internal_dict_value

if __name__ == '__main__':
    load()