from injective_proto.proto.descriptor import INJECTIVE_DESCRIPTOR_POOL
# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: injective/wasmx/v1/events.proto
# Protobuf Python Version: 5.26.1
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from injective_proto.proto.injective.wasmx.v1 import wasmx_pb2 as injective_dot_wasmx_dot_v1_dot_wasmx__pb2
from injective_proto.proto.injective.wasmx.v1 import proposal_pb2 as injective_dot_wasmx_dot_v1_dot_proposal__pb2
from injective_proto.proto.gogoproto import gogo_pb2 as gogoproto_dot_gogo__pb2


DESCRIPTOR = INJECTIVE_DESCRIPTOR_POOL.AddSerializedFile(b'\n\x1finjective/wasmx/v1/events.proto\x12\x12injective.wasmx.v1\x1a\x1einjective/wasmx/v1/wasmx.proto\x1a!injective/wasmx/v1/proposal.proto\x1a\x14gogoproto/gogo.proto\"\xa9\x01\n\x16\x45ventContractExecution\x12)\n\x10\x63ontract_address\x18\x01 \x01(\tR\x0f\x63ontractAddress\x12\x1a\n\x08response\x18\x02 \x01(\x0cR\x08response\x12\x1f\n\x0bother_error\x18\x03 \x01(\tR\notherError\x12\'\n\x0f\x65xecution_error\x18\x04 \x01(\tR\x0e\x65xecutionError\"\xee\x02\n\x17\x45ventContractRegistered\x12)\n\x10\x63ontract_address\x18\x01 \x01(\tR\x0f\x63ontractAddress\x12\x1b\n\tgas_price\x18\x03 \x01(\x04R\x08gasPrice\x12.\n\x13should_pin_contract\x18\x04 \x01(\x08R\x11shouldPinContract\x12\x30\n\x14is_migration_allowed\x18\x05 \x01(\x08R\x12isMigrationAllowed\x12\x17\n\x07\x63ode_id\x18\x06 \x01(\x04R\x06\x63odeId\x12#\n\radmin_address\x18\x07 \x01(\tR\x0c\x61\x64minAddress\x12\'\n\x0fgranter_address\x18\x08 \x01(\tR\x0egranterAddress\x12\x42\n\x0c\x66unding_mode\x18\t \x01(\x0e\x32\x1f.injective.wasmx.v1.FundingModeR\x0b\x66undingMode\"F\n\x19\x45ventContractDeregistered\x12)\n\x10\x63ontract_address\x18\x01 \x01(\tR\x0f\x63ontractAddressB\xdc\x01\n\x16\x63om.injective.wasmx.v1B\x0b\x45ventsProtoP\x01ZKgithub.com/InjectiveLabs/injective-core/injective-chain/modules/wasmx/types\xa2\x02\x03IWX\xaa\x02\x12Injective.Wasmx.V1\xca\x02\x12Injective\\Wasmx\\V1\xe2\x02\x1eInjective\\Wasmx\\V1\\GPBMetadata\xea\x02\x14Injective::Wasmx::V1b\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'injective.wasmx.v1.events_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'\n\026com.injective.wasmx.v1B\013EventsProtoP\001ZKgithub.com/InjectiveLabs/injective-core/injective-chain/modules/wasmx/types\242\002\003IWX\252\002\022Injective.Wasmx.V1\312\002\022Injective\\Wasmx\\V1\342\002\036Injective\\Wasmx\\V1\\GPBMetadata\352\002\024Injective::Wasmx::V1'
  _globals['_EVENTCONTRACTEXECUTION']._serialized_start=145
  _globals['_EVENTCONTRACTEXECUTION']._serialized_end=314
  _globals['_EVENTCONTRACTREGISTERED']._serialized_start=317
  _globals['_EVENTCONTRACTREGISTERED']._serialized_end=683
  _globals['_EVENTCONTRACTDEREGISTERED']._serialized_start=685
  _globals['_EVENTCONTRACTDEREGISTERED']._serialized_end=755
# @@protoc_insertion_point(module_scope)