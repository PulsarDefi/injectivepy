from pyinjective.proto.descriptor import INJECTIVE_DESCRIPTOR_POOL
# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: injective/ocr/v1beta1/genesis.proto
# Protobuf Python Version: 5.26.1
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from pyinjective.proto.injective.ocr.v1beta1 import ocr_pb2 as injective_dot_ocr_dot_v1beta1_dot_ocr__pb2
from pyinjective.proto.gogoproto import gogo_pb2 as gogoproto_dot_gogo__pb2
from pyinjective.proto.cosmos.base.v1beta1 import coin_pb2 as cosmos_dot_base_dot_v1beta1_dot_coin__pb2


DESCRIPTOR = INJECTIVE_DESCRIPTOR_POOL.AddSerializedFile(b'\n#injective/ocr/v1beta1/genesis.proto\x12\x15injective.ocr.v1beta1\x1a\x1finjective/ocr/v1beta1/ocr.proto\x1a\x14gogoproto/gogo.proto\x1a\x1e\x63osmos/base/v1beta1/coin.proto\"\x94\x06\n\x0cGenesisState\x12;\n\x06params\x18\x01 \x01(\x0b\x32\x1d.injective.ocr.v1beta1.ParamsB\x04\xc8\xde\x1f\x00R\x06params\x12\x44\n\x0c\x66\x65\x65\x64_configs\x18\x02 \x03(\x0b\x32!.injective.ocr.v1beta1.FeedConfigR\x0b\x66\x65\x65\x64\x43onfigs\x12_\n\x17latest_epoch_and_rounds\x18\x03 \x03(\x0b\x32(.injective.ocr.v1beta1.FeedEpochAndRoundR\x14latestEpochAndRounds\x12V\n\x12\x66\x65\x65\x64_transmissions\x18\x04 \x03(\x0b\x32\'.injective.ocr.v1beta1.FeedTransmissionR\x11\x66\x65\x65\x64Transmissions\x12r\n\x1blatest_aggregator_round_ids\x18\x05 \x03(\x0b\x32\x33.injective.ocr.v1beta1.FeedLatestAggregatorRoundIDsR\x18latestAggregatorRoundIds\x12\x44\n\x0creward_pools\x18\x06 \x03(\x0b\x32!.injective.ocr.v1beta1.RewardPoolR\x0brewardPools\x12Y\n\x17\x66\x65\x65\x64_observation_counts\x18\x07 \x03(\x0b\x32!.injective.ocr.v1beta1.FeedCountsR\x15\x66\x65\x65\x64ObservationCounts\x12[\n\x18\x66\x65\x65\x64_transmission_counts\x18\x08 \x03(\x0b\x32!.injective.ocr.v1beta1.FeedCountsR\x16\x66\x65\x65\x64TransmissionCounts\x12V\n\x12pending_payeeships\x18\t \x03(\x0b\x32\'.injective.ocr.v1beta1.PendingPayeeshipR\x11pendingPayeeships\"t\n\x10\x46\x65\x65\x64Transmission\x12\x17\n\x07\x66\x65\x65\x64_id\x18\x01 \x01(\tR\x06\x66\x65\x65\x64Id\x12G\n\x0ctransmission\x18\x02 \x01(\x0b\x32#.injective.ocr.v1beta1.TransmissionR\x0ctransmission\"z\n\x11\x46\x65\x65\x64\x45pochAndRound\x12\x17\n\x07\x66\x65\x65\x64_id\x18\x01 \x01(\tR\x06\x66\x65\x65\x64Id\x12L\n\x0f\x65poch_and_round\x18\x02 \x01(\x0b\x32$.injective.ocr.v1beta1.EpochAndRoundR\repochAndRound\"g\n\x1c\x46\x65\x65\x64LatestAggregatorRoundIDs\x12\x17\n\x07\x66\x65\x65\x64_id\x18\x01 \x01(\tR\x06\x66\x65\x65\x64Id\x12.\n\x13\x61ggregator_round_id\x18\x02 \x01(\x04R\x11\x61ggregatorRoundId\"^\n\nRewardPool\x12\x17\n\x07\x66\x65\x65\x64_id\x18\x01 \x01(\tR\x06\x66\x65\x65\x64Id\x12\x37\n\x06\x61mount\x18\x02 \x01(\x0b\x32\x19.cosmos.base.v1beta1.CoinB\x04\xc8\xde\x1f\x00R\x06\x61mount\"[\n\nFeedCounts\x12\x17\n\x07\x66\x65\x65\x64_id\x18\x01 \x01(\tR\x06\x66\x65\x65\x64Id\x12\x34\n\x06\x63ounts\x18\x02 \x03(\x0b\x32\x1c.injective.ocr.v1beta1.CountR\x06\x63ounts\"7\n\x05\x43ount\x12\x18\n\x07\x61\x64\x64ress\x18\x01 \x01(\tR\x07\x61\x64\x64ress\x12\x14\n\x05\x63ount\x18\x02 \x01(\x04R\x05\x63ount\"t\n\x10PendingPayeeship\x12\x17\n\x07\x66\x65\x65\x64_id\x18\x01 \x01(\tR\x06\x66\x65\x65\x64Id\x12 \n\x0btransmitter\x18\x02 \x01(\tR\x0btransmitter\x12%\n\x0eproposed_payee\x18\x03 \x01(\tR\rproposedPayeeB\xea\x01\n\x19\x63om.injective.ocr.v1beta1B\x0cGenesisProtoP\x01ZIgithub.com/InjectiveLabs/injective-core/injective-chain/modules/ocr/types\xa2\x02\x03IOX\xaa\x02\x15Injective.Ocr.V1beta1\xca\x02\x15Injective\\Ocr\\V1beta1\xe2\x02!Injective\\Ocr\\V1beta1\\GPBMetadata\xea\x02\x17Injective::Ocr::V1beta1b\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'injective.ocr.v1beta1.genesis_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'\n\031com.injective.ocr.v1beta1B\014GenesisProtoP\001ZIgithub.com/InjectiveLabs/injective-core/injective-chain/modules/ocr/types\242\002\003IOX\252\002\025Injective.Ocr.V1beta1\312\002\025Injective\\Ocr\\V1beta1\342\002!Injective\\Ocr\\V1beta1\\GPBMetadata\352\002\027Injective::Ocr::V1beta1'
  _globals['_GENESISSTATE'].fields_by_name['params']._loaded_options = None
  _globals['_GENESISSTATE'].fields_by_name['params']._serialized_options = b'\310\336\037\000'
  _globals['_REWARDPOOL'].fields_by_name['amount']._loaded_options = None
  _globals['_REWARDPOOL'].fields_by_name['amount']._serialized_options = b'\310\336\037\000'
  _globals['_GENESISSTATE']._serialized_start=150
  _globals['_GENESISSTATE']._serialized_end=938
  _globals['_FEEDTRANSMISSION']._serialized_start=940
  _globals['_FEEDTRANSMISSION']._serialized_end=1056
  _globals['_FEEDEPOCHANDROUND']._serialized_start=1058
  _globals['_FEEDEPOCHANDROUND']._serialized_end=1180
  _globals['_FEEDLATESTAGGREGATORROUNDIDS']._serialized_start=1182
  _globals['_FEEDLATESTAGGREGATORROUNDIDS']._serialized_end=1285
  _globals['_REWARDPOOL']._serialized_start=1287
  _globals['_REWARDPOOL']._serialized_end=1381
  _globals['_FEEDCOUNTS']._serialized_start=1383
  _globals['_FEEDCOUNTS']._serialized_end=1474
  _globals['_COUNT']._serialized_start=1476
  _globals['_COUNT']._serialized_end=1531
  _globals['_PENDINGPAYEESHIP']._serialized_start=1533
  _globals['_PENDINGPAYEESHIP']._serialized_end=1649
# @@protoc_insertion_point(module_scope)
