from injective_proto.proto.descriptor import INJECTIVE_DESCRIPTOR_POOL
# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: ibc/applications/transfer/v1/genesis.proto
# Protobuf Python Version: 5.26.1
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from injective_proto.proto.ibc.applications.transfer.v1 import transfer_pb2 as ibc_dot_applications_dot_transfer_dot_v1_dot_transfer__pb2
from injective_proto.proto.cosmos.base.v1beta1 import coin_pb2 as cosmos_dot_base_dot_v1beta1_dot_coin__pb2
from injective_proto.proto.gogoproto import gogo_pb2 as gogoproto_dot_gogo__pb2


DESCRIPTOR = INJECTIVE_DESCRIPTOR_POOL.AddSerializedFile(b'\n*ibc/applications/transfer/v1/genesis.proto\x12\x1cibc.applications.transfer.v1\x1a+ibc/applications/transfer/v1/transfer.proto\x1a\x1e\x63osmos/base/v1beta1/coin.proto\x1a\x14gogoproto/gogo.proto\"\xbc\x02\n\x0cGenesisState\x12\x17\n\x07port_id\x18\x01 \x01(\tR\x06portId\x12[\n\x0c\x64\x65nom_traces\x18\x02 \x03(\x0b\x32(.ibc.applications.transfer.v1.DenomTraceB\x0e\xc8\xde\x1f\x00\xaa\xdf\x1f\x06TracesR\x0b\x64\x65nomTraces\x12\x42\n\x06params\x18\x03 \x01(\x0b\x32$.ibc.applications.transfer.v1.ParamsB\x04\xc8\xde\x1f\x00R\x06params\x12r\n\x0etotal_escrowed\x18\x04 \x03(\x0b\x32\x19.cosmos.base.v1beta1.CoinB0\xc8\xde\x1f\x00\xaa\xdf\x1f(github.com/cosmos/cosmos-sdk/types.CoinsR\rtotalEscrowedB\xfc\x01\n com.ibc.applications.transfer.v1B\x0cGenesisProtoP\x01Z7github.com/cosmos/ibc-go/v8/modules/apps/transfer/types\xa2\x02\x03IAT\xaa\x02\x1cIbc.Applications.Transfer.V1\xca\x02\x1cIbc\\Applications\\Transfer\\V1\xe2\x02(Ibc\\Applications\\Transfer\\V1\\GPBMetadata\xea\x02\x1fIbc::Applications::Transfer::V1b\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'ibc.applications.transfer.v1.genesis_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'\n com.ibc.applications.transfer.v1B\014GenesisProtoP\001Z7github.com/cosmos/ibc-go/v8/modules/apps/transfer/types\242\002\003IAT\252\002\034Ibc.Applications.Transfer.V1\312\002\034Ibc\\Applications\\Transfer\\V1\342\002(Ibc\\Applications\\Transfer\\V1\\GPBMetadata\352\002\037Ibc::Applications::Transfer::V1'
  _globals['_GENESISSTATE'].fields_by_name['denom_traces']._loaded_options = None
  _globals['_GENESISSTATE'].fields_by_name['denom_traces']._serialized_options = b'\310\336\037\000\252\337\037\006Traces'
  _globals['_GENESISSTATE'].fields_by_name['params']._loaded_options = None
  _globals['_GENESISSTATE'].fields_by_name['params']._serialized_options = b'\310\336\037\000'
  _globals['_GENESISSTATE'].fields_by_name['total_escrowed']._loaded_options = None
  _globals['_GENESISSTATE'].fields_by_name['total_escrowed']._serialized_options = b'\310\336\037\000\252\337\037(github.com/cosmos/cosmos-sdk/types.Coins'
  _globals['_GENESISSTATE']._serialized_start=176
  _globals['_GENESISSTATE']._serialized_end=492
# @@protoc_insertion_point(module_scope)
