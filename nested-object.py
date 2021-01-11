#!/usr/bin/env python

import argparse
import json

def nested_get(input_dict, nested_key):
    internal_dict_value = input_dict
    for k in nested_key:
        internal_dict_value = internal_dict_value.get(k, None)
        if internal_dict_value is None:
            return None
    return internal_dict_value

def main():
    parser = argparse.ArgumentParser(
        formatter_class=argparse.RawTextHelpFormatter,
        description='''
            Initial bootstrap for PDU account.
                - kms-key-id        KMS key ID or alias
                - region            Region of the account
        ''')
    parser.add_argument(
        '--object',
        required=True, 
        help='Nested Object'
    )
    parser.add_argument(
        '--key',
        required=True, 
        help='Search key'
    )

    args = parser.parse_args()
    
    try:
        input_dict = json.loads(args.object)
    except json.decoder.JSONDecodeError as json_error:
                raise ValueError("JSON improperly formatted: %s" % str(json_error))
    
    nested_key = args.key.split('/')
    print(nested_get(input_dict,nested_key)) 

if __name__ == "__main__":
    main()