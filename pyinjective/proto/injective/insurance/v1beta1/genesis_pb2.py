# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: injective/insurance/v1beta1/genesis.proto
# Protobuf Python Version: 4.25.0
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from injective.insurance.v1beta1 import insurance_pb2 as injective_dot_insurance_dot_v1beta1_dot_insurance__pb2
from gogoproto import gogo_pb2 as gogoproto_dot_gogo__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n)injective/insurance/v1beta1/genesis.proto\x12\x1binjective.insurance.v1beta1\x1a+injective/insurance/v1beta1/insurance.proto\x1a\x14gogoproto/gogo.proto\"\xaa\x02\n\x0cGenesisState\x12\x39\n\x06params\x18\x01 \x01(\x0b\x32#.injective.insurance.v1beta1.ParamsB\x04\xc8\xde\x1f\x00\x12I\n\x0finsurance_funds\x18\x02 \x03(\x0b\x32*.injective.insurance.v1beta1.InsuranceFundB\x04\xc8\xde\x1f\x00\x12R\n\x13redemption_schedule\x18\x03 \x03(\x0b\x32/.injective.insurance.v1beta1.RedemptionScheduleB\x04\xc8\xde\x1f\x00\x12\x1b\n\x13next_share_denom_id\x18\x04 \x01(\x04\x12#\n\x1bnext_redemption_schedule_id\x18\x05 \x01(\x04\x42QZOgithub.com/InjectiveLabs/injective-core/injective-chain/modules/insurance/typesb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'injective.insurance.v1beta1.genesis_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
  _globals['DESCRIPTOR']._options = None
  _globals['DESCRIPTOR']._serialized_options = b'ZOgithub.com/InjectiveLabs/injective-core/injective-chain/modules/insurance/types'
  _globals['_GENESISSTATE'].fields_by_name['params']._options = None
  _globals['_GENESISSTATE'].fields_by_name['params']._serialized_options = b'\310\336\037\000'
  _globals['_GENESISSTATE'].fields_by_name['insurance_funds']._options = None
  _globals['_GENESISSTATE'].fields_by_name['insurance_funds']._serialized_options = b'\310\336\037\000'
  _globals['_GENESISSTATE'].fields_by_name['redemption_schedule']._options = None
  _globals['_GENESISSTATE'].fields_by_name['redemption_schedule']._serialized_options = b'\310\336\037\000'
  _globals['_GENESISSTATE']._serialized_start=142
  _globals['_GENESISSTATE']._serialized_end=440
# @@protoc_insertion_point(module_scope)
