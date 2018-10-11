#!/usr/bin/python
# -*- coding: utf-8 -*-
"""

Converts an NGSI v2 Normalized Representation 
into an NGSI-LD Representation

Copyright (c) 2018 FIWARE Foundation e.V.

Author: José Manuel Cantera

"""

import sys
import json
import ntpath

from rfc3987 import parse
from copy import deepcopy

ld_context = 'https://fiware.github.io/dataModels/ldContext/fiware-ld-context.jsonld'


def ngsild_uri(type_part, id_part):
    template = 'urn:ngsi-ld:{}:{}'

    return template.format(type_part, id_part)


# Generates an Entity Id as a URI
def ld_id(entity_id, entity_type):
    out = entity_id
    try:
        d = parse(entity_id, rule='URI')
        print(d)
        if d['authority'] == None:
             out = ngsild_uri(entity_type, entity_id)
    except ValueError:
        print 'val error'
        out = ngsild_uri(entity_type, entity_id)
    
    return out


# Generates a Relationship's object as a URI
def ld_object(attribute_name, entity_id):
    out = entity_id
    try:
        d = parse(entity_id, rule='URI')
    except ValueError:
        entity_type = ''
        if attribute_name.startswith('ref'):
            entity_type = attribute_name[3:]

        out = ngsild_uri(entity_type, entity_id)
    
    return out


# Prints the JSON string but with the proper key order
def print_json_string(entity):
    print entity['id']
    
    entity_only_id = {
        'id': entity['id'],
    }
    
    out = json.dumps(entity_only_id, indent=4)[:-2]
    
    entity_only_type = {
        'type': entity['type'],
    }
    
    # with -2 it is removed the new line char as well
    out += "," + json.dumps(entity_only_type, indent=4)[1:-2]

    entity_cloned = deepcopy(entity)
    
    del entity_cloned['id']
    del entity_cloned['type']
    del entity_cloned['@context']
    
    # Now the rest of the entity without the '@context
    out += "," + json.dumps(entity_cloned,indent=4)[1:-2] 
    
    # Last go the '@context'
    only_ld_context = {
        '@context': entity['@context']
    }
    
    out += "," + json.dumps(only_ld_context, indent=4)[1:] 
    
    return out


# Do all the transformation work
def normalized_2_LD(entity):
    out = {
        '@context': ld_context
    }

    for key in entity:
        if key == 'id':
            out[key] = ld_id(entity['id'], entity['type'])
            continue

        if key == 'type':
            out[key] = entity[key]
            continue

        attr = entity[key]
        out[key] = {}
        ld_attr = out[key]

        if not('type' in attr) or attr['type'] != 'Relationship':
            ld_attr['type'] = 'Property'
            ld_attr['value'] = attr['value']
        else:
            ld_attr['type'] = 'Relationship'
            ld_attr['object'] = ld_object(key, attr['value'])

        if key == 'location':
            ld_attr['type'] = 'GeoProperty'

        if 'type' in attr and attr['type'] == 'DateTime':
            ld_attr['value'] = {
                '@type': 'DateTime',
                '@value': attr['value']
            }
        
        if 'type' in attr and attr['type'] == 'PostalAddress':
            ld_attr['value']['type'] = 'PostalAddress'

        if 'metadata' in attr:
            metadata = attr['metadata']
            
            for mkey in metadata:
                if mkey == 'timestamp':
                    ld_attr['observedAt'] = metadata[mey]['value']
                elif mkey == 'unitCode':
                    ld_attr['unitCode'] = metadata[mkey]['value']
                else:
                    sub_attr = {}
                    # Metadata which are Relationships is assumed not to be there
                    sub_attr['type'] = 'Property'
                    sub_attr['value'] = metadata[mkey]['value']
                    ld_attr[mkey] = sub_attr

    return out


def read_json(infile):
    with open(infile) as data_file:
        data = json.loads(data_file.read())

    return data


def write_json(data, outfile):
    with open(outfile, 'w') as data_file:
        # json.dump(data, data_file, indent=4)
        data_file.write(print_json_string(data))
        data_file.write("\n")


def main(args):
    data = read_json(args[1])
    result = normalized_2_LD(data)
    file_name = ntpath.basename(args[1])
    write_json(result, 'example-LD.json')


if __name__ == '__main__':
    if(len(sys.argv) != 2):
        print("Usage: normalized2LD [file]")
        exit(-1)

    main(sys.argv)
