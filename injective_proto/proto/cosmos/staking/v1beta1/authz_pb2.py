from injective_proto.proto.descriptor import INJECTIVE_DESCRIPTOR_POOL
# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: cosmos/staking/v1beta1/authz.proto
# Protobuf Python Version: 5.26.1
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from injective_proto.proto.gogoproto import gogo_pb2 as gogoproto_dot_gogo__pb2
from injective_proto.proto.cosmos_proto import cosmos_pb2 as cosmos__proto_dot_cosmos__pb2
from injective_proto.proto.cosmos.base.v1beta1 import coin_pb2 as cosmos_dot_base_dot_v1beta1_dot_coin__pb2
from injective_proto.proto.amino import amino_pb2 as amino_dot_amino__pb2


DESCRIPTOR = INJECTIVE_DESCRIPTOR_POOL.AddSerializedFile(b'\n\"cosmos/staking/v1beta1/authz.proto\x12\x16\x63osmos.staking.v1beta1\x1a\x14gogoproto/gogo.proto\x1a\x19\x63osmos_proto/cosmos.proto\x1a\x1e\x63osmos/base/v1beta1/coin.proto\x1a\x11\x61mino/amino.proto\"\xfa\x04\n\x12StakeAuthorization\x12\x65\n\nmax_tokens\x18\x01 \x01(\x0b\x32\x19.cosmos.base.v1beta1.CoinB+\xaa\xdf\x1f\'github.com/cosmos/cosmos-sdk/types.CoinR\tmaxTokens\x12\x84\x01\n\nallow_list\x18\x02 \x01(\x0b\x32\x35.cosmos.staking.v1beta1.StakeAuthorization.ValidatorsB,\xb2\xe7\xb0*\'cosmos-sdk/StakeAuthorization/AllowListH\x00R\tallowList\x12\x81\x01\n\tdeny_list\x18\x03 \x01(\x0b\x32\x35.cosmos.staking.v1beta1.StakeAuthorization.ValidatorsB+\xb2\xe7\xb0*&cosmos-sdk/StakeAuthorization/DenyListH\x00R\x08\x64\x65nyList\x12X\n\x12\x61uthorization_type\x18\x04 \x01(\x0e\x32).cosmos.staking.v1beta1.AuthorizationTypeR\x11\x61uthorizationType\x1a@\n\nValidators\x12\x32\n\x07\x61\x64\x64ress\x18\x01 \x03(\tB\x18\xd2\xb4-\x14\x63osmos.AddressStringR\x07\x61\x64\x64ress:H\xca\xb4-\"cosmos.authz.v1beta1.Authorization\x8a\xe7\xb0*\x1d\x63osmos-sdk/StakeAuthorizationB\x0c\n\nvalidators*\xd2\x01\n\x11\x41uthorizationType\x12\"\n\x1e\x41UTHORIZATION_TYPE_UNSPECIFIED\x10\x00\x12\x1f\n\x1b\x41UTHORIZATION_TYPE_DELEGATE\x10\x01\x12!\n\x1d\x41UTHORIZATION_TYPE_UNDELEGATE\x10\x02\x12!\n\x1d\x41UTHORIZATION_TYPE_REDELEGATE\x10\x03\x12\x32\n.AUTHORIZATION_TYPE_CANCEL_UNBONDING_DELEGATION\x10\x04\x42\xd0\x01\n\x1a\x63om.cosmos.staking.v1beta1B\nAuthzProtoP\x01Z,github.com/cosmos/cosmos-sdk/x/staking/types\xa2\x02\x03\x43SX\xaa\x02\x16\x43osmos.Staking.V1beta1\xca\x02\x16\x43osmos\\Staking\\V1beta1\xe2\x02\"Cosmos\\Staking\\V1beta1\\GPBMetadata\xea\x02\x18\x43osmos::Staking::V1beta1b\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'cosmos.staking.v1beta1.authz_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'\n\032com.cosmos.staking.v1beta1B\nAuthzProtoP\001Z,github.com/cosmos/cosmos-sdk/x/staking/types\242\002\003CSX\252\002\026Cosmos.Staking.V1beta1\312\002\026Cosmos\\Staking\\V1beta1\342\002\"Cosmos\\Staking\\V1beta1\\GPBMetadata\352\002\030Cosmos::Staking::V1beta1'
  _globals['_STAKEAUTHORIZATION_VALIDATORS'].fields_by_name['address']._loaded_options = None
  _globals['_STAKEAUTHORIZATION_VALIDATORS'].fields_by_name['address']._serialized_options = b'\322\264-\024cosmos.AddressString'
  _globals['_STAKEAUTHORIZATION'].fields_by_name['max_tokens']._loaded_options = None
  _globals['_STAKEAUTHORIZATION'].fields_by_name['max_tokens']._serialized_options = b'\252\337\037\'github.com/cosmos/cosmos-sdk/types.Coin'
  _globals['_STAKEAUTHORIZATION'].fields_by_name['allow_list']._loaded_options = None
  _globals['_STAKEAUTHORIZATION'].fields_by_name['allow_list']._serialized_options = b'\262\347\260*\'cosmos-sdk/StakeAuthorization/AllowList'
  _globals['_STAKEAUTHORIZATION'].fields_by_name['deny_list']._loaded_options = None
  _globals['_STAKEAUTHORIZATION'].fields_by_name['deny_list']._serialized_options = b'\262\347\260*&cosmos-sdk/StakeAuthorization/DenyList'
  _globals['_STAKEAUTHORIZATION']._loaded_options = None
  _globals['_STAKEAUTHORIZATION']._serialized_options = b'\312\264-\"cosmos.authz.v1beta1.Authorization\212\347\260*\035cosmos-sdk/StakeAuthorization'
  _globals['_AUTHORIZATIONTYPE']._serialized_start=800
  _globals['_AUTHORIZATIONTYPE']._serialized_end=1010
  _globals['_STAKEAUTHORIZATION']._serialized_start=163
  _globals['_STAKEAUTHORIZATION']._serialized_end=797
  _globals['_STAKEAUTHORIZATION_VALIDATORS']._serialized_start=645
  _globals['_STAKEAUTHORIZATION_VALIDATORS']._serialized_end=709
# @@protoc_insertion_point(module_scope)