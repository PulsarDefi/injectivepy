from injective_proto.proto.descriptor import INJECTIVE_DESCRIPTOR_POOL
# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: cosmos/circuit/v1/types.proto
# Protobuf Python Version: 5.26.1
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = INJECTIVE_DESCRIPTOR_POOL.AddSerializedFile(b'\n\x1d\x63osmos/circuit/v1/types.proto\x12\x11\x63osmos.circuit.v1\"\xd6\x01\n\x0bPermissions\x12:\n\x05level\x18\x01 \x01(\x0e\x32$.cosmos.circuit.v1.Permissions.LevelR\x05level\x12&\n\x0flimit_type_urls\x18\x02 \x03(\tR\rlimitTypeUrls\"c\n\x05Level\x12\x1a\n\x16LEVEL_NONE_UNSPECIFIED\x10\x00\x12\x13\n\x0fLEVEL_SOME_MSGS\x10\x01\x12\x12\n\x0eLEVEL_ALL_MSGS\x10\x02\x12\x15\n\x11LEVEL_SUPER_ADMIN\x10\x03\"w\n\x19GenesisAccountPermissions\x12\x18\n\x07\x61\x64\x64ress\x18\x01 \x01(\tR\x07\x61\x64\x64ress\x12@\n\x0bpermissions\x18\x02 \x01(\x0b\x32\x1e.cosmos.circuit.v1.PermissionsR\x0bpermissions\"\x9b\x01\n\x0cGenesisState\x12]\n\x13\x61\x63\x63ount_permissions\x18\x01 \x03(\x0b\x32,.cosmos.circuit.v1.GenesisAccountPermissionsR\x12\x61\x63\x63ountPermissions\x12,\n\x12\x64isabled_type_urls\x18\x02 \x03(\tR\x10\x64isabledTypeUrlsB\xa7\x01\n\x15\x63om.cosmos.circuit.v1B\nTypesProtoP\x01Z\x1c\x63osmossdk.io/x/circuit/types\xa2\x02\x03\x43\x43X\xaa\x02\x11\x43osmos.Circuit.V1\xca\x02\x11\x43osmos\\Circuit\\V1\xe2\x02\x1d\x43osmos\\Circuit\\V1\\GPBMetadata\xea\x02\x13\x43osmos::Circuit::V1b\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'cosmos.circuit.v1.types_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'\n\025com.cosmos.circuit.v1B\nTypesProtoP\001Z\034cosmossdk.io/x/circuit/types\242\002\003CCX\252\002\021Cosmos.Circuit.V1\312\002\021Cosmos\\Circuit\\V1\342\002\035Cosmos\\Circuit\\V1\\GPBMetadata\352\002\023Cosmos::Circuit::V1'
  _globals['_PERMISSIONS']._serialized_start=53
  _globals['_PERMISSIONS']._serialized_end=267
  _globals['_PERMISSIONS_LEVEL']._serialized_start=168
  _globals['_PERMISSIONS_LEVEL']._serialized_end=267
  _globals['_GENESISACCOUNTPERMISSIONS']._serialized_start=269
  _globals['_GENESISACCOUNTPERMISSIONS']._serialized_end=388
  _globals['_GENESISSTATE']._serialized_start=391
  _globals['_GENESISSTATE']._serialized_end=546
# @@protoc_insertion_point(module_scope)
