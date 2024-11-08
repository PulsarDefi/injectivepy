from injective_proto.proto.descriptor import INJECTIVE_DESCRIPTOR_POOL
# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: injective/types/v1beta1/account.proto
# Protobuf Python Version: 5.26.1
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from injective_proto.proto.cosmos.auth.v1beta1 import auth_pb2 as cosmos_dot_auth_dot_v1beta1_dot_auth__pb2
from injective_proto.proto.cosmos_proto import cosmos_pb2 as cosmos__proto_dot_cosmos__pb2
from injective_proto.proto.gogoproto import gogo_pb2 as gogoproto_dot_gogo__pb2


DESCRIPTOR = INJECTIVE_DESCRIPTOR_POOL.AddSerializedFile(b'\n%injective/types/v1beta1/account.proto\x12\x17injective.types.v1beta1\x1a\x1e\x63osmos/auth/v1beta1/auth.proto\x1a\x19\x63osmos_proto/cosmos.proto\x1a\x14gogoproto/gogo.proto\"\xcf\x01\n\nEthAccount\x12`\n\x0c\x62\x61se_account\x18\x01 \x01(\x0b\x32 .cosmos.auth.v1beta1.BaseAccountB\x1b\xd0\xde\x1f\x01\xf2\xde\x1f\x13yaml:\"base_account\"R\x0b\x62\x61seAccount\x12\x31\n\tcode_hash\x18\x02 \x01(\x0c\x42\x14\xf2\xde\x1f\x10yaml:\"code_hash\"R\x08\x63odeHash:,\x88\xa0\x1f\x00\x98\xa0\x1f\x00\xe8\xa0\x1f\x00\xca\xb4-\x1c\x63osmos.auth.v1beta1.AccountIB\xe8\x01\n\x1b\x63om.injective.types.v1beta1B\x0c\x41\x63\x63ountProtoP\x01Z=github.com/InjectiveLabs/injective-core/injective-chain/types\xa2\x02\x03ITX\xaa\x02\x17Injective.Types.V1beta1\xca\x02\x17Injective\\Types\\V1beta1\xe2\x02#Injective\\Types\\V1beta1\\GPBMetadata\xea\x02\x19Injective::Types::V1beta1b\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'injective.types.v1beta1.account_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'\n\033com.injective.types.v1beta1B\014AccountProtoP\001Z=github.com/InjectiveLabs/injective-core/injective-chain/types\242\002\003ITX\252\002\027Injective.Types.V1beta1\312\002\027Injective\\Types\\V1beta1\342\002#Injective\\Types\\V1beta1\\GPBMetadata\352\002\031Injective::Types::V1beta1'
  _globals['_ETHACCOUNT'].fields_by_name['base_account']._loaded_options = None
  _globals['_ETHACCOUNT'].fields_by_name['base_account']._serialized_options = b'\320\336\037\001\362\336\037\023yaml:\"base_account\"'
  _globals['_ETHACCOUNT'].fields_by_name['code_hash']._loaded_options = None
  _globals['_ETHACCOUNT'].fields_by_name['code_hash']._serialized_options = b'\362\336\037\020yaml:\"code_hash\"'
  _globals['_ETHACCOUNT']._loaded_options = None
  _globals['_ETHACCOUNT']._serialized_options = b'\210\240\037\000\230\240\037\000\350\240\037\000\312\264-\034cosmos.auth.v1beta1.AccountI'
  _globals['_ETHACCOUNT']._serialized_start=148
  _globals['_ETHACCOUNT']._serialized_end=355
# @@protoc_insertion_point(module_scope)
