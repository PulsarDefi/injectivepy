from injective_proto.proto.descriptor import INJECTIVE_DESCRIPTOR_POOL
# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: ibc/applications/interchain_accounts/genesis/v1/genesis.proto
# Protobuf Python Version: 5.26.1
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from injective_proto.proto.gogoproto import gogo_pb2 as gogoproto_dot_gogo__pb2
from injective_proto.proto.ibc.applications.interchain_accounts.controller.v1 import controller_pb2 as ibc_dot_applications_dot_interchain__accounts_dot_controller_dot_v1_dot_controller__pb2
from injective_proto.proto.ibc.applications.interchain_accounts.host.v1 import host_pb2 as ibc_dot_applications_dot_interchain__accounts_dot_host_dot_v1_dot_host__pb2


DESCRIPTOR = INJECTIVE_DESCRIPTOR_POOL.AddSerializedFile(b'\n=ibc/applications/interchain_accounts/genesis/v1/genesis.proto\x12/ibc.applications.interchain_accounts.genesis.v1\x1a\x14gogoproto/gogo.proto\x1a\x43ibc/applications/interchain_accounts/controller/v1/controller.proto\x1a\x37ibc/applications/interchain_accounts/host/v1/host.proto\"\x8f\x02\n\x0cGenesisState\x12\x87\x01\n\x18\x63ontroller_genesis_state\x18\x01 \x01(\x0b\x32G.ibc.applications.interchain_accounts.genesis.v1.ControllerGenesisStateB\x04\xc8\xde\x1f\x00R\x16\x63ontrollerGenesisState\x12u\n\x12host_genesis_state\x18\x02 \x01(\x0b\x32\x41.ibc.applications.interchain_accounts.genesis.v1.HostGenesisStateB\x04\xc8\xde\x1f\x00R\x10hostGenesisState\"\xfd\x02\n\x16\x43ontrollerGenesisState\x12m\n\x0f\x61\x63tive_channels\x18\x01 \x03(\x0b\x32>.ibc.applications.interchain_accounts.genesis.v1.ActiveChannelB\x04\xc8\xde\x1f\x00R\x0e\x61\x63tiveChannels\x12\x83\x01\n\x13interchain_accounts\x18\x02 \x03(\x0b\x32L.ibc.applications.interchain_accounts.genesis.v1.RegisteredInterchainAccountB\x04\xc8\xde\x1f\x00R\x12interchainAccounts\x12\x14\n\x05ports\x18\x03 \x03(\tR\x05ports\x12X\n\x06params\x18\x04 \x01(\x0b\x32:.ibc.applications.interchain_accounts.controller.v1.ParamsB\x04\xc8\xde\x1f\x00R\x06params\"\xef\x02\n\x10HostGenesisState\x12m\n\x0f\x61\x63tive_channels\x18\x01 \x03(\x0b\x32>.ibc.applications.interchain_accounts.genesis.v1.ActiveChannelB\x04\xc8\xde\x1f\x00R\x0e\x61\x63tiveChannels\x12\x83\x01\n\x13interchain_accounts\x18\x02 \x03(\x0b\x32L.ibc.applications.interchain_accounts.genesis.v1.RegisteredInterchainAccountB\x04\xc8\xde\x1f\x00R\x12interchainAccounts\x12\x12\n\x04port\x18\x03 \x01(\tR\x04port\x12R\n\x06params\x18\x04 \x01(\x0b\x32\x34.ibc.applications.interchain_accounts.host.v1.ParamsB\x04\xc8\xde\x1f\x00R\x06params\"\xa0\x01\n\rActiveChannel\x12#\n\rconnection_id\x18\x01 \x01(\tR\x0c\x63onnectionId\x12\x17\n\x07port_id\x18\x02 \x01(\tR\x06portId\x12\x1d\n\nchannel_id\x18\x03 \x01(\tR\tchannelId\x12\x32\n\x15is_middleware_enabled\x18\x04 \x01(\x08R\x13isMiddlewareEnabled\"\x84\x01\n\x1bRegisteredInterchainAccount\x12#\n\rconnection_id\x18\x01 \x01(\tR\x0c\x63onnectionId\x12\x17\n\x07port_id\x18\x02 \x01(\tR\x06portId\x12\'\n\x0f\x61\x63\x63ount_address\x18\x03 \x01(\tR\x0e\x61\x63\x63ountAddressB\xef\x02\n3com.ibc.applications.interchain_accounts.genesis.v1B\x0cGenesisProtoP\x01ZMgithub.com/cosmos/ibc-go/v8/modules/apps/27-interchain-accounts/genesis/types\xa2\x02\x04IAIG\xaa\x02.Ibc.Applications.InterchainAccounts.Genesis.V1\xca\x02.Ibc\\Applications\\InterchainAccounts\\Genesis\\V1\xe2\x02:Ibc\\Applications\\InterchainAccounts\\Genesis\\V1\\GPBMetadata\xea\x02\x32Ibc::Applications::InterchainAccounts::Genesis::V1b\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'ibc.applications.interchain_accounts.genesis.v1.genesis_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'\n3com.ibc.applications.interchain_accounts.genesis.v1B\014GenesisProtoP\001ZMgithub.com/cosmos/ibc-go/v8/modules/apps/27-interchain-accounts/genesis/types\242\002\004IAIG\252\002.Ibc.Applications.InterchainAccounts.Genesis.V1\312\002.Ibc\\Applications\\InterchainAccounts\\Genesis\\V1\342\002:Ibc\\Applications\\InterchainAccounts\\Genesis\\V1\\GPBMetadata\352\0022Ibc::Applications::InterchainAccounts::Genesis::V1'
  _globals['_GENESISSTATE'].fields_by_name['controller_genesis_state']._loaded_options = None
  _globals['_GENESISSTATE'].fields_by_name['controller_genesis_state']._serialized_options = b'\310\336\037\000'
  _globals['_GENESISSTATE'].fields_by_name['host_genesis_state']._loaded_options = None
  _globals['_GENESISSTATE'].fields_by_name['host_genesis_state']._serialized_options = b'\310\336\037\000'
  _globals['_CONTROLLERGENESISSTATE'].fields_by_name['active_channels']._loaded_options = None
  _globals['_CONTROLLERGENESISSTATE'].fields_by_name['active_channels']._serialized_options = b'\310\336\037\000'
  _globals['_CONTROLLERGENESISSTATE'].fields_by_name['interchain_accounts']._loaded_options = None
  _globals['_CONTROLLERGENESISSTATE'].fields_by_name['interchain_accounts']._serialized_options = b'\310\336\037\000'
  _globals['_CONTROLLERGENESISSTATE'].fields_by_name['params']._loaded_options = None
  _globals['_CONTROLLERGENESISSTATE'].fields_by_name['params']._serialized_options = b'\310\336\037\000'
  _globals['_HOSTGENESISSTATE'].fields_by_name['active_channels']._loaded_options = None
  _globals['_HOSTGENESISSTATE'].fields_by_name['active_channels']._serialized_options = b'\310\336\037\000'
  _globals['_HOSTGENESISSTATE'].fields_by_name['interchain_accounts']._loaded_options = None
  _globals['_HOSTGENESISSTATE'].fields_by_name['interchain_accounts']._serialized_options = b'\310\336\037\000'
  _globals['_HOSTGENESISSTATE'].fields_by_name['params']._loaded_options = None
  _globals['_HOSTGENESISSTATE'].fields_by_name['params']._serialized_options = b'\310\336\037\000'
  _globals['_GENESISSTATE']._serialized_start=263
  _globals['_GENESISSTATE']._serialized_end=534
  _globals['_CONTROLLERGENESISSTATE']._serialized_start=537
  _globals['_CONTROLLERGENESISSTATE']._serialized_end=918
  _globals['_HOSTGENESISSTATE']._serialized_start=921
  _globals['_HOSTGENESISSTATE']._serialized_end=1288
  _globals['_ACTIVECHANNEL']._serialized_start=1291
  _globals['_ACTIVECHANNEL']._serialized_end=1451
  _globals['_REGISTEREDINTERCHAINACCOUNT']._serialized_start=1454
  _globals['_REGISTEREDINTERCHAINACCOUNT']._serialized_end=1586
# @@protoc_insertion_point(module_scope)