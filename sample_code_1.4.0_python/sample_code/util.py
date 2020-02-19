# -*- coding: utf-8 -*-
import os
from avro.schema import Parse
from avro.datafile import DataFileReader, DataFileWriter
from avro.io import DatumReader, DatumWriter, BinaryDecoder, BinaryEncoder

current_dir = os.path.dirname(os.path.realpath(__file__))

with open(os.path.join(current_dir, './schema/result.avsc'), 'r') as f:
    RESULT_SCHEMA = f.read().replace('\r', '').replace('\n', '').replace(' ', '')

with open(os.path.join(current_dir, './schema/put_repo_request.avsc'), 'r') as f:
    PUT_REPO_SCHEMA = f.read().replace('\r', '').replace('\n', '').replace(' ', '')

with open(os.path.join(current_dir, './schema/insert_face_request.avsc'), 'r') as f:
    INSERT_FACE_SCHEMA = f.read().replace('\r', '').replace('\n', '').replace(' ', '')

with open(os.path.join(current_dir, './schema/error_response.avsc'), 'r') as f:
    ERROR_SCHEMA = f.read().replace('\r', '').replace('\n', '').replace(' ', '')

# 反序列化
# read_shcmea_str: 读schema
# write_schem_str: 写schema, 一般来说是server用于序列化的schema
def read_avro(read_schema_str, write_schema_str, reader):
    write_schema = Parse(write_schema_str)
    read_schema = Parse(read_schema_str)
    datum_reader = DatumReader(write_schema, read_schema)
    decoder = BinaryDecoder(reader)
    return datum_reader.read(decoder)

# 序列化
# write_schema_str: 用于序列化的shcema
def write_avro(write_schema_str, writer, datum):
    write_schema = Parse(write_schema_str)
    datum_writer = DatumWriter(write_schema)
    encoder = BinaryEncoder(writer)
    datum_writer.write(datum, encoder)
