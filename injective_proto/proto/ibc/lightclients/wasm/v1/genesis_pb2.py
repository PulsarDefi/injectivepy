from injective_proto.proto.descriptor import INJECTIVE_DESCRIPTOR_POOL
# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: ibc/lightclients/wasm/v1/genesis.proto
# Protobuf Python Version: 5.26.1
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from injective_proto.proto.gogoproto import gogo_pb2 as gogoproto_dot_gogo__pb2


DESCRIPTOR = INJECTIVE_DESCRIPTOR_POOL.AddSerializedFile(b'\n&ibc/lightclients/wasm/v1/genesis.proto\x12\x18ibc.lightclients.wasm.v1\x1a\x14gogoproto/gogo.proto\"V\n\x0cGenesisState\x12\x46\n\tcontracts\x18\x01 \x03(\x0b\x32\".ibc.lightclients.wasm.v1.ContractB\x04\xc8\xde\x1f\x00R\tcontracts\"/\n\x08\x43ontract\x12\x1d\n\ncode_bytes\x18\x01 \x01(\x0cR\tcodeBytes:\x04\x88\xa0\x1f\x00\x42\xed\x01\n\x1c\x63om.ibc.lightclients.wasm.v1B\x0cGenesisProtoP\x01Z<github.com/cosmos/ibc-go/modules/light-clients/08-wasm/types\xa2\x02\x03ILW\xaa\x02\x18Ibc.Lightclients.Wasm.V1\xca\x02\x18Ibc\\Lightclients\\Wasm\\V1\xe2\x02$Ibc\\Lightclients\\Wasm\\V1\\GPBMetadata\xea\x02\x1bIbc::Lightclients::Wasm::V1b\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'ibc.lightclients.wasm.v1.genesis_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'\n\034com.ibc.lightclients.wasm.v1B\014GenesisProtoP\001Z<github.com/cosmos/ibc-go/modules/light-clients/08-wasm/types\242\002\003ILW\252\002\030Ibc.Lightclients.Wasm.V1\312\002\030Ibc\\Lightclients\\Wasm\\V1\342\002$Ibc\\Lightclients\\Wasm\\V1\\GPBMetadata\352\002\033Ibc::Lightclients::Wasm::V1'
  _globals['_GENESISSTATE'].fields_by_name['contracts']._loaded_options = None
  _globals['_GENESISSTATE'].fields_by_name['contracts']._serialized_options = b'\310\336\037\000'
  _globals['_CONTRACT']._loaded_options = None
  _globals['_CONTRACT']._serialized_options = b'\210\240\037\000'
  _globals['_GENESISSTATE']._serialized_start=90
  _globals['_GENESISSTATE']._serialized_end=176
  _globals['_CONTRACT']._serialized_start=178
  _globals['_CONTRACT']._serialized_end=225
# @@protoc_insertion_point(module_scope)
