from injective_proto.proto.descriptor import INJECTIVE_DESCRIPTOR_POOL
# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: exchange/event_provider_api.proto
# Protobuf Python Version: 5.26.1
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = INJECTIVE_DESCRIPTOR_POOL.AddSerializedFile(b'\n!exchange/event_provider_api.proto\x12\x12\x65vent_provider_api\"\x18\n\x16GetLatestHeightRequest\"~\n\x17GetLatestHeightResponse\x12\x0c\n\x01v\x18\x01 \x01(\tR\x01v\x12\x0c\n\x01s\x18\x02 \x01(\tR\x01s\x12\x0c\n\x01\x65\x18\x03 \x01(\tR\x01\x65\x12\x39\n\x04\x64\x61ta\x18\x04 \x01(\x0b\x32%.event_provider_api.LatestBlockHeightR\x04\x64\x61ta\"+\n\x11LatestBlockHeight\x12\x16\n\x06height\x18\x01 \x01(\x04R\x06height\"L\n\x18StreamBlockEventsRequest\x12\x18\n\x07\x62\x61\x63kend\x18\x01 \x01(\tR\x07\x62\x61\x63kend\x12\x16\n\x06height\x18\x02 \x01(\x11R\x06height\"N\n\x19StreamBlockEventsResponse\x12\x31\n\x06\x62locks\x18\x01 \x03(\x0b\x32\x19.event_provider_api.BlockR\x06\x62locks\"\x8a\x01\n\x05\x42lock\x12\x16\n\x06height\x18\x01 \x01(\x12R\x06height\x12\x18\n\x07version\x18\x02 \x01(\tR\x07version\x12\x36\n\x06\x65vents\x18\x03 \x03(\x0b\x32\x1e.event_provider_api.BlockEventR\x06\x65vents\x12\x17\n\x07in_sync\x18\x04 \x01(\x08R\x06inSync\"V\n\nBlockEvent\x12\x19\n\x08type_url\x18\x01 \x01(\tR\x07typeUrl\x12\x14\n\x05value\x18\x02 \x01(\x0cR\x05value\x12\x17\n\x07tx_hash\x18\x03 \x01(\x0cR\x06txHash\"L\n\x18GetBlockEventsRPCRequest\x12\x18\n\x07\x62\x61\x63kend\x18\x01 \x01(\tR\x07\x62\x61\x63kend\x12\x16\n\x06height\x18\x02 \x01(\x11R\x06height\"}\n\x19GetBlockEventsRPCResponse\x12\x0c\n\x01v\x18\x01 \x01(\tR\x01v\x12\x0c\n\x01s\x18\x02 \x01(\tR\x01s\x12\x0c\n\x01\x65\x18\x03 \x01(\tR\x01\x65\x12\x36\n\x04\x64\x61ta\x18\x04 \x01(\x0b\x32\".event_provider_api.BlockEventsRPCR\x04\x64\x61ta\"\xca\x01\n\x0e\x42lockEventsRPC\x12\x14\n\x05types\x18\x01 \x03(\tR\x05types\x12\x16\n\x06\x65vents\x18\x02 \x03(\x0cR\x06\x65vents\x12M\n\ttx_hashes\x18\x03 \x03(\x0b\x32\x30.event_provider_api.BlockEventsRPC.TxHashesEntryR\x08txHashes\x1a;\n\rTxHashesEntry\x12\x10\n\x03key\x18\x01 \x01(\x11R\x03key\x12\x14\n\x05value\x18\x02 \x01(\x0cR\x05value:\x02\x38\x01\"e\n\x19GetCustomEventsRPCRequest\x12\x18\n\x07\x62\x61\x63kend\x18\x01 \x01(\tR\x07\x62\x61\x63kend\x12\x16\n\x06height\x18\x02 \x01(\x11R\x06height\x12\x16\n\x06\x65vents\x18\x03 \x01(\tR\x06\x65vents\"~\n\x1aGetCustomEventsRPCResponse\x12\x0c\n\x01v\x18\x01 \x01(\tR\x01v\x12\x0c\n\x01s\x18\x02 \x01(\tR\x01s\x12\x0c\n\x01\x65\x18\x03 \x01(\tR\x01\x65\x12\x36\n\x04\x64\x61ta\x18\x04 \x01(\x0b\x32\".event_provider_api.BlockEventsRPCR\x04\x64\x61ta\"T\n\x19GetABCIBlockEventsRequest\x12\x16\n\x06height\x18\x01 \x01(\x11R\x06height\x12\x1f\n\x0b\x65vent_types\x18\x02 \x03(\tR\neventTypes\"\x81\x01\n\x1aGetABCIBlockEventsResponse\x12\x0c\n\x01v\x18\x01 \x01(\tR\x01v\x12\x0c\n\x01s\x18\x02 \x01(\tR\x01s\x12\x0c\n\x01\x65\x18\x03 \x01(\tR\x01\x65\x12\x39\n\traw_block\x18\x04 \x01(\x0b\x32\x1c.event_provider_api.RawBlockR\x08rawBlock\"\xcc\x02\n\x08RawBlock\x12\x16\n\x06height\x18\x01 \x01(\x12R\x06height\x12\x1d\n\nblock_time\x18\x05 \x01(\tR\tblockTime\x12\'\n\x0f\x62lock_timestamp\x18\x06 \x01(\x12R\x0e\x62lockTimestamp\x12J\n\x0btxs_results\x18\x02 \x03(\x0b\x32).event_provider_api.ABCIResponseDeliverTxR\ntxsResults\x12K\n\x12\x62\x65gin_block_events\x18\x03 \x03(\x0b\x32\x1d.event_provider_api.ABCIEventR\x10\x62\x65ginBlockEvents\x12G\n\x10\x65nd_block_events\x18\x04 \x03(\x0b\x32\x1d.event_provider_api.ABCIEventR\x0e\x65ndBlockEvents\"\xf9\x01\n\x15\x41\x42\x43IResponseDeliverTx\x12\x12\n\x04\x63ode\x18\x01 \x01(\x11R\x04\x63ode\x12\x10\n\x03log\x18\x02 \x01(\tR\x03log\x12\x12\n\x04info\x18\x03 \x01(\tR\x04info\x12\x1d\n\ngas_wanted\x18\x04 \x01(\x12R\tgasWanted\x12\x19\n\x08gas_used\x18\x05 \x01(\x12R\x07gasUsed\x12\x35\n\x06\x65vents\x18\x06 \x03(\x0b\x32\x1d.event_provider_api.ABCIEventR\x06\x65vents\x12\x1c\n\tcodespace\x18\x07 \x01(\tR\tcodespace\x12\x17\n\x07tx_hash\x18\x08 \x01(\x0cR\x06txHash\"b\n\tABCIEvent\x12\x12\n\x04type\x18\x01 \x01(\tR\x04type\x12\x41\n\nattributes\x18\x02 \x03(\x0b\x32!.event_provider_api.ABCIAttributeR\nattributes\"7\n\rABCIAttribute\x12\x10\n\x03key\x18\x01 \x01(\tR\x03key\x12\x14\n\x05value\x18\x02 \x01(\tR\x05value2\xce\x04\n\x10\x45ventProviderAPI\x12j\n\x0fGetLatestHeight\x12*.event_provider_api.GetLatestHeightRequest\x1a+.event_provider_api.GetLatestHeightResponse\x12r\n\x11StreamBlockEvents\x12,.event_provider_api.StreamBlockEventsRequest\x1a-.event_provider_api.StreamBlockEventsResponse0\x01\x12p\n\x11GetBlockEventsRPC\x12,.event_provider_api.GetBlockEventsRPCRequest\x1a-.event_provider_api.GetBlockEventsRPCResponse\x12s\n\x12GetCustomEventsRPC\x12-.event_provider_api.GetCustomEventsRPCRequest\x1a..event_provider_api.GetCustomEventsRPCResponse\x12s\n\x12GetABCIBlockEvents\x12-.event_provider_api.GetABCIBlockEventsRequest\x1a..event_provider_api.GetABCIBlockEventsResponseB\xa6\x01\n\x16\x63om.event_provider_apiB\x15\x45ventProviderApiProtoP\x01Z\x15/event_provider_apipb\xa2\x02\x03\x45XX\xaa\x02\x10\x45ventProviderApi\xca\x02\x10\x45ventProviderApi\xe2\x02\x1c\x45ventProviderApi\\GPBMetadata\xea\x02\x10\x45ventProviderApib\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'exchange.event_provider_api_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'\n\026com.event_provider_apiB\025EventProviderApiProtoP\001Z\025/event_provider_apipb\242\002\003EXX\252\002\020EventProviderApi\312\002\020EventProviderApi\342\002\034EventProviderApi\\GPBMetadata\352\002\020EventProviderApi'
  _globals['_BLOCKEVENTSRPC_TXHASHESENTRY']._loaded_options = None
  _globals['_BLOCKEVENTSRPC_TXHASHESENTRY']._serialized_options = b'8\001'
  _globals['_GETLATESTHEIGHTREQUEST']._serialized_start=57
  _globals['_GETLATESTHEIGHTREQUEST']._serialized_end=81
  _globals['_GETLATESTHEIGHTRESPONSE']._serialized_start=83
  _globals['_GETLATESTHEIGHTRESPONSE']._serialized_end=209
  _globals['_LATESTBLOCKHEIGHT']._serialized_start=211
  _globals['_LATESTBLOCKHEIGHT']._serialized_end=254
  _globals['_STREAMBLOCKEVENTSREQUEST']._serialized_start=256
  _globals['_STREAMBLOCKEVENTSREQUEST']._serialized_end=332
  _globals['_STREAMBLOCKEVENTSRESPONSE']._serialized_start=334
  _globals['_STREAMBLOCKEVENTSRESPONSE']._serialized_end=412
  _globals['_BLOCK']._serialized_start=415
  _globals['_BLOCK']._serialized_end=553
  _globals['_BLOCKEVENT']._serialized_start=555
  _globals['_BLOCKEVENT']._serialized_end=641
  _globals['_GETBLOCKEVENTSRPCREQUEST']._serialized_start=643
  _globals['_GETBLOCKEVENTSRPCREQUEST']._serialized_end=719
  _globals['_GETBLOCKEVENTSRPCRESPONSE']._serialized_start=721
  _globals['_GETBLOCKEVENTSRPCRESPONSE']._serialized_end=846
  _globals['_BLOCKEVENTSRPC']._serialized_start=849
  _globals['_BLOCKEVENTSRPC']._serialized_end=1051
  _globals['_BLOCKEVENTSRPC_TXHASHESENTRY']._serialized_start=992
  _globals['_BLOCKEVENTSRPC_TXHASHESENTRY']._serialized_end=1051
  _globals['_GETCUSTOMEVENTSRPCREQUEST']._serialized_start=1053
  _globals['_GETCUSTOMEVENTSRPCREQUEST']._serialized_end=1154
  _globals['_GETCUSTOMEVENTSRPCRESPONSE']._serialized_start=1156
  _globals['_GETCUSTOMEVENTSRPCRESPONSE']._serialized_end=1282
  _globals['_GETABCIBLOCKEVENTSREQUEST']._serialized_start=1284
  _globals['_GETABCIBLOCKEVENTSREQUEST']._serialized_end=1368
  _globals['_GETABCIBLOCKEVENTSRESPONSE']._serialized_start=1371
  _globals['_GETABCIBLOCKEVENTSRESPONSE']._serialized_end=1500
  _globals['_RAWBLOCK']._serialized_start=1503
  _globals['_RAWBLOCK']._serialized_end=1835
  _globals['_ABCIRESPONSEDELIVERTX']._serialized_start=1838
  _globals['_ABCIRESPONSEDELIVERTX']._serialized_end=2087
  _globals['_ABCIEVENT']._serialized_start=2089
  _globals['_ABCIEVENT']._serialized_end=2187
  _globals['_ABCIATTRIBUTE']._serialized_start=2189
  _globals['_ABCIATTRIBUTE']._serialized_end=2244
  _globals['_EVENTPROVIDERAPI']._serialized_start=2247
  _globals['_EVENTPROVIDERAPI']._serialized_end=2837
# @@protoc_insertion_point(module_scope)