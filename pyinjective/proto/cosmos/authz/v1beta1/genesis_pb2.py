# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: cosmos/authz/v1beta1/genesis.proto
# Protobuf Python Version: 4.25.0
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from gogoproto import gogo_pb2 as gogoproto_dot_gogo__pb2
from cosmos.authz.v1beta1 import authz_pb2 as cosmos_dot_authz_dot_v1beta1_dot_authz__pb2
from amino import amino_pb2 as amino_dot_amino__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\"cosmos/authz/v1beta1/genesis.proto\x12\x14\x63osmos.authz.v1beta1\x1a\x14gogoproto/gogo.proto\x1a cosmos/authz/v1beta1/authz.proto\x1a\x11\x61mino/amino.proto\"Z\n\x0cGenesisState\x12J\n\rauthorization\x18\x01 \x03(\x0b\x32(.cosmos.authz.v1beta1.GrantAuthorizationB\t\xc8\xde\x1f\x00\xa8\xe7\xb0*\x01\x42&Z$github.com/cosmos/cosmos-sdk/x/authzb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'cosmos.authz.v1beta1.genesis_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
  _globals['DESCRIPTOR']._options = None
  _globals['DESCRIPTOR']._serialized_options = b'Z$github.com/cosmos/cosmos-sdk/x/authz'
  _globals['_GENESISSTATE'].fields_by_name['authorization']._options = None
  _globals['_GENESISSTATE'].fields_by_name['authorization']._serialized_options = b'\310\336\037\000\250\347\260*\001'
  _globals['_GENESISSTATE']._serialized_start=135
  _globals['_GENESISSTATE']._serialized_end=225
# @@protoc_insertion_point(module_scope)
