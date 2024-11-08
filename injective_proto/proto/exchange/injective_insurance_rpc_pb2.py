from injective_proto.proto.descriptor import INJECTIVE_DESCRIPTOR_POOL
# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: exchange/injective_insurance_rpc.proto
# Protobuf Python Version: 5.26.1
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = INJECTIVE_DESCRIPTOR_POOL.AddSerializedFile(b'\n&exchange/injective_insurance_rpc.proto\x12\x17injective_insurance_rpc\"\x0e\n\x0c\x46undsRequest\"M\n\rFundsResponse\x12<\n\x05\x66unds\x18\x01 \x03(\x0b\x32&.injective_insurance_rpc.InsuranceFundR\x05\x66unds\"\xf5\x03\n\rInsuranceFund\x12#\n\rmarket_ticker\x18\x01 \x01(\tR\x0cmarketTicker\x12\x1b\n\tmarket_id\x18\x02 \x01(\tR\x08marketId\x12#\n\rdeposit_denom\x18\x03 \x01(\tR\x0c\x64\x65positDenom\x12(\n\x10pool_token_denom\x18\x04 \x01(\tR\x0epoolTokenDenom\x12I\n!redemption_notice_period_duration\x18\x05 \x01(\x12R\x1eredemptionNoticePeriodDuration\x12\x18\n\x07\x62\x61lance\x18\x06 \x01(\tR\x07\x62\x61lance\x12\x1f\n\x0btotal_share\x18\x07 \x01(\tR\ntotalShare\x12\x1f\n\x0boracle_base\x18\x08 \x01(\tR\noracleBase\x12!\n\x0coracle_quote\x18\t \x01(\tR\x0boracleQuote\x12\x1f\n\x0boracle_type\x18\n \x01(\tR\noracleType\x12\x16\n\x06\x65xpiry\x18\x0b \x01(\x12R\x06\x65xpiry\x12P\n\x12\x64\x65posit_token_meta\x18\x0c \x01(\x0b\x32\".injective_insurance_rpc.TokenMetaR\x10\x64\x65positTokenMeta\"\xa0\x01\n\tTokenMeta\x12\x12\n\x04name\x18\x01 \x01(\tR\x04name\x12\x18\n\x07\x61\x64\x64ress\x18\x02 \x01(\tR\x07\x61\x64\x64ress\x12\x16\n\x06symbol\x18\x03 \x01(\tR\x06symbol\x12\x12\n\x04logo\x18\x04 \x01(\tR\x04logo\x12\x1a\n\x08\x64\x65\x63imals\x18\x05 \x01(\x11R\x08\x64\x65\x63imals\x12\x1d\n\nupdated_at\x18\x06 \x01(\x12R\tupdatedAt\"#\n\x0b\x46undRequest\x12\x14\n\x05\x64\x65nom\x18\x01 \x01(\tR\x05\x64\x65nom\"J\n\x0c\x46undResponse\x12:\n\x04\x66und\x18\x01 \x01(\x0b\x32&.injective_insurance_rpc.InsuranceFundR\x04\x66und\"s\n\x12RedemptionsRequest\x12\x1a\n\x08redeemer\x18\x01 \x01(\tR\x08redeemer\x12)\n\x10redemption_denom\x18\x02 \x01(\tR\x0fredemptionDenom\x12\x16\n\x06status\x18\x03 \x01(\tR\x06status\"u\n\x13RedemptionsResponse\x12^\n\x14redemption_schedules\x18\x01 \x03(\x0b\x32+.injective_insurance_rpc.RedemptionScheduleR\x13redemptionSchedules\"\x9b\x03\n\x12RedemptionSchedule\x12#\n\rredemption_id\x18\x01 \x01(\x04R\x0credemptionId\x12\x16\n\x06status\x18\x02 \x01(\tR\x06status\x12\x1a\n\x08redeemer\x18\x03 \x01(\tR\x08redeemer\x12:\n\x19\x63laimable_redemption_time\x18\x04 \x01(\x12R\x17\x63laimableRedemptionTime\x12+\n\x11redemption_amount\x18\x05 \x01(\tR\x10redemptionAmount\x12)\n\x10redemption_denom\x18\x06 \x01(\tR\x0fredemptionDenom\x12!\n\x0crequested_at\x18\x07 \x01(\x12R\x0brequestedAt\x12)\n\x10\x64isbursed_amount\x18\x08 \x01(\tR\x0f\x64isbursedAmount\x12\'\n\x0f\x64isbursed_denom\x18\t \x01(\tR\x0e\x64isbursedDenom\x12!\n\x0c\x64isbursed_at\x18\n \x01(\x12R\x0b\x64isbursedAt2\xae\x02\n\x15InjectiveInsuranceRPC\x12V\n\x05\x46unds\x12%.injective_insurance_rpc.FundsRequest\x1a&.injective_insurance_rpc.FundsResponse\x12S\n\x04\x46und\x12$.injective_insurance_rpc.FundRequest\x1a%.injective_insurance_rpc.FundResponse\x12h\n\x0bRedemptions\x12+.injective_insurance_rpc.RedemptionsRequest\x1a,.injective_insurance_rpc.RedemptionsResponseB\xc9\x01\n\x1b\x63om.injective_insurance_rpcB\x1aInjectiveInsuranceRpcProtoP\x01Z\x1a/injective_insurance_rpcpb\xa2\x02\x03IXX\xaa\x02\x15InjectiveInsuranceRpc\xca\x02\x15InjectiveInsuranceRpc\xe2\x02!InjectiveInsuranceRpc\\GPBMetadata\xea\x02\x15InjectiveInsuranceRpcb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'exchange.injective_insurance_rpc_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'\n\033com.injective_insurance_rpcB\032InjectiveInsuranceRpcProtoP\001Z\032/injective_insurance_rpcpb\242\002\003IXX\252\002\025InjectiveInsuranceRpc\312\002\025InjectiveInsuranceRpc\342\002!InjectiveInsuranceRpc\\GPBMetadata\352\002\025InjectiveInsuranceRpc'
  _globals['_FUNDSREQUEST']._serialized_start=67
  _globals['_FUNDSREQUEST']._serialized_end=81
  _globals['_FUNDSRESPONSE']._serialized_start=83
  _globals['_FUNDSRESPONSE']._serialized_end=160
  _globals['_INSURANCEFUND']._serialized_start=163
  _globals['_INSURANCEFUND']._serialized_end=664
  _globals['_TOKENMETA']._serialized_start=667
  _globals['_TOKENMETA']._serialized_end=827
  _globals['_FUNDREQUEST']._serialized_start=829
  _globals['_FUNDREQUEST']._serialized_end=864
  _globals['_FUNDRESPONSE']._serialized_start=866
  _globals['_FUNDRESPONSE']._serialized_end=940
  _globals['_REDEMPTIONSREQUEST']._serialized_start=942
  _globals['_REDEMPTIONSREQUEST']._serialized_end=1057
  _globals['_REDEMPTIONSRESPONSE']._serialized_start=1059
  _globals['_REDEMPTIONSRESPONSE']._serialized_end=1176
  _globals['_REDEMPTIONSCHEDULE']._serialized_start=1179
  _globals['_REDEMPTIONSCHEDULE']._serialized_end=1590
  _globals['_INJECTIVEINSURANCERPC']._serialized_start=1593
  _globals['_INJECTIVEINSURANCERPC']._serialized_end=1895
# @@protoc_insertion_point(module_scope)
