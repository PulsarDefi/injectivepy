from injective_proto.proto.descriptor import INJECTIVE_DESCRIPTOR_POOL
# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: cosmos/store/internal/kv/v1beta1/kv.proto
# Protobuf Python Version: 5.26.1
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from injective_proto.proto.gogoproto import gogo_pb2 as gogoproto_dot_gogo__pb2


DESCRIPTOR = INJECTIVE_DESCRIPTOR_POOL.AddSerializedFile(b'\n)cosmos/store/internal/kv/v1beta1/kv.proto\x12 cosmos.store.internal.kv.v1beta1\x1a\x14gogoproto/gogo.proto\"K\n\x05Pairs\x12\x42\n\x05pairs\x18\x01 \x03(\x0b\x32&.cosmos.store.internal.kv.v1beta1.PairB\x04\xc8\xde\x1f\x00R\x05pairs\".\n\x04Pair\x12\x10\n\x03key\x18\x01 \x01(\x0cR\x03key\x12\x14\n\x05value\x18\x02 \x01(\x0cR\x05valueB\xf4\x01\n$com.cosmos.store.internal.kv.v1beta1B\x07KvProtoP\x01Z\x1e\x63osmossdk.io/store/internal/kv\xa2\x02\x04\x43SIK\xaa\x02 Cosmos.Store.Internal.Kv.V1beta1\xca\x02 Cosmos\\Store\\Internal\\Kv\\V1beta1\xe2\x02,Cosmos\\Store\\Internal\\Kv\\V1beta1\\GPBMetadata\xea\x02$Cosmos::Store::Internal::Kv::V1beta1b\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'cosmos.store.internal.kv.v1beta1.kv_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'\n$com.cosmos.store.internal.kv.v1beta1B\007KvProtoP\001Z\036cosmossdk.io/store/internal/kv\242\002\004CSIK\252\002 Cosmos.Store.Internal.Kv.V1beta1\312\002 Cosmos\\Store\\Internal\\Kv\\V1beta1\342\002,Cosmos\\Store\\Internal\\Kv\\V1beta1\\GPBMetadata\352\002$Cosmos::Store::Internal::Kv::V1beta1'
  _globals['_PAIRS'].fields_by_name['pairs']._loaded_options = None
  _globals['_PAIRS'].fields_by_name['pairs']._serialized_options = b'\310\336\037\000'
  _globals['_PAIRS']._serialized_start=101
  _globals['_PAIRS']._serialized_end=176
  _globals['_PAIR']._serialized_start=178
  _globals['_PAIR']._serialized_end=224
# @@protoc_insertion_point(module_scope)
