from pyinjective.proto.descriptor import INJECTIVE_DESCRIPTOR_POOL
# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: exchange/injective_spot_exchange_rpc.proto
# Protobuf Python Version: 5.26.1
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = INJECTIVE_DESCRIPTOR_POOL.AddSerializedFile(b'\n*exchange/injective_spot_exchange_rpc.proto\x12\x1binjective_spot_exchange_rpc\"\x9e\x01\n\x0eMarketsRequest\x12#\n\rmarket_status\x18\x01 \x01(\tR\x0cmarketStatus\x12\x1d\n\nbase_denom\x18\x02 \x01(\tR\tbaseDenom\x12\x1f\n\x0bquote_denom\x18\x03 \x01(\tR\nquoteDenom\x12\'\n\x0fmarket_statuses\x18\x04 \x03(\tR\x0emarketStatuses\"X\n\x0fMarketsResponse\x12\x45\n\x07markets\x18\x01 \x03(\x0b\x32+.injective_spot_exchange_rpc.SpotMarketInfoR\x07markets\"\xd1\x04\n\x0eSpotMarketInfo\x12\x1b\n\tmarket_id\x18\x01 \x01(\tR\x08marketId\x12#\n\rmarket_status\x18\x02 \x01(\tR\x0cmarketStatus\x12\x16\n\x06ticker\x18\x03 \x01(\tR\x06ticker\x12\x1d\n\nbase_denom\x18\x04 \x01(\tR\tbaseDenom\x12N\n\x0f\x62\x61se_token_meta\x18\x05 \x01(\x0b\x32&.injective_spot_exchange_rpc.TokenMetaR\rbaseTokenMeta\x12\x1f\n\x0bquote_denom\x18\x06 \x01(\tR\nquoteDenom\x12P\n\x10quote_token_meta\x18\x07 \x01(\x0b\x32&.injective_spot_exchange_rpc.TokenMetaR\x0equoteTokenMeta\x12$\n\x0emaker_fee_rate\x18\x08 \x01(\tR\x0cmakerFeeRate\x12$\n\x0etaker_fee_rate\x18\t \x01(\tR\x0ctakerFeeRate\x12\x30\n\x14service_provider_fee\x18\n \x01(\tR\x12serviceProviderFee\x12-\n\x13min_price_tick_size\x18\x0b \x01(\tR\x10minPriceTickSize\x12\x33\n\x16min_quantity_tick_size\x18\x0c \x01(\tR\x13minQuantityTickSize\x12!\n\x0cmin_notional\x18\r \x01(\tR\x0bminNotional\"\xa0\x01\n\tTokenMeta\x12\x12\n\x04name\x18\x01 \x01(\tR\x04name\x12\x18\n\x07\x61\x64\x64ress\x18\x02 \x01(\tR\x07\x61\x64\x64ress\x12\x16\n\x06symbol\x18\x03 \x01(\tR\x06symbol\x12\x12\n\x04logo\x18\x04 \x01(\tR\x04logo\x12\x1a\n\x08\x64\x65\x63imals\x18\x05 \x01(\x11R\x08\x64\x65\x63imals\x12\x1d\n\nupdated_at\x18\x06 \x01(\x12R\tupdatedAt\",\n\rMarketRequest\x12\x1b\n\tmarket_id\x18\x01 \x01(\tR\x08marketId\"U\n\x0eMarketResponse\x12\x43\n\x06market\x18\x01 \x01(\x0b\x32+.injective_spot_exchange_rpc.SpotMarketInfoR\x06market\"5\n\x14StreamMarketsRequest\x12\x1d\n\nmarket_ids\x18\x01 \x03(\tR\tmarketIds\"\xa1\x01\n\x15StreamMarketsResponse\x12\x43\n\x06market\x18\x01 \x01(\x0b\x32+.injective_spot_exchange_rpc.SpotMarketInfoR\x06market\x12%\n\x0eoperation_type\x18\x02 \x01(\tR\roperationType\x12\x1c\n\ttimestamp\x18\x03 \x01(\x12R\ttimestamp\"1\n\x12OrderbookV2Request\x12\x1b\n\tmarket_id\x18\x01 \x01(\tR\x08marketId\"f\n\x13OrderbookV2Response\x12O\n\torderbook\x18\x01 \x01(\x0b\x32\x31.injective_spot_exchange_rpc.SpotLimitOrderbookV2R\torderbook\"\xcc\x01\n\x14SpotLimitOrderbookV2\x12;\n\x04\x62uys\x18\x01 \x03(\x0b\x32\'.injective_spot_exchange_rpc.PriceLevelR\x04\x62uys\x12=\n\x05sells\x18\x02 \x03(\x0b\x32\'.injective_spot_exchange_rpc.PriceLevelR\x05sells\x12\x1a\n\x08sequence\x18\x03 \x01(\x04R\x08sequence\x12\x1c\n\ttimestamp\x18\x04 \x01(\x12R\ttimestamp\"\\\n\nPriceLevel\x12\x14\n\x05price\x18\x01 \x01(\tR\x05price\x12\x1a\n\x08quantity\x18\x02 \x01(\tR\x08quantity\x12\x1c\n\ttimestamp\x18\x03 \x01(\x12R\ttimestamp\"4\n\x13OrderbooksV2Request\x12\x1d\n\nmarket_ids\x18\x01 \x03(\tR\tmarketIds\"o\n\x14OrderbooksV2Response\x12W\n\norderbooks\x18\x01 \x03(\x0b\x32\x37.injective_spot_exchange_rpc.SingleSpotLimitOrderbookV2R\norderbooks\"\x8a\x01\n\x1aSingleSpotLimitOrderbookV2\x12\x1b\n\tmarket_id\x18\x01 \x01(\tR\x08marketId\x12O\n\torderbook\x18\x02 \x01(\x0b\x32\x31.injective_spot_exchange_rpc.SpotLimitOrderbookV2R\torderbook\"9\n\x18StreamOrderbookV2Request\x12\x1d\n\nmarket_ids\x18\x01 \x03(\tR\tmarketIds\"\xce\x01\n\x19StreamOrderbookV2Response\x12O\n\torderbook\x18\x01 \x01(\x0b\x32\x31.injective_spot_exchange_rpc.SpotLimitOrderbookV2R\torderbook\x12%\n\x0eoperation_type\x18\x02 \x01(\tR\roperationType\x12\x1c\n\ttimestamp\x18\x03 \x01(\x12R\ttimestamp\x12\x1b\n\tmarket_id\x18\x04 \x01(\tR\x08marketId\"=\n\x1cStreamOrderbookUpdateRequest\x12\x1d\n\nmarket_ids\x18\x01 \x03(\tR\tmarketIds\"\xed\x01\n\x1dStreamOrderbookUpdateResponse\x12j\n\x17orderbook_level_updates\x18\x01 \x01(\x0b\x32\x32.injective_spot_exchange_rpc.OrderbookLevelUpdatesR\x15orderbookLevelUpdates\x12%\n\x0eoperation_type\x18\x02 \x01(\tR\roperationType\x12\x1c\n\ttimestamp\x18\x03 \x01(\x12R\ttimestamp\x12\x1b\n\tmarket_id\x18\x04 \x01(\tR\x08marketId\"\xf7\x01\n\x15OrderbookLevelUpdates\x12\x1b\n\tmarket_id\x18\x01 \x01(\tR\x08marketId\x12\x1a\n\x08sequence\x18\x02 \x01(\x04R\x08sequence\x12\x41\n\x04\x62uys\x18\x03 \x03(\x0b\x32-.injective_spot_exchange_rpc.PriceLevelUpdateR\x04\x62uys\x12\x43\n\x05sells\x18\x04 \x03(\x0b\x32-.injective_spot_exchange_rpc.PriceLevelUpdateR\x05sells\x12\x1d\n\nupdated_at\x18\x05 \x01(\x12R\tupdatedAt\"\x7f\n\x10PriceLevelUpdate\x12\x14\n\x05price\x18\x01 \x01(\tR\x05price\x12\x1a\n\x08quantity\x18\x02 \x01(\tR\x08quantity\x12\x1b\n\tis_active\x18\x03 \x01(\x08R\x08isActive\x12\x1c\n\ttimestamp\x18\x04 \x01(\x12R\ttimestamp\"\x83\x03\n\rOrdersRequest\x12\x1b\n\tmarket_id\x18\x01 \x01(\tR\x08marketId\x12\x1d\n\norder_side\x18\x02 \x01(\tR\torderSide\x12#\n\rsubaccount_id\x18\x03 \x01(\tR\x0csubaccountId\x12\x12\n\x04skip\x18\x04 \x01(\x04R\x04skip\x12\x14\n\x05limit\x18\x05 \x01(\x11R\x05limit\x12\x1d\n\nstart_time\x18\x06 \x01(\x12R\tstartTime\x12\x19\n\x08\x65nd_time\x18\x07 \x01(\x12R\x07\x65ndTime\x12\x1d\n\nmarket_ids\x18\x08 \x03(\tR\tmarketIds\x12)\n\x10include_inactive\x18\t \x01(\x08R\x0fincludeInactive\x12\x36\n\x17subaccount_total_orders\x18\n \x01(\x08R\x15subaccountTotalOrders\x12\x19\n\x08trade_id\x18\x0b \x01(\tR\x07tradeId\x12\x10\n\x03\x63id\x18\x0c \x01(\tR\x03\x63id\"\x92\x01\n\x0eOrdersResponse\x12\x43\n\x06orders\x18\x01 \x03(\x0b\x32+.injective_spot_exchange_rpc.SpotLimitOrderR\x06orders\x12;\n\x06paging\x18\x02 \x01(\x0b\x32#.injective_spot_exchange_rpc.PagingR\x06paging\"\xb8\x03\n\x0eSpotLimitOrder\x12\x1d\n\norder_hash\x18\x01 \x01(\tR\torderHash\x12\x1d\n\norder_side\x18\x02 \x01(\tR\torderSide\x12\x1b\n\tmarket_id\x18\x03 \x01(\tR\x08marketId\x12#\n\rsubaccount_id\x18\x04 \x01(\tR\x0csubaccountId\x12\x14\n\x05price\x18\x05 \x01(\tR\x05price\x12\x1a\n\x08quantity\x18\x06 \x01(\tR\x08quantity\x12+\n\x11unfilled_quantity\x18\x07 \x01(\tR\x10unfilledQuantity\x12#\n\rtrigger_price\x18\x08 \x01(\tR\x0ctriggerPrice\x12#\n\rfee_recipient\x18\t \x01(\tR\x0c\x66\x65\x65Recipient\x12\x14\n\x05state\x18\n \x01(\tR\x05state\x12\x1d\n\ncreated_at\x18\x0b \x01(\x12R\tcreatedAt\x12\x1d\n\nupdated_at\x18\x0c \x01(\x12R\tupdatedAt\x12\x17\n\x07tx_hash\x18\r \x01(\tR\x06txHash\x12\x10\n\x03\x63id\x18\x0e \x01(\tR\x03\x63id\"\x86\x01\n\x06Paging\x12\x14\n\x05total\x18\x01 \x01(\x12R\x05total\x12\x12\n\x04\x66rom\x18\x02 \x01(\x11R\x04\x66rom\x12\x0e\n\x02to\x18\x03 \x01(\x11R\x02to\x12.\n\x13\x63ount_by_subaccount\x18\x04 \x01(\x12R\x11\x63ountBySubaccount\x12\x12\n\x04next\x18\x05 \x03(\tR\x04next\"\x89\x03\n\x13StreamOrdersRequest\x12\x1b\n\tmarket_id\x18\x01 \x01(\tR\x08marketId\x12\x1d\n\norder_side\x18\x02 \x01(\tR\torderSide\x12#\n\rsubaccount_id\x18\x03 \x01(\tR\x0csubaccountId\x12\x12\n\x04skip\x18\x04 \x01(\x04R\x04skip\x12\x14\n\x05limit\x18\x05 \x01(\x11R\x05limit\x12\x1d\n\nstart_time\x18\x06 \x01(\x12R\tstartTime\x12\x19\n\x08\x65nd_time\x18\x07 \x01(\x12R\x07\x65ndTime\x12\x1d\n\nmarket_ids\x18\x08 \x03(\tR\tmarketIds\x12)\n\x10include_inactive\x18\t \x01(\x08R\x0fincludeInactive\x12\x36\n\x17subaccount_total_orders\x18\n \x01(\x08R\x15subaccountTotalOrders\x12\x19\n\x08trade_id\x18\x0b \x01(\tR\x07tradeId\x12\x10\n\x03\x63id\x18\x0c \x01(\tR\x03\x63id\"\x9e\x01\n\x14StreamOrdersResponse\x12\x41\n\x05order\x18\x01 \x01(\x0b\x32+.injective_spot_exchange_rpc.SpotLimitOrderR\x05order\x12%\n\x0eoperation_type\x18\x02 \x01(\tR\roperationType\x12\x1c\n\ttimestamp\x18\x03 \x01(\x12R\ttimestamp\"\xbf\x03\n\rTradesRequest\x12\x1b\n\tmarket_id\x18\x01 \x01(\tR\x08marketId\x12%\n\x0e\x65xecution_side\x18\x02 \x01(\tR\rexecutionSide\x12\x1c\n\tdirection\x18\x03 \x01(\tR\tdirection\x12#\n\rsubaccount_id\x18\x04 \x01(\tR\x0csubaccountId\x12\x12\n\x04skip\x18\x05 \x01(\x04R\x04skip\x12\x14\n\x05limit\x18\x06 \x01(\x11R\x05limit\x12\x1d\n\nstart_time\x18\x07 \x01(\x12R\tstartTime\x12\x19\n\x08\x65nd_time\x18\x08 \x01(\x12R\x07\x65ndTime\x12\x1d\n\nmarket_ids\x18\t \x03(\tR\tmarketIds\x12%\n\x0esubaccount_ids\x18\n \x03(\tR\rsubaccountIds\x12\'\n\x0f\x65xecution_types\x18\x0b \x03(\tR\x0e\x65xecutionTypes\x12\x19\n\x08trade_id\x18\x0c \x01(\tR\x07tradeId\x12\'\n\x0f\x61\x63\x63ount_address\x18\r \x01(\tR\x0e\x61\x63\x63ountAddress\x12\x10\n\x03\x63id\x18\x0e \x01(\tR\x03\x63id\"\x8d\x01\n\x0eTradesResponse\x12>\n\x06trades\x18\x01 \x03(\x0b\x32&.injective_spot_exchange_rpc.SpotTradeR\x06trades\x12;\n\x06paging\x18\x02 \x01(\x0b\x32#.injective_spot_exchange_rpc.PagingR\x06paging\"\xb2\x03\n\tSpotTrade\x12\x1d\n\norder_hash\x18\x01 \x01(\tR\torderHash\x12#\n\rsubaccount_id\x18\x02 \x01(\tR\x0csubaccountId\x12\x1b\n\tmarket_id\x18\x03 \x01(\tR\x08marketId\x12\x30\n\x14trade_execution_type\x18\x04 \x01(\tR\x12tradeExecutionType\x12\'\n\x0ftrade_direction\x18\x05 \x01(\tR\x0etradeDirection\x12=\n\x05price\x18\x06 \x01(\x0b\x32\'.injective_spot_exchange_rpc.PriceLevelR\x05price\x12\x10\n\x03\x66\x65\x65\x18\x07 \x01(\tR\x03\x66\x65\x65\x12\x1f\n\x0b\x65xecuted_at\x18\x08 \x01(\x12R\nexecutedAt\x12#\n\rfee_recipient\x18\t \x01(\tR\x0c\x66\x65\x65Recipient\x12\x19\n\x08trade_id\x18\n \x01(\tR\x07tradeId\x12%\n\x0e\x65xecution_side\x18\x0b \x01(\tR\rexecutionSide\x12\x10\n\x03\x63id\x18\x0c \x01(\tR\x03\x63id\"\xc5\x03\n\x13StreamTradesRequest\x12\x1b\n\tmarket_id\x18\x01 \x01(\tR\x08marketId\x12%\n\x0e\x65xecution_side\x18\x02 \x01(\tR\rexecutionSide\x12\x1c\n\tdirection\x18\x03 \x01(\tR\tdirection\x12#\n\rsubaccount_id\x18\x04 \x01(\tR\x0csubaccountId\x12\x12\n\x04skip\x18\x05 \x01(\x04R\x04skip\x12\x14\n\x05limit\x18\x06 \x01(\x11R\x05limit\x12\x1d\n\nstart_time\x18\x07 \x01(\x12R\tstartTime\x12\x19\n\x08\x65nd_time\x18\x08 \x01(\x12R\x07\x65ndTime\x12\x1d\n\nmarket_ids\x18\t \x03(\tR\tmarketIds\x12%\n\x0esubaccount_ids\x18\n \x03(\tR\rsubaccountIds\x12\'\n\x0f\x65xecution_types\x18\x0b \x03(\tR\x0e\x65xecutionTypes\x12\x19\n\x08trade_id\x18\x0c \x01(\tR\x07tradeId\x12\'\n\x0f\x61\x63\x63ount_address\x18\r \x01(\tR\x0e\x61\x63\x63ountAddress\x12\x10\n\x03\x63id\x18\x0e \x01(\tR\x03\x63id\"\x99\x01\n\x14StreamTradesResponse\x12<\n\x05trade\x18\x01 \x01(\x0b\x32&.injective_spot_exchange_rpc.SpotTradeR\x05trade\x12%\n\x0eoperation_type\x18\x02 \x01(\tR\roperationType\x12\x1c\n\ttimestamp\x18\x03 \x01(\x12R\ttimestamp\"\xc1\x03\n\x0fTradesV2Request\x12\x1b\n\tmarket_id\x18\x01 \x01(\tR\x08marketId\x12%\n\x0e\x65xecution_side\x18\x02 \x01(\tR\rexecutionSide\x12\x1c\n\tdirection\x18\x03 \x01(\tR\tdirection\x12#\n\rsubaccount_id\x18\x04 \x01(\tR\x0csubaccountId\x12\x12\n\x04skip\x18\x05 \x01(\x04R\x04skip\x12\x14\n\x05limit\x18\x06 \x01(\x11R\x05limit\x12\x1d\n\nstart_time\x18\x07 \x01(\x12R\tstartTime\x12\x19\n\x08\x65nd_time\x18\x08 \x01(\x12R\x07\x65ndTime\x12\x1d\n\nmarket_ids\x18\t \x03(\tR\tmarketIds\x12%\n\x0esubaccount_ids\x18\n \x03(\tR\rsubaccountIds\x12\'\n\x0f\x65xecution_types\x18\x0b \x03(\tR\x0e\x65xecutionTypes\x12\x19\n\x08trade_id\x18\x0c \x01(\tR\x07tradeId\x12\'\n\x0f\x61\x63\x63ount_address\x18\r \x01(\tR\x0e\x61\x63\x63ountAddress\x12\x10\n\x03\x63id\x18\x0e \x01(\tR\x03\x63id\"\x8f\x01\n\x10TradesV2Response\x12>\n\x06trades\x18\x01 \x03(\x0b\x32&.injective_spot_exchange_rpc.SpotTradeR\x06trades\x12;\n\x06paging\x18\x02 \x01(\x0b\x32#.injective_spot_exchange_rpc.PagingR\x06paging\"\xc7\x03\n\x15StreamTradesV2Request\x12\x1b\n\tmarket_id\x18\x01 \x01(\tR\x08marketId\x12%\n\x0e\x65xecution_side\x18\x02 \x01(\tR\rexecutionSide\x12\x1c\n\tdirection\x18\x03 \x01(\tR\tdirection\x12#\n\rsubaccount_id\x18\x04 \x01(\tR\x0csubaccountId\x12\x12\n\x04skip\x18\x05 \x01(\x04R\x04skip\x12\x14\n\x05limit\x18\x06 \x01(\x11R\x05limit\x12\x1d\n\nstart_time\x18\x07 \x01(\x12R\tstartTime\x12\x19\n\x08\x65nd_time\x18\x08 \x01(\x12R\x07\x65ndTime\x12\x1d\n\nmarket_ids\x18\t \x03(\tR\tmarketIds\x12%\n\x0esubaccount_ids\x18\n \x03(\tR\rsubaccountIds\x12\'\n\x0f\x65xecution_types\x18\x0b \x03(\tR\x0e\x65xecutionTypes\x12\x19\n\x08trade_id\x18\x0c \x01(\tR\x07tradeId\x12\'\n\x0f\x61\x63\x63ount_address\x18\r \x01(\tR\x0e\x61\x63\x63ountAddress\x12\x10\n\x03\x63id\x18\x0e \x01(\tR\x03\x63id\"\x9b\x01\n\x16StreamTradesV2Response\x12<\n\x05trade\x18\x01 \x01(\x0b\x32&.injective_spot_exchange_rpc.SpotTradeR\x05trade\x12%\n\x0eoperation_type\x18\x02 \x01(\tR\roperationType\x12\x1c\n\ttimestamp\x18\x03 \x01(\x12R\ttimestamp\"\x89\x01\n\x1bSubaccountOrdersListRequest\x12#\n\rsubaccount_id\x18\x01 \x01(\tR\x0csubaccountId\x12\x1b\n\tmarket_id\x18\x02 \x01(\tR\x08marketId\x12\x12\n\x04skip\x18\x03 \x01(\x04R\x04skip\x12\x14\n\x05limit\x18\x04 \x01(\x11R\x05limit\"\xa0\x01\n\x1cSubaccountOrdersListResponse\x12\x43\n\x06orders\x18\x01 \x03(\x0b\x32+.injective_spot_exchange_rpc.SpotLimitOrderR\x06orders\x12;\n\x06paging\x18\x02 \x01(\x0b\x32#.injective_spot_exchange_rpc.PagingR\x06paging\"\xce\x01\n\x1bSubaccountTradesListRequest\x12#\n\rsubaccount_id\x18\x01 \x01(\tR\x0csubaccountId\x12\x1b\n\tmarket_id\x18\x02 \x01(\tR\x08marketId\x12%\n\x0e\x65xecution_type\x18\x03 \x01(\tR\rexecutionType\x12\x1c\n\tdirection\x18\x04 \x01(\tR\tdirection\x12\x12\n\x04skip\x18\x05 \x01(\x04R\x04skip\x12\x14\n\x05limit\x18\x06 \x01(\x11R\x05limit\"^\n\x1cSubaccountTradesListResponse\x12>\n\x06trades\x18\x01 \x03(\x0b\x32&.injective_spot_exchange_rpc.SpotTradeR\x06trades\"\xb6\x03\n\x14OrdersHistoryRequest\x12#\n\rsubaccount_id\x18\x01 \x01(\tR\x0csubaccountId\x12\x1b\n\tmarket_id\x18\x02 \x01(\tR\x08marketId\x12\x12\n\x04skip\x18\x03 \x01(\x04R\x04skip\x12\x14\n\x05limit\x18\x04 \x01(\x11R\x05limit\x12\x1f\n\x0border_types\x18\x05 \x03(\tR\norderTypes\x12\x1c\n\tdirection\x18\x06 \x01(\tR\tdirection\x12\x1d\n\nstart_time\x18\x07 \x01(\x12R\tstartTime\x12\x19\n\x08\x65nd_time\x18\x08 \x01(\x12R\x07\x65ndTime\x12\x14\n\x05state\x18\t \x01(\tR\x05state\x12\'\n\x0f\x65xecution_types\x18\n \x03(\tR\x0e\x65xecutionTypes\x12\x1d\n\nmarket_ids\x18\x0b \x03(\tR\tmarketIds\x12\x19\n\x08trade_id\x18\x0c \x01(\tR\x07tradeId\x12.\n\x13\x61\x63tive_markets_only\x18\r \x01(\x08R\x11\x61\x63tiveMarketsOnly\x12\x10\n\x03\x63id\x18\x0e \x01(\tR\x03\x63id\"\x9b\x01\n\x15OrdersHistoryResponse\x12\x45\n\x06orders\x18\x01 \x03(\x0b\x32-.injective_spot_exchange_rpc.SpotOrderHistoryR\x06orders\x12;\n\x06paging\x18\x02 \x01(\x0b\x32#.injective_spot_exchange_rpc.PagingR\x06paging\"\xf3\x03\n\x10SpotOrderHistory\x12\x1d\n\norder_hash\x18\x01 \x01(\tR\torderHash\x12\x1b\n\tmarket_id\x18\x02 \x01(\tR\x08marketId\x12\x1b\n\tis_active\x18\x03 \x01(\x08R\x08isActive\x12#\n\rsubaccount_id\x18\x04 \x01(\tR\x0csubaccountId\x12%\n\x0e\x65xecution_type\x18\x05 \x01(\tR\rexecutionType\x12\x1d\n\norder_type\x18\x06 \x01(\tR\torderType\x12\x14\n\x05price\x18\x07 \x01(\tR\x05price\x12#\n\rtrigger_price\x18\x08 \x01(\tR\x0ctriggerPrice\x12\x1a\n\x08quantity\x18\t \x01(\tR\x08quantity\x12\'\n\x0f\x66illed_quantity\x18\n \x01(\tR\x0e\x66illedQuantity\x12\x14\n\x05state\x18\x0b \x01(\tR\x05state\x12\x1d\n\ncreated_at\x18\x0c \x01(\x12R\tcreatedAt\x12\x1d\n\nupdated_at\x18\r \x01(\x12R\tupdatedAt\x12\x1c\n\tdirection\x18\x0e \x01(\tR\tdirection\x12\x17\n\x07tx_hash\x18\x0f \x01(\tR\x06txHash\x12\x10\n\x03\x63id\x18\x10 \x01(\tR\x03\x63id\"\xdc\x01\n\x1aStreamOrdersHistoryRequest\x12#\n\rsubaccount_id\x18\x01 \x01(\tR\x0csubaccountId\x12\x1b\n\tmarket_id\x18\x02 \x01(\tR\x08marketId\x12\x1f\n\x0border_types\x18\x03 \x03(\tR\norderTypes\x12\x1c\n\tdirection\x18\x04 \x01(\tR\tdirection\x12\x14\n\x05state\x18\x05 \x01(\tR\x05state\x12\'\n\x0f\x65xecution_types\x18\x06 \x03(\tR\x0e\x65xecutionTypes\"\xa7\x01\n\x1bStreamOrdersHistoryResponse\x12\x43\n\x05order\x18\x01 \x01(\x0b\x32-.injective_spot_exchange_rpc.SpotOrderHistoryR\x05order\x12%\n\x0eoperation_type\x18\x02 \x01(\tR\roperationType\x12\x1c\n\ttimestamp\x18\x03 \x01(\x12R\ttimestamp\"\xc7\x01\n\x18\x41tomicSwapHistoryRequest\x12\x18\n\x07\x61\x64\x64ress\x18\x01 \x01(\tR\x07\x61\x64\x64ress\x12)\n\x10\x63ontract_address\x18\x02 \x01(\tR\x0f\x63ontractAddress\x12\x12\n\x04skip\x18\x03 \x01(\x11R\x04skip\x12\x14\n\x05limit\x18\x04 \x01(\x11R\x05limit\x12\x1f\n\x0b\x66rom_number\x18\x05 \x01(\x11R\nfromNumber\x12\x1b\n\tto_number\x18\x06 \x01(\x11R\x08toNumber\"\x95\x01\n\x19\x41tomicSwapHistoryResponse\x12;\n\x06paging\x18\x01 \x01(\x0b\x32#.injective_spot_exchange_rpc.PagingR\x06paging\x12;\n\x04\x64\x61ta\x18\x02 \x03(\x0b\x32\'.injective_spot_exchange_rpc.AtomicSwapR\x04\x64\x61ta\"\xe0\x03\n\nAtomicSwap\x12\x16\n\x06sender\x18\x01 \x01(\tR\x06sender\x12\x14\n\x05route\x18\x02 \x01(\tR\x05route\x12\x42\n\x0bsource_coin\x18\x03 \x01(\x0b\x32!.injective_spot_exchange_rpc.CoinR\nsourceCoin\x12>\n\tdest_coin\x18\x04 \x01(\x0b\x32!.injective_spot_exchange_rpc.CoinR\x08\x64\x65stCoin\x12\x35\n\x04\x66\x65\x65s\x18\x05 \x03(\x0b\x32!.injective_spot_exchange_rpc.CoinR\x04\x66\x65\x65s\x12)\n\x10\x63ontract_address\x18\x06 \x01(\tR\x0f\x63ontractAddress\x12&\n\x0findex_by_sender\x18\x07 \x01(\x11R\rindexBySender\x12\x37\n\x18index_by_sender_contract\x18\x08 \x01(\x11R\x15indexBySenderContract\x12\x17\n\x07tx_hash\x18\t \x01(\tR\x06txHash\x12\x1f\n\x0b\x65xecuted_at\x18\n \x01(\x12R\nexecutedAt\x12#\n\rrefund_amount\x18\x0b \x01(\tR\x0crefundAmount\"4\n\x04\x43oin\x12\x14\n\x05\x64\x65nom\x18\x01 \x01(\tR\x05\x64\x65nom\x12\x16\n\x06\x61mount\x18\x02 \x01(\tR\x06\x61mount2\x9e\x11\n\x18InjectiveSpotExchangeRPC\x12\x64\n\x07Markets\x12+.injective_spot_exchange_rpc.MarketsRequest\x1a,.injective_spot_exchange_rpc.MarketsResponse\x12\x61\n\x06Market\x12*.injective_spot_exchange_rpc.MarketRequest\x1a+.injective_spot_exchange_rpc.MarketResponse\x12x\n\rStreamMarkets\x12\x31.injective_spot_exchange_rpc.StreamMarketsRequest\x1a\x32.injective_spot_exchange_rpc.StreamMarketsResponse0\x01\x12p\n\x0bOrderbookV2\x12/.injective_spot_exchange_rpc.OrderbookV2Request\x1a\x30.injective_spot_exchange_rpc.OrderbookV2Response\x12s\n\x0cOrderbooksV2\x12\x30.injective_spot_exchange_rpc.OrderbooksV2Request\x1a\x31.injective_spot_exchange_rpc.OrderbooksV2Response\x12\x84\x01\n\x11StreamOrderbookV2\x12\x35.injective_spot_exchange_rpc.StreamOrderbookV2Request\x1a\x36.injective_spot_exchange_rpc.StreamOrderbookV2Response0\x01\x12\x90\x01\n\x15StreamOrderbookUpdate\x12\x39.injective_spot_exchange_rpc.StreamOrderbookUpdateRequest\x1a:.injective_spot_exchange_rpc.StreamOrderbookUpdateResponse0\x01\x12\x61\n\x06Orders\x12*.injective_spot_exchange_rpc.OrdersRequest\x1a+.injective_spot_exchange_rpc.OrdersResponse\x12u\n\x0cStreamOrders\x12\x30.injective_spot_exchange_rpc.StreamOrdersRequest\x1a\x31.injective_spot_exchange_rpc.StreamOrdersResponse0\x01\x12\x61\n\x06Trades\x12*.injective_spot_exchange_rpc.TradesRequest\x1a+.injective_spot_exchange_rpc.TradesResponse\x12u\n\x0cStreamTrades\x12\x30.injective_spot_exchange_rpc.StreamTradesRequest\x1a\x31.injective_spot_exchange_rpc.StreamTradesResponse0\x01\x12g\n\x08TradesV2\x12,.injective_spot_exchange_rpc.TradesV2Request\x1a-.injective_spot_exchange_rpc.TradesV2Response\x12{\n\x0eStreamTradesV2\x12\x32.injective_spot_exchange_rpc.StreamTradesV2Request\x1a\x33.injective_spot_exchange_rpc.StreamTradesV2Response0\x01\x12\x8b\x01\n\x14SubaccountOrdersList\x12\x38.injective_spot_exchange_rpc.SubaccountOrdersListRequest\x1a\x39.injective_spot_exchange_rpc.SubaccountOrdersListResponse\x12\x8b\x01\n\x14SubaccountTradesList\x12\x38.injective_spot_exchange_rpc.SubaccountTradesListRequest\x1a\x39.injective_spot_exchange_rpc.SubaccountTradesListResponse\x12v\n\rOrdersHistory\x12\x31.injective_spot_exchange_rpc.OrdersHistoryRequest\x1a\x32.injective_spot_exchange_rpc.OrdersHistoryResponse\x12\x8a\x01\n\x13StreamOrdersHistory\x12\x37.injective_spot_exchange_rpc.StreamOrdersHistoryRequest\x1a\x38.injective_spot_exchange_rpc.StreamOrdersHistoryResponse0\x01\x12\x82\x01\n\x11\x41tomicSwapHistory\x12\x35.injective_spot_exchange_rpc.AtomicSwapHistoryRequest\x1a\x36.injective_spot_exchange_rpc.AtomicSwapHistoryResponseB\xe0\x01\n\x1f\x63om.injective_spot_exchange_rpcB\x1dInjectiveSpotExchangeRpcProtoP\x01Z\x1e/injective_spot_exchange_rpcpb\xa2\x02\x03IXX\xaa\x02\x18InjectiveSpotExchangeRpc\xca\x02\x18InjectiveSpotExchangeRpc\xe2\x02$InjectiveSpotExchangeRpc\\GPBMetadata\xea\x02\x18InjectiveSpotExchangeRpcb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'exchange.injective_spot_exchange_rpc_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'\n\037com.injective_spot_exchange_rpcB\035InjectiveSpotExchangeRpcProtoP\001Z\036/injective_spot_exchange_rpcpb\242\002\003IXX\252\002\030InjectiveSpotExchangeRpc\312\002\030InjectiveSpotExchangeRpc\342\002$InjectiveSpotExchangeRpc\\GPBMetadata\352\002\030InjectiveSpotExchangeRpc'
  _globals['_MARKETSREQUEST']._serialized_start=76
  _globals['_MARKETSREQUEST']._serialized_end=234
  _globals['_MARKETSRESPONSE']._serialized_start=236
  _globals['_MARKETSRESPONSE']._serialized_end=324
  _globals['_SPOTMARKETINFO']._serialized_start=327
  _globals['_SPOTMARKETINFO']._serialized_end=920
  _globals['_TOKENMETA']._serialized_start=923
  _globals['_TOKENMETA']._serialized_end=1083
  _globals['_MARKETREQUEST']._serialized_start=1085
  _globals['_MARKETREQUEST']._serialized_end=1129
  _globals['_MARKETRESPONSE']._serialized_start=1131
  _globals['_MARKETRESPONSE']._serialized_end=1216
  _globals['_STREAMMARKETSREQUEST']._serialized_start=1218
  _globals['_STREAMMARKETSREQUEST']._serialized_end=1271
  _globals['_STREAMMARKETSRESPONSE']._serialized_start=1274
  _globals['_STREAMMARKETSRESPONSE']._serialized_end=1435
  _globals['_ORDERBOOKV2REQUEST']._serialized_start=1437
  _globals['_ORDERBOOKV2REQUEST']._serialized_end=1486
  _globals['_ORDERBOOKV2RESPONSE']._serialized_start=1488
  _globals['_ORDERBOOKV2RESPONSE']._serialized_end=1590
  _globals['_SPOTLIMITORDERBOOKV2']._serialized_start=1593
  _globals['_SPOTLIMITORDERBOOKV2']._serialized_end=1797
  _globals['_PRICELEVEL']._serialized_start=1799
  _globals['_PRICELEVEL']._serialized_end=1891
  _globals['_ORDERBOOKSV2REQUEST']._serialized_start=1893
  _globals['_ORDERBOOKSV2REQUEST']._serialized_end=1945
  _globals['_ORDERBOOKSV2RESPONSE']._serialized_start=1947
  _globals['_ORDERBOOKSV2RESPONSE']._serialized_end=2058
  _globals['_SINGLESPOTLIMITORDERBOOKV2']._serialized_start=2061
  _globals['_SINGLESPOTLIMITORDERBOOKV2']._serialized_end=2199
  _globals['_STREAMORDERBOOKV2REQUEST']._serialized_start=2201
  _globals['_STREAMORDERBOOKV2REQUEST']._serialized_end=2258
  _globals['_STREAMORDERBOOKV2RESPONSE']._serialized_start=2261
  _globals['_STREAMORDERBOOKV2RESPONSE']._serialized_end=2467
  _globals['_STREAMORDERBOOKUPDATEREQUEST']._serialized_start=2469
  _globals['_STREAMORDERBOOKUPDATEREQUEST']._serialized_end=2530
  _globals['_STREAMORDERBOOKUPDATERESPONSE']._serialized_start=2533
  _globals['_STREAMORDERBOOKUPDATERESPONSE']._serialized_end=2770
  _globals['_ORDERBOOKLEVELUPDATES']._serialized_start=2773
  _globals['_ORDERBOOKLEVELUPDATES']._serialized_end=3020
  _globals['_PRICELEVELUPDATE']._serialized_start=3022
  _globals['_PRICELEVELUPDATE']._serialized_end=3149
  _globals['_ORDERSREQUEST']._serialized_start=3152
  _globals['_ORDERSREQUEST']._serialized_end=3539
  _globals['_ORDERSRESPONSE']._serialized_start=3542
  _globals['_ORDERSRESPONSE']._serialized_end=3688
  _globals['_SPOTLIMITORDER']._serialized_start=3691
  _globals['_SPOTLIMITORDER']._serialized_end=4131
  _globals['_PAGING']._serialized_start=4134
  _globals['_PAGING']._serialized_end=4268
  _globals['_STREAMORDERSREQUEST']._serialized_start=4271
  _globals['_STREAMORDERSREQUEST']._serialized_end=4664
  _globals['_STREAMORDERSRESPONSE']._serialized_start=4667
  _globals['_STREAMORDERSRESPONSE']._serialized_end=4825
  _globals['_TRADESREQUEST']._serialized_start=4828
  _globals['_TRADESREQUEST']._serialized_end=5275
  _globals['_TRADESRESPONSE']._serialized_start=5278
  _globals['_TRADESRESPONSE']._serialized_end=5419
  _globals['_SPOTTRADE']._serialized_start=5422
  _globals['_SPOTTRADE']._serialized_end=5856
  _globals['_STREAMTRADESREQUEST']._serialized_start=5859
  _globals['_STREAMTRADESREQUEST']._serialized_end=6312
  _globals['_STREAMTRADESRESPONSE']._serialized_start=6315
  _globals['_STREAMTRADESRESPONSE']._serialized_end=6468
  _globals['_TRADESV2REQUEST']._serialized_start=6471
  _globals['_TRADESV2REQUEST']._serialized_end=6920
  _globals['_TRADESV2RESPONSE']._serialized_start=6923
  _globals['_TRADESV2RESPONSE']._serialized_end=7066
  _globals['_STREAMTRADESV2REQUEST']._serialized_start=7069
  _globals['_STREAMTRADESV2REQUEST']._serialized_end=7524
  _globals['_STREAMTRADESV2RESPONSE']._serialized_start=7527
  _globals['_STREAMTRADESV2RESPONSE']._serialized_end=7682
  _globals['_SUBACCOUNTORDERSLISTREQUEST']._serialized_start=7685
  _globals['_SUBACCOUNTORDERSLISTREQUEST']._serialized_end=7822
  _globals['_SUBACCOUNTORDERSLISTRESPONSE']._serialized_start=7825
  _globals['_SUBACCOUNTORDERSLISTRESPONSE']._serialized_end=7985
  _globals['_SUBACCOUNTTRADESLISTREQUEST']._serialized_start=7988
  _globals['_SUBACCOUNTTRADESLISTREQUEST']._serialized_end=8194
  _globals['_SUBACCOUNTTRADESLISTRESPONSE']._serialized_start=8196
  _globals['_SUBACCOUNTTRADESLISTRESPONSE']._serialized_end=8290
  _globals['_ORDERSHISTORYREQUEST']._serialized_start=8293
  _globals['_ORDERSHISTORYREQUEST']._serialized_end=8731
  _globals['_ORDERSHISTORYRESPONSE']._serialized_start=8734
  _globals['_ORDERSHISTORYRESPONSE']._serialized_end=8889
  _globals['_SPOTORDERHISTORY']._serialized_start=8892
  _globals['_SPOTORDERHISTORY']._serialized_end=9391
  _globals['_STREAMORDERSHISTORYREQUEST']._serialized_start=9394
  _globals['_STREAMORDERSHISTORYREQUEST']._serialized_end=9614
  _globals['_STREAMORDERSHISTORYRESPONSE']._serialized_start=9617
  _globals['_STREAMORDERSHISTORYRESPONSE']._serialized_end=9784
  _globals['_ATOMICSWAPHISTORYREQUEST']._serialized_start=9787
  _globals['_ATOMICSWAPHISTORYREQUEST']._serialized_end=9986
  _globals['_ATOMICSWAPHISTORYRESPONSE']._serialized_start=9989
  _globals['_ATOMICSWAPHISTORYRESPONSE']._serialized_end=10138
  _globals['_ATOMICSWAP']._serialized_start=10141
  _globals['_ATOMICSWAP']._serialized_end=10621
  _globals['_COIN']._serialized_start=10623
  _globals['_COIN']._serialized_end=10675
  _globals['_INJECTIVESPOTEXCHANGERPC']._serialized_start=10678
  _globals['_INJECTIVESPOTEXCHANGERPC']._serialized_end=12884
# @@protoc_insertion_point(module_scope)
