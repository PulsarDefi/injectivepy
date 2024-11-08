from pyinjective.proto.descriptor import INJECTIVE_DESCRIPTOR_POOL
# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: ibc/applications/transfer/v1/authz.proto
# Protobuf Python Version: 5.26.1
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from pyinjective.proto.cosmos_proto import cosmos_pb2 as cosmos__proto_dot_cosmos__pb2
from pyinjective.proto.gogoproto import gogo_pb2 as gogoproto_dot_gogo__pb2
from pyinjective.proto.cosmos.base.v1beta1 import coin_pb2 as cosmos_dot_base_dot_v1beta1_dot_coin__pb2


DESCRIPTOR = INJECTIVE_DESCRIPTOR_POOL.AddSerializedFile(b'\n(ibc/applications/transfer/v1/authz.proto\x12\x1cibc.applications.transfer.v1\x1a\x19\x63osmos_proto/cosmos.proto\x1a\x14gogoproto/gogo.proto\x1a\x1e\x63osmos/base/v1beta1/coin.proto\"\x91\x02\n\nAllocation\x12\x1f\n\x0bsource_port\x18\x01 \x01(\tR\nsourcePort\x12%\n\x0esource_channel\x18\x02 \x01(\tR\rsourceChannel\x12l\n\x0bspend_limit\x18\x03 \x03(\x0b\x32\x19.cosmos.base.v1beta1.CoinB0\xc8\xde\x1f\x00\xaa\xdf\x1f(github.com/cosmos/cosmos-sdk/types.CoinsR\nspendLimit\x12\x1d\n\nallow_list\x18\x04 \x03(\tR\tallowList\x12.\n\x13\x61llowed_packet_data\x18\x05 \x03(\tR\x11\x61llowedPacketData\"\x91\x01\n\x15TransferAuthorization\x12P\n\x0b\x61llocations\x18\x01 \x03(\x0b\x32(.ibc.applications.transfer.v1.AllocationB\x04\xc8\xde\x1f\x00R\x0b\x61llocations:&\xca\xb4-\"cosmos.authz.v1beta1.AuthorizationB\xfa\x01\n com.ibc.applications.transfer.v1B\nAuthzProtoP\x01Z7github.com/cosmos/ibc-go/v8/modules/apps/transfer/types\xa2\x02\x03IAT\xaa\x02\x1cIbc.Applications.Transfer.V1\xca\x02\x1cIbc\\Applications\\Transfer\\V1\xe2\x02(Ibc\\Applications\\Transfer\\V1\\GPBMetadata\xea\x02\x1fIbc::Applications::Transfer::V1b\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'ibc.applications.transfer.v1.authz_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'\n com.ibc.applications.transfer.v1B\nAuthzProtoP\001Z7github.com/cosmos/ibc-go/v8/modules/apps/transfer/types\242\002\003IAT\252\002\034Ibc.Applications.Transfer.V1\312\002\034Ibc\\Applications\\Transfer\\V1\342\002(Ibc\\Applications\\Transfer\\V1\\GPBMetadata\352\002\037Ibc::Applications::Transfer::V1'
  _globals['_ALLOCATION'].fields_by_name['spend_limit']._loaded_options = None
  _globals['_ALLOCATION'].fields_by_name['spend_limit']._serialized_options = b'\310\336\037\000\252\337\037(github.com/cosmos/cosmos-sdk/types.Coins'
  _globals['_TRANSFERAUTHORIZATION'].fields_by_name['allocations']._loaded_options = None
  _globals['_TRANSFERAUTHORIZATION'].fields_by_name['allocations']._serialized_options = b'\310\336\037\000'
  _globals['_TRANSFERAUTHORIZATION']._loaded_options = None
  _globals['_TRANSFERAUTHORIZATION']._serialized_options = b'\312\264-\"cosmos.authz.v1beta1.Authorization'
  _globals['_ALLOCATION']._serialized_start=156
  _globals['_ALLOCATION']._serialized_end=429
  _globals['_TRANSFERAUTHORIZATION']._serialized_start=432
  _globals['_TRANSFERAUTHORIZATION']._serialized_end=577
# @@protoc_insertion_point(module_scope)
