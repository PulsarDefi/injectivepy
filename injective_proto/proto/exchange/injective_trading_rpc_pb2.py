from injective_proto.proto.descriptor import INJECTIVE_DESCRIPTOR_POOL
# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: exchange/injective_trading_rpc.proto
# Protobuf Python Version: 5.26.1
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = INJECTIVE_DESCRIPTOR_POOL.AddSerializedFile(b'\n$exchange/injective_trading_rpc.proto\x12\x15injective_trading_rpc\"\xf6\x02\n\x1cListTradingStrategiesRequest\x12\x14\n\x05state\x18\x01 \x01(\tR\x05state\x12\x1b\n\tmarket_id\x18\x02 \x01(\tR\x08marketId\x12#\n\rsubaccount_id\x18\x03 \x01(\tR\x0csubaccountId\x12\'\n\x0f\x61\x63\x63ount_address\x18\x04 \x01(\tR\x0e\x61\x63\x63ountAddress\x12+\n\x11pending_execution\x18\x05 \x01(\x08R\x10pendingExecution\x12\x1d\n\nstart_time\x18\x06 \x01(\x12R\tstartTime\x12\x19\n\x08\x65nd_time\x18\x07 \x01(\x12R\x07\x65ndTime\x12\x14\n\x05limit\x18\x08 \x01(\x11R\x05limit\x12\x12\n\x04skip\x18\t \x01(\x04R\x04skip\x12#\n\rstrategy_type\x18\n \x03(\tR\x0cstrategyType\x12\x1f\n\x0bmarket_type\x18\x0b \x01(\tR\nmarketType\"\x9e\x01\n\x1dListTradingStrategiesResponse\x12\x46\n\nstrategies\x18\x01 \x03(\x0b\x32&.injective_trading_rpc.TradingStrategyR\nstrategies\x12\x35\n\x06paging\x18\x02 \x01(\x0b\x32\x1d.injective_trading_rpc.PagingR\x06paging\"\xd9\n\n\x0fTradingStrategy\x12\x14\n\x05state\x18\x01 \x01(\tR\x05state\x12\x1b\n\tmarket_id\x18\x02 \x01(\tR\x08marketId\x12#\n\rsubaccount_id\x18\x03 \x01(\tR\x0csubaccountId\x12\'\n\x0f\x61\x63\x63ount_address\x18\x04 \x01(\tR\x0e\x61\x63\x63ountAddress\x12)\n\x10\x63ontract_address\x18\x05 \x01(\tR\x0f\x63ontractAddress\x12\'\n\x0f\x65xecution_price\x18\x06 \x01(\tR\x0e\x65xecutionPrice\x12#\n\rbase_quantity\x18\x07 \x01(\tR\x0c\x62\x61seQuantity\x12%\n\x0equote_quantity\x18\x14 \x01(\tR\rquoteQuantity\x12\x1f\n\x0blower_bound\x18\x08 \x01(\tR\nlowerBound\x12\x1f\n\x0bupper_bound\x18\t \x01(\tR\nupperBound\x12\x1b\n\tstop_loss\x18\n \x01(\tR\x08stopLoss\x12\x1f\n\x0btake_profit\x18\x0b \x01(\tR\ntakeProfit\x12\x19\n\x08swap_fee\x18\x0c \x01(\tR\x07swapFee\x12!\n\x0c\x62\x61se_deposit\x18\x11 \x01(\tR\x0b\x62\x61seDeposit\x12#\n\rquote_deposit\x18\x12 \x01(\tR\x0cquoteDeposit\x12(\n\x10market_mid_price\x18\x13 \x01(\tR\x0emarketMidPrice\x12>\n\x1bsubscription_quote_quantity\x18\x15 \x01(\tR\x19subscriptionQuoteQuantity\x12<\n\x1asubscription_base_quantity\x18\x16 \x01(\tR\x18subscriptionBaseQuantity\x12\x31\n\x15number_of_grid_levels\x18\x17 \x01(\tR\x12numberOfGridLevels\x12<\n\x1bshould_exit_with_quote_only\x18\x18 \x01(\x08R\x17shouldExitWithQuoteOnly\x12\x1f\n\x0bstop_reason\x18\x19 \x01(\tR\nstopReason\x12+\n\x11pending_execution\x18\x1a \x01(\x08R\x10pendingExecution\x12%\n\x0e\x63reated_height\x18\r \x01(\x12R\rcreatedHeight\x12%\n\x0eremoved_height\x18\x0e \x01(\x12R\rremovedHeight\x12\x1d\n\ncreated_at\x18\x0f \x01(\x12R\tcreatedAt\x12\x1d\n\nupdated_at\x18\x10 \x01(\x12R\tupdatedAt\x12\x1b\n\texit_type\x18\x1b \x01(\tR\x08\x65xitType\x12K\n\x10stop_loss_config\x18\x1c \x01(\x0b\x32!.injective_trading_rpc.ExitConfigR\x0estopLossConfig\x12O\n\x12take_profit_config\x18\x1d \x01(\x0b\x32!.injective_trading_rpc.ExitConfigR\x10takeProfitConfig\x12#\n\rstrategy_type\x18\x1e \x01(\tR\x0cstrategyType\x12)\n\x10\x63ontract_version\x18\x1f \x01(\tR\x0f\x63ontractVersion\x12#\n\rcontract_name\x18  \x01(\tR\x0c\x63ontractName\x12\x1f\n\x0bmarket_type\x18! \x01(\tR\nmarketType\"H\n\nExitConfig\x12\x1b\n\texit_type\x18\x01 \x01(\tR\x08\x65xitType\x12\x1d\n\nexit_price\x18\x02 \x01(\tR\texitPrice\"\x86\x01\n\x06Paging\x12\x14\n\x05total\x18\x01 \x01(\x12R\x05total\x12\x12\n\x04\x66rom\x18\x02 \x01(\x11R\x04\x66rom\x12\x0e\n\x02to\x18\x03 \x01(\x11R\x02to\x12.\n\x13\x63ount_by_subaccount\x18\x04 \x01(\x12R\x11\x63ountBySubaccount\x12\x12\n\x04next\x18\x05 \x03(\tR\x04next2\x9a\x01\n\x13InjectiveTradingRPC\x12\x82\x01\n\x15ListTradingStrategies\x12\x33.injective_trading_rpc.ListTradingStrategiesRequest\x1a\x34.injective_trading_rpc.ListTradingStrategiesResponseB\xbb\x01\n\x19\x63om.injective_trading_rpcB\x18InjectiveTradingRpcProtoP\x01Z\x18/injective_trading_rpcpb\xa2\x02\x03IXX\xaa\x02\x13InjectiveTradingRpc\xca\x02\x13InjectiveTradingRpc\xe2\x02\x1fInjectiveTradingRpc\\GPBMetadata\xea\x02\x13InjectiveTradingRpcb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'exchange.injective_trading_rpc_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'\n\031com.injective_trading_rpcB\030InjectiveTradingRpcProtoP\001Z\030/injective_trading_rpcpb\242\002\003IXX\252\002\023InjectiveTradingRpc\312\002\023InjectiveTradingRpc\342\002\037InjectiveTradingRpc\\GPBMetadata\352\002\023InjectiveTradingRpc'
  _globals['_LISTTRADINGSTRATEGIESREQUEST']._serialized_start=64
  _globals['_LISTTRADINGSTRATEGIESREQUEST']._serialized_end=438
  _globals['_LISTTRADINGSTRATEGIESRESPONSE']._serialized_start=441
  _globals['_LISTTRADINGSTRATEGIESRESPONSE']._serialized_end=599
  _globals['_TRADINGSTRATEGY']._serialized_start=602
  _globals['_TRADINGSTRATEGY']._serialized_end=1971
  _globals['_EXITCONFIG']._serialized_start=1973
  _globals['_EXITCONFIG']._serialized_end=2045
  _globals['_PAGING']._serialized_start=2048
  _globals['_PAGING']._serialized_end=2182
  _globals['_INJECTIVETRADINGRPC']._serialized_start=2185
  _globals['_INJECTIVETRADINGRPC']._serialized_end=2339
# @@protoc_insertion_point(module_scope)
