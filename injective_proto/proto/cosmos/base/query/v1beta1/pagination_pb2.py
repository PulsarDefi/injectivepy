from injective_proto.proto.descriptor import INJECTIVE_DESCRIPTOR_POOL
# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: cosmos/base/query/v1beta1/pagination.proto
# Protobuf Python Version: 5.26.1
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = INJECTIVE_DESCRIPTOR_POOL.AddSerializedFile(b'\n*cosmos/base/query/v1beta1/pagination.proto\x12\x19\x63osmos.base.query.v1beta1\"\x88\x01\n\x0bPageRequest\x12\x10\n\x03key\x18\x01 \x01(\x0cR\x03key\x12\x16\n\x06offset\x18\x02 \x01(\x04R\x06offset\x12\x14\n\x05limit\x18\x03 \x01(\x04R\x05limit\x12\x1f\n\x0b\x63ount_total\x18\x04 \x01(\x08R\ncountTotal\x12\x18\n\x07reverse\x18\x05 \x01(\x08R\x07reverse\"?\n\x0cPageResponse\x12\x19\n\x08next_key\x18\x01 \x01(\x0cR\x07nextKey\x12\x14\n\x05total\x18\x02 \x01(\x04R\x05totalB\xe1\x01\n\x1d\x63om.cosmos.base.query.v1beta1B\x0fPaginationProtoP\x01Z(github.com/cosmos/cosmos-sdk/types/query\xa2\x02\x03\x43\x42Q\xaa\x02\x19\x43osmos.Base.Query.V1beta1\xca\x02\x19\x43osmos\\Base\\Query\\V1beta1\xe2\x02%Cosmos\\Base\\Query\\V1beta1\\GPBMetadata\xea\x02\x1c\x43osmos::Base::Query::V1beta1b\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'cosmos.base.query.v1beta1.pagination_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'\n\035com.cosmos.base.query.v1beta1B\017PaginationProtoP\001Z(github.com/cosmos/cosmos-sdk/types/query\242\002\003CBQ\252\002\031Cosmos.Base.Query.V1beta1\312\002\031Cosmos\\Base\\Query\\V1beta1\342\002%Cosmos\\Base\\Query\\V1beta1\\GPBMetadata\352\002\034Cosmos::Base::Query::V1beta1'
  _globals['_PAGEREQUEST']._serialized_start=74
  _globals['_PAGEREQUEST']._serialized_end=210
  _globals['_PAGERESPONSE']._serialized_start=212
  _globals['_PAGERESPONSE']._serialized_end=275
# @@protoc_insertion_point(module_scope)
