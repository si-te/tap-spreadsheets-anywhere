import csv
import re
import logging
import sys

LOGGER = logging.getLogger(__name__)

def generator_wrapper(reader, table_spec):   
    field_name = "string"
    if 'field_names' in table_spec and len(table_spec['field_names']) > 0:
        field_name = table_spec['field_names'][0]

    yield {field_name: reader.read()}


def get_row_iterator(table_spec, reader):
    return generator_wrapper(reader, table_spec)
