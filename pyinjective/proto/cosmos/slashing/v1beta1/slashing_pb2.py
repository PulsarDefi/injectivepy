# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: cosmos/slashing/v1beta1/slashing.proto
# Protobuf Python Version: 5.26.1
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from pyinjective.proto.gogoproto import gogo_pb2 as gogoproto_dot_gogo__pb2
from google.protobuf import duration_pb2 as google_dot_protobuf_dot_duration__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
from pyinjective.proto.cosmos_proto import cosmos_pb2 as cosmos__proto_dot_cosmos__pb2
from pyinjective.proto.amino import amino_pb2 as amino_dot_amino__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n&cosmos/slashing/v1beta1/slashing.proto\x12\x17\x63osmos.slashing.v1beta1\x1a\x14gogoproto/gogo.proto\x1a\x1egoogle/protobuf/duration.proto\x1a\x1fgoogle/protobuf/timestamp.proto\x1a\x19\x63osmos_proto/cosmos.proto\x1a\x11\x61mino/amino.proto\"\xc1\x02\n\x14ValidatorSigningInfo\x12;\n\x07\x61\x64\x64ress\x18\x01 \x01(\tB!\xd2\xb4-\x1d\x63osmos.ConsensusAddressStringR\x07\x61\x64\x64ress\x12!\n\x0cstart_height\x18\x02 \x01(\x03R\x0bstartHeight\x12!\n\x0cindex_offset\x18\x03 \x01(\x03R\x0bindexOffset\x12L\n\x0cjailed_until\x18\x04 \x01(\x0b\x32\x1a.google.protobuf.TimestampB\r\xc8\xde\x1f\x00\x90\xdf\x1f\x01\xa8\xe7\xb0*\x01R\x0bjailedUntil\x12\x1e\n\ntombstoned\x18\x05 \x01(\x08R\ntombstoned\x12\x32\n\x15missed_blocks_counter\x18\x06 \x01(\x03R\x13missedBlocksCounter:\x04\xe8\xa0\x1f\x01\"\x8d\x04\n\x06Params\x12\x30\n\x14signed_blocks_window\x18\x01 \x01(\x03R\x12signedBlocksWindow\x12i\n\x15min_signed_per_window\x18\x02 \x01(\x0c\x42\x36\xc8\xde\x1f\x00\xda\xde\x1f\x1b\x63osmossdk.io/math.LegacyDec\xd2\xb4-\ncosmos.Dec\xa8\xe7\xb0*\x01R\x12minSignedPerWindow\x12^\n\x16\x64owntime_jail_duration\x18\x03 \x01(\x0b\x32\x19.google.protobuf.DurationB\r\xc8\xde\x1f\x00\x98\xdf\x1f\x01\xa8\xe7\xb0*\x01R\x14\x64owntimeJailDuration\x12s\n\x1aslash_fraction_double_sign\x18\x04 \x01(\x0c\x42\x36\xc8\xde\x1f\x00\xda\xde\x1f\x1b\x63osmossdk.io/math.LegacyDec\xd2\xb4-\ncosmos.Dec\xa8\xe7\xb0*\x01R\x17slashFractionDoubleSign\x12n\n\x17slash_fraction_downtime\x18\x05 \x01(\x0c\x42\x36\xc8\xde\x1f\x00\xda\xde\x1f\x1b\x63osmossdk.io/math.LegacyDec\xd2\xb4-\ncosmos.Dec\xa8\xe7\xb0*\x01R\x15slashFractionDowntime:!\x8a\xe7\xb0*\x1c\x63osmos-sdk/x/slashing/ParamsB\xdd\x01\n\x1b\x63om.cosmos.slashing.v1beta1B\rSlashingProtoP\x01Z-github.com/cosmos/cosmos-sdk/x/slashing/types\xa2\x02\x03\x43SX\xaa\x02\x17\x43osmos.Slashing.V1beta1\xca\x02\x17\x43osmos\\Slashing\\V1beta1\xe2\x02#Cosmos\\Slashing\\V1beta1\\GPBMetadata\xea\x02\x19\x43osmos::Slashing::V1beta1\xa8\xe2\x1e\x01\x62\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'cosmos.slashing.v1beta1.slashing_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'\n\033com.cosmos.slashing.v1beta1B\rSlashingProtoP\001Z-github.com/cosmos/cosmos-sdk/x/slashing/types\242\002\003CSX\252\002\027Cosmos.Slashing.V1beta1\312\002\027Cosmos\\Slashing\\V1beta1\342\002#Cosmos\\Slashing\\V1beta1\\GPBMetadata\352\002\031Cosmos::Slashing::V1beta1\250\342\036\001'
  _globals['_VALIDATORSIGNINGINFO'].fields_by_name['address']._loaded_options = None
  _globals['_VALIDATORSIGNINGINFO'].fields_by_name['address']._serialized_options = b'\322\264-\035cosmos.ConsensusAddressString'
  _globals['_VALIDATORSIGNINGINFO'].fields_by_name['jailed_until']._loaded_options = None
  _globals['_VALIDATORSIGNINGINFO'].fields_by_name['jailed_until']._serialized_options = b'\310\336\037\000\220\337\037\001\250\347\260*\001'
  _globals['_VALIDATORSIGNINGINFO']._loaded_options = None
  _globals['_VALIDATORSIGNINGINFO']._serialized_options = b'\350\240\037\001'
  _globals['_PARAMS'].fields_by_name['min_signed_per_window']._loaded_options = None
  _globals['_PARAMS'].fields_by_name['min_signed_per_window']._serialized_options = b'\310\336\037\000\332\336\037\033cosmossdk.io/math.LegacyDec\322\264-\ncosmos.Dec\250\347\260*\001'
  _globals['_PARAMS'].fields_by_name['downtime_jail_duration']._loaded_options = None
  _globals['_PARAMS'].fields_by_name['downtime_jail_duration']._serialized_options = b'\310\336\037\000\230\337\037\001\250\347\260*\001'
  _globals['_PARAMS'].fields_by_name['slash_fraction_double_sign']._loaded_options = None
  _globals['_PARAMS'].fields_by_name['slash_fraction_double_sign']._serialized_options = b'\310\336\037\000\332\336\037\033cosmossdk.io/math.LegacyDec\322\264-\ncosmos.Dec\250\347\260*\001'
  _globals['_PARAMS'].fields_by_name['slash_fraction_downtime']._loaded_options = None
  _globals['_PARAMS'].fields_by_name['slash_fraction_downtime']._serialized_options = b'\310\336\037\000\332\336\037\033cosmossdk.io/math.LegacyDec\322\264-\ncosmos.Dec\250\347\260*\001'
  _globals['_PARAMS']._loaded_options = None
  _globals['_PARAMS']._serialized_options = b'\212\347\260*\034cosmos-sdk/x/slashing/Params'
  _globals['_VALIDATORSIGNINGINFO']._serialized_start=201
  _globals['_VALIDATORSIGNINGINFO']._serialized_end=522
  _globals['_PARAMS']._serialized_start=525
  _globals['_PARAMS']._serialized_end=1050
# @@protoc_insertion_point(module_scope)
