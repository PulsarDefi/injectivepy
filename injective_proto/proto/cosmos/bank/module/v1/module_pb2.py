from injective_proto.proto.descriptor import INJECTIVE_DESCRIPTOR_POOL
# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: cosmos/bank/module/v1/module.proto
# Protobuf Python Version: 5.26.1
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from injective_proto.proto.cosmos.app.v1alpha1 import module_pb2 as cosmos_dot_app_dot_v1alpha1_dot_module__pb2


DESCRIPTOR = INJECTIVE_DESCRIPTOR_POOL.AddSerializedFile(b'\n\"cosmos/bank/module/v1/module.proto\x12\x15\x63osmos.bank.module.v1\x1a cosmos/app/v1alpha1/module.proto\"\xcb\x01\n\x06Module\x12G\n blocked_module_accounts_override\x18\x01 \x03(\tR\x1d\x62lockedModuleAccountsOverride\x12\x1c\n\tauthority\x18\x02 \x01(\tR\tauthority\x12-\n\x12restrictions_order\x18\x03 \x03(\tR\x11restrictionsOrder:+\xba\xc0\x96\xda\x01%\n#github.com/cosmos/cosmos-sdk/x/bankB\x9f\x01\n\x19\x63om.cosmos.bank.module.v1B\x0bModuleProtoP\x01\xa2\x02\x03\x43\x42M\xaa\x02\x15\x43osmos.Bank.Module.V1\xca\x02\x15\x43osmos\\Bank\\Module\\V1\xe2\x02!Cosmos\\Bank\\Module\\V1\\GPBMetadata\xea\x02\x18\x43osmos::Bank::Module::V1b\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'cosmos.bank.module.v1.module_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'\n\031com.cosmos.bank.module.v1B\013ModuleProtoP\001\242\002\003CBM\252\002\025Cosmos.Bank.Module.V1\312\002\025Cosmos\\Bank\\Module\\V1\342\002!Cosmos\\Bank\\Module\\V1\\GPBMetadata\352\002\030Cosmos::Bank::Module::V1'
  _globals['_MODULE']._loaded_options = None
  _globals['_MODULE']._serialized_options = b'\272\300\226\332\001%\n#github.com/cosmos/cosmos-sdk/x/bank'
  _globals['_MODULE']._serialized_start=96
  _globals['_MODULE']._serialized_end=299
# @@protoc_insertion_point(module_scope)
