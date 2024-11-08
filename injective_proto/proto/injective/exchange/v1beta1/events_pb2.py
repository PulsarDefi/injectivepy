from injective_proto.proto.descriptor import INJECTIVE_DESCRIPTOR_POOL
# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: injective/exchange/v1beta1/events.proto
# Protobuf Python Version: 5.26.1
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from injective_proto.proto.gogoproto import gogo_pb2 as gogoproto_dot_gogo__pb2
from injective_proto.proto.cosmos.base.v1beta1 import coin_pb2 as cosmos_dot_base_dot_v1beta1_dot_coin__pb2
from injective_proto.proto.injective.oracle.v1beta1 import oracle_pb2 as injective_dot_oracle_dot_v1beta1_dot_oracle__pb2
from injective_proto.proto.injective.exchange.v1beta1 import exchange_pb2 as injective_dot_exchange_dot_v1beta1_dot_exchange__pb2


DESCRIPTOR = INJECTIVE_DESCRIPTOR_POOL.AddSerializedFile(b'\n\'injective/exchange/v1beta1/events.proto\x12\x1ainjective.exchange.v1beta1\x1a\x14gogoproto/gogo.proto\x1a\x1e\x63osmos/base/v1beta1/coin.proto\x1a%injective/oracle/v1beta1/oracle.proto\x1a)injective/exchange/v1beta1/exchange.proto\"\xdc\x01\n\x17\x45ventBatchSpotExecution\x12\x1b\n\tmarket_id\x18\x01 \x01(\tR\x08marketId\x12\x15\n\x06is_buy\x18\x02 \x01(\x08R\x05isBuy\x12O\n\rexecutionType\x18\x03 \x01(\x0e\x32).injective.exchange.v1beta1.ExecutionTypeR\rexecutionType\x12<\n\x06trades\x18\x04 \x03(\x0b\x32$.injective.exchange.v1beta1.TradeLogR\x06trades\"\xe7\x02\n\x1d\x45ventBatchDerivativeExecution\x12\x1b\n\tmarket_id\x18\x01 \x01(\tR\x08marketId\x12\x15\n\x06is_buy\x18\x02 \x01(\x08R\x05isBuy\x12%\n\x0eis_liquidation\x18\x03 \x01(\x08R\risLiquidation\x12R\n\x12\x63umulative_funding\x18\x04 \x01(\tB#\xc8\xde\x1f\x01\xda\xde\x1f\x1b\x63osmossdk.io/math.LegacyDecR\x11\x63umulativeFunding\x12O\n\rexecutionType\x18\x05 \x01(\x0e\x32).injective.exchange.v1beta1.ExecutionTypeR\rexecutionType\x12\x46\n\x06trades\x18\x06 \x03(\x0b\x32..injective.exchange.v1beta1.DerivativeTradeLogR\x06trades\"\xc2\x02\n\x1d\x45ventLostFundsFromLiquidation\x12\x1b\n\tmarket_id\x18\x01 \x01(\tR\x08marketId\x12#\n\rsubaccount_id\x18\x02 \x01(\x0cR\x0csubaccountId\x12x\n\'lost_funds_from_available_during_payout\x18\x03 \x01(\tB#\xc8\xde\x1f\x00\xda\xde\x1f\x1b\x63osmossdk.io/math.LegacyDecR\"lostFundsFromAvailableDuringPayout\x12\x65\n\x1dlost_funds_from_order_cancels\x18\x04 \x01(\tB#\xc8\xde\x1f\x00\xda\xde\x1f\x1b\x63osmossdk.io/math.LegacyDecR\x19lostFundsFromOrderCancels\"\x89\x01\n\x1c\x45ventBatchDerivativePosition\x12\x1b\n\tmarket_id\x18\x01 \x01(\tR\x08marketId\x12L\n\tpositions\x18\x02 \x03(\x0b\x32..injective.exchange.v1beta1.SubaccountPositionR\tpositions\"\xbb\x01\n\x1b\x45ventDerivativeMarketPaused\x12\x1b\n\tmarket_id\x18\x01 \x01(\tR\x08marketId\x12!\n\x0csettle_price\x18\x02 \x01(\tR\x0bsettlePrice\x12.\n\x13total_missing_funds\x18\x03 \x01(\tR\x11totalMissingFunds\x12,\n\x12missing_funds_rate\x18\x04 \x01(\tR\x10missingFundsRate\"\x8f\x01\n\x1b\x45ventMarketBeyondBankruptcy\x12\x1b\n\tmarket_id\x18\x01 \x01(\tR\x08marketId\x12!\n\x0csettle_price\x18\x02 \x01(\tR\x0bsettlePrice\x12\x30\n\x14missing_market_funds\x18\x03 \x01(\tR\x12missingMarketFunds\"\x88\x01\n\x18\x45ventAllPositionsHaircut\x12\x1b\n\tmarket_id\x18\x01 \x01(\tR\x08marketId\x12!\n\x0csettle_price\x18\x02 \x01(\tR\x0bsettlePrice\x12,\n\x12missing_funds_rate\x18\x03 \x01(\tR\x10missingFundsRate\"o\n\x1e\x45ventBinaryOptionsMarketUpdate\x12M\n\x06market\x18\x01 \x01(\x0b\x32/.injective.exchange.v1beta1.BinaryOptionsMarketB\x04\xc8\xde\x1f\x00R\x06market\"\xc9\x01\n\x12\x45ventNewSpotOrders\x12\x1b\n\tmarket_id\x18\x01 \x01(\tR\x08marketId\x12I\n\nbuy_orders\x18\x02 \x03(\x0b\x32*.injective.exchange.v1beta1.SpotLimitOrderR\tbuyOrders\x12K\n\x0bsell_orders\x18\x03 \x03(\x0b\x32*.injective.exchange.v1beta1.SpotLimitOrderR\nsellOrders\"\xdb\x01\n\x18\x45ventNewDerivativeOrders\x12\x1b\n\tmarket_id\x18\x01 \x01(\tR\x08marketId\x12O\n\nbuy_orders\x18\x02 \x03(\x0b\x32\x30.injective.exchange.v1beta1.DerivativeLimitOrderR\tbuyOrders\x12Q\n\x0bsell_orders\x18\x03 \x03(\x0b\x32\x30.injective.exchange.v1beta1.DerivativeLimitOrderR\nsellOrders\"{\n\x14\x45ventCancelSpotOrder\x12\x1b\n\tmarket_id\x18\x01 \x01(\tR\x08marketId\x12\x46\n\x05order\x18\x02 \x01(\x0b\x32*.injective.exchange.v1beta1.SpotLimitOrderB\x04\xc8\xde\x1f\x00R\x05order\"]\n\x15\x45ventSpotMarketUpdate\x12\x44\n\x06market\x18\x01 \x01(\x0b\x32&.injective.exchange.v1beta1.SpotMarketB\x04\xc8\xde\x1f\x00R\x06market\"\xa7\x02\n\x1a\x45ventPerpetualMarketUpdate\x12J\n\x06market\x18\x01 \x01(\x0b\x32,.injective.exchange.v1beta1.DerivativeMarketB\x04\xc8\xde\x1f\x00R\x06market\x12i\n\x15perpetual_market_info\x18\x02 \x01(\x0b\x32/.injective.exchange.v1beta1.PerpetualMarketInfoB\x04\xc8\xde\x1f\x01R\x13perpetualMarketInfo\x12R\n\x07\x66unding\x18\x03 \x01(\x0b\x32\x32.injective.exchange.v1beta1.PerpetualMarketFundingB\x04\xc8\xde\x1f\x01R\x07\x66unding\"\xe4\x01\n\x1e\x45ventExpiryFuturesMarketUpdate\x12J\n\x06market\x18\x01 \x01(\x0b\x32,.injective.exchange.v1beta1.DerivativeMarketB\x04\xc8\xde\x1f\x00R\x06market\x12v\n\x1a\x65xpiry_futures_market_info\x18\x03 \x01(\x0b\x32\x33.injective.exchange.v1beta1.ExpiryFuturesMarketInfoB\x04\xc8\xde\x1f\x01R\x17\x65xpiryFuturesMarketInfo\"\xcc\x02\n!EventPerpetualMarketFundingUpdate\x12\x1b\n\tmarket_id\x18\x01 \x01(\tR\x08marketId\x12R\n\x07\x66unding\x18\x02 \x01(\x0b\x32\x32.injective.exchange.v1beta1.PerpetualMarketFundingB\x04\xc8\xde\x1f\x00R\x07\x66unding\x12*\n\x11is_hourly_funding\x18\x03 \x01(\x08R\x0fisHourlyFunding\x12\x46\n\x0c\x66unding_rate\x18\x04 \x01(\tB#\xc8\xde\x1f\x01\xda\xde\x1f\x1b\x63osmossdk.io/math.LegacyDecR\x0b\x66undingRate\x12\x42\n\nmark_price\x18\x05 \x01(\tB#\xc8\xde\x1f\x01\xda\xde\x1f\x1b\x63osmossdk.io/math.LegacyDecR\tmarkPrice\"\x97\x01\n\x16\x45ventSubaccountDeposit\x12\x1f\n\x0bsrc_address\x18\x01 \x01(\tR\nsrcAddress\x12#\n\rsubaccount_id\x18\x02 \x01(\x0cR\x0csubaccountId\x12\x37\n\x06\x61mount\x18\x03 \x01(\x0b\x32\x19.cosmos.base.v1beta1.CoinB\x04\xc8\xde\x1f\x00R\x06\x61mount\"\x98\x01\n\x17\x45ventSubaccountWithdraw\x12#\n\rsubaccount_id\x18\x01 \x01(\x0cR\x0csubaccountId\x12\x1f\n\x0b\x64st_address\x18\x02 \x01(\tR\ndstAddress\x12\x37\n\x06\x61mount\x18\x03 \x01(\x0b\x32\x19.cosmos.base.v1beta1.CoinB\x04\xc8\xde\x1f\x00R\x06\x61mount\"\xb1\x01\n\x1e\x45ventSubaccountBalanceTransfer\x12*\n\x11src_subaccount_id\x18\x01 \x01(\tR\x0fsrcSubaccountId\x12*\n\x11\x64st_subaccount_id\x18\x02 \x01(\tR\x0f\x64stSubaccountId\x12\x37\n\x06\x61mount\x18\x03 \x01(\x0b\x32\x19.cosmos.base.v1beta1.CoinB\x04\xc8\xde\x1f\x00R\x06\x61mount\"m\n\x17\x45ventBatchDepositUpdate\x12R\n\x0f\x64\x65posit_updates\x18\x01 \x03(\x0b\x32).injective.exchange.v1beta1.DepositUpdateR\x0e\x64\x65positUpdates\"\xc7\x01\n\x1b\x44\x65rivativeMarketOrderCancel\x12Z\n\x0cmarket_order\x18\x01 \x01(\x0b\x32\x31.injective.exchange.v1beta1.DerivativeMarketOrderB\x04\xc8\xde\x1f\x01R\x0bmarketOrder\x12L\n\x0f\x63\x61ncel_quantity\x18\x02 \x01(\tB#\xc8\xde\x1f\x00\xda\xde\x1f\x1b\x63osmossdk.io/math.LegacyDecR\x0e\x63\x61ncelQuantity\"\xa7\x02\n\x1a\x45ventCancelDerivativeOrder\x12\x1b\n\tmarket_id\x18\x01 \x01(\tR\x08marketId\x12$\n\risLimitCancel\x18\x02 \x01(\x08R\risLimitCancel\x12W\n\x0blimit_order\x18\x03 \x01(\x0b\x32\x30.injective.exchange.v1beta1.DerivativeLimitOrderB\x04\xc8\xde\x1f\x01R\nlimitOrder\x12m\n\x13market_order_cancel\x18\x04 \x01(\x0b\x32\x37.injective.exchange.v1beta1.DerivativeMarketOrderCancelB\x04\xc8\xde\x1f\x01R\x11marketOrderCancel\"g\n\x18\x45ventFeeDiscountSchedule\x12K\n\x08schedule\x18\x01 \x01(\x0b\x32/.injective.exchange.v1beta1.FeeDiscountScheduleR\x08schedule\"\xe2\x01\n EventTradingRewardCampaignUpdate\x12Z\n\rcampaign_info\x18\x01 \x01(\x0b\x32\x35.injective.exchange.v1beta1.TradingRewardCampaignInfoR\x0c\x63\x61mpaignInfo\x12\x62\n\x15\x63\x61mpaign_reward_pools\x18\x02 \x03(\x0b\x32..injective.exchange.v1beta1.CampaignRewardPoolR\x13\x63\x61mpaignRewardPools\"u\n\x1e\x45ventTradingRewardDistribution\x12S\n\x0f\x61\x63\x63ount_rewards\x18\x01 \x03(\x0b\x32*.injective.exchange.v1beta1.AccountRewardsR\x0e\x61\x63\x63ountRewards\"\xb5\x01\n\"EventNewConditionalDerivativeOrder\x12\x1b\n\tmarket_id\x18\x01 \x01(\tR\x08marketId\x12\x41\n\x05order\x18\x02 \x01(\x0b\x32+.injective.exchange.v1beta1.DerivativeOrderR\x05order\x12\x12\n\x04hash\x18\x03 \x01(\x0cR\x04hash\x12\x1b\n\tis_market\x18\x04 \x01(\x08R\x08isMarket\"\x9f\x02\n%EventCancelConditionalDerivativeOrder\x12\x1b\n\tmarket_id\x18\x01 \x01(\tR\x08marketId\x12$\n\risLimitCancel\x18\x02 \x01(\x08R\risLimitCancel\x12W\n\x0blimit_order\x18\x03 \x01(\x0b\x32\x30.injective.exchange.v1beta1.DerivativeLimitOrderB\x04\xc8\xde\x1f\x01R\nlimitOrder\x12Z\n\x0cmarket_order\x18\x04 \x01(\x0b\x32\x31.injective.exchange.v1beta1.DerivativeMarketOrderB\x04\xc8\xde\x1f\x01R\x0bmarketOrder\"\xfb\x01\n&EventConditionalDerivativeOrderTrigger\x12\x1b\n\tmarket_id\x18\x01 \x01(\x0cR\x08marketId\x12&\n\x0eisLimitTrigger\x18\x02 \x01(\x08R\x0eisLimitTrigger\x12\x30\n\x14triggered_order_hash\x18\x03 \x01(\x0cR\x12triggeredOrderHash\x12*\n\x11placed_order_hash\x18\x04 \x01(\x0cR\x0fplacedOrderHash\x12.\n\x13triggered_order_cid\x18\x05 \x01(\tR\x11triggeredOrderCid\"l\n\x0e\x45ventOrderFail\x12\x18\n\x07\x61\x63\x63ount\x18\x01 \x01(\x0cR\x07\x61\x63\x63ount\x12\x16\n\x06hashes\x18\x02 \x03(\x0cR\x06hashes\x12\x14\n\x05\x66lags\x18\x03 \x03(\rR\x05\x66lags\x12\x12\n\x04\x63ids\x18\x04 \x03(\tR\x04\x63ids\"\x94\x01\n+EventAtomicMarketOrderFeeMultipliersUpdated\x12\x65\n\x16market_fee_multipliers\x18\x01 \x03(\x0b\x32/.injective.exchange.v1beta1.MarketFeeMultiplierR\x14marketFeeMultipliers\"\xc2\x01\n\x14\x45ventOrderbookUpdate\x12N\n\x0cspot_updates\x18\x01 \x03(\x0b\x32+.injective.exchange.v1beta1.OrderbookUpdateR\x0bspotUpdates\x12Z\n\x12\x64\x65rivative_updates\x18\x02 \x03(\x0b\x32+.injective.exchange.v1beta1.OrderbookUpdateR\x11\x64\x65rivativeUpdates\"h\n\x0fOrderbookUpdate\x12\x10\n\x03seq\x18\x01 \x01(\x04R\x03seq\x12\x43\n\torderbook\x18\x02 \x01(\x0b\x32%.injective.exchange.v1beta1.OrderbookR\torderbook\"\xae\x01\n\tOrderbook\x12\x1b\n\tmarket_id\x18\x01 \x01(\x0cR\x08marketId\x12@\n\nbuy_levels\x18\x02 \x03(\x0b\x32!.injective.exchange.v1beta1.LevelR\tbuyLevels\x12\x42\n\x0bsell_levels\x18\x03 \x03(\x0b\x32!.injective.exchange.v1beta1.LevelR\nsellLevels\"|\n\x18\x45ventGrantAuthorizations\x12\x18\n\x07granter\x18\x01 \x01(\tR\x07granter\x12\x46\n\x06grants\x18\x02 \x03(\x0b\x32..injective.exchange.v1beta1.GrantAuthorizationR\x06grants\"\x81\x01\n\x14\x45ventGrantActivation\x12\x18\n\x07grantee\x18\x01 \x01(\tR\x07grantee\x12\x18\n\x07granter\x18\x02 \x01(\tR\x07granter\x12\x35\n\x06\x61mount\x18\x03 \x01(\tB\x1d\xc8\xde\x1f\x00\xda\xde\x1f\x15\x63osmossdk.io/math.IntR\x06\x61mount\"G\n\x11\x45ventInvalidGrant\x12\x18\n\x07grantee\x18\x01 \x01(\tR\x07grantee\x12\x18\n\x07granter\x18\x02 \x01(\tR\x07granter\"\xab\x01\n\x14\x45ventOrderCancelFail\x12\x1b\n\tmarket_id\x18\x01 \x01(\tR\x08marketId\x12#\n\rsubaccount_id\x18\x02 \x01(\tR\x0csubaccountId\x12\x1d\n\norder_hash\x18\x03 \x01(\tR\torderHash\x12\x10\n\x03\x63id\x18\x04 \x01(\tR\x03\x63id\x12 \n\x0b\x64\x65scription\x18\x05 \x01(\tR\x0b\x64\x65scriptionB\x87\x02\n\x1e\x63om.injective.exchange.v1beta1B\x0b\x45ventsProtoP\x01ZNgithub.com/InjectiveLabs/injective-core/injective-chain/modules/exchange/types\xa2\x02\x03IEX\xaa\x02\x1aInjective.Exchange.V1beta1\xca\x02\x1aInjective\\Exchange\\V1beta1\xe2\x02&Injective\\Exchange\\V1beta1\\GPBMetadata\xea\x02\x1cInjective::Exchange::V1beta1b\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'injective.exchange.v1beta1.events_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'\n\036com.injective.exchange.v1beta1B\013EventsProtoP\001ZNgithub.com/InjectiveLabs/injective-core/injective-chain/modules/exchange/types\242\002\003IEX\252\002\032Injective.Exchange.V1beta1\312\002\032Injective\\Exchange\\V1beta1\342\002&Injective\\Exchange\\V1beta1\\GPBMetadata\352\002\034Injective::Exchange::V1beta1'
  _globals['_EVENTBATCHDERIVATIVEEXECUTION'].fields_by_name['cumulative_funding']._loaded_options = None
  _globals['_EVENTBATCHDERIVATIVEEXECUTION'].fields_by_name['cumulative_funding']._serialized_options = b'\310\336\037\001\332\336\037\033cosmossdk.io/math.LegacyDec'
  _globals['_EVENTLOSTFUNDSFROMLIQUIDATION'].fields_by_name['lost_funds_from_available_during_payout']._loaded_options = None
  _globals['_EVENTLOSTFUNDSFROMLIQUIDATION'].fields_by_name['lost_funds_from_available_during_payout']._serialized_options = b'\310\336\037\000\332\336\037\033cosmossdk.io/math.LegacyDec'
  _globals['_EVENTLOSTFUNDSFROMLIQUIDATION'].fields_by_name['lost_funds_from_order_cancels']._loaded_options = None
  _globals['_EVENTLOSTFUNDSFROMLIQUIDATION'].fields_by_name['lost_funds_from_order_cancels']._serialized_options = b'\310\336\037\000\332\336\037\033cosmossdk.io/math.LegacyDec'
  _globals['_EVENTBINARYOPTIONSMARKETUPDATE'].fields_by_name['market']._loaded_options = None
  _globals['_EVENTBINARYOPTIONSMARKETUPDATE'].fields_by_name['market']._serialized_options = b'\310\336\037\000'
  _globals['_EVENTCANCELSPOTORDER'].fields_by_name['order']._loaded_options = None
  _globals['_EVENTCANCELSPOTORDER'].fields_by_name['order']._serialized_options = b'\310\336\037\000'
  _globals['_EVENTSPOTMARKETUPDATE'].fields_by_name['market']._loaded_options = None
  _globals['_EVENTSPOTMARKETUPDATE'].fields_by_name['market']._serialized_options = b'\310\336\037\000'
  _globals['_EVENTPERPETUALMARKETUPDATE'].fields_by_name['market']._loaded_options = None
  _globals['_EVENTPERPETUALMARKETUPDATE'].fields_by_name['market']._serialized_options = b'\310\336\037\000'
  _globals['_EVENTPERPETUALMARKETUPDATE'].fields_by_name['perpetual_market_info']._loaded_options = None
  _globals['_EVENTPERPETUALMARKETUPDATE'].fields_by_name['perpetual_market_info']._serialized_options = b'\310\336\037\001'
  _globals['_EVENTPERPETUALMARKETUPDATE'].fields_by_name['funding']._loaded_options = None
  _globals['_EVENTPERPETUALMARKETUPDATE'].fields_by_name['funding']._serialized_options = b'\310\336\037\001'
  _globals['_EVENTEXPIRYFUTURESMARKETUPDATE'].fields_by_name['market']._loaded_options = None
  _globals['_EVENTEXPIRYFUTURESMARKETUPDATE'].fields_by_name['market']._serialized_options = b'\310\336\037\000'
  _globals['_EVENTEXPIRYFUTURESMARKETUPDATE'].fields_by_name['expiry_futures_market_info']._loaded_options = None
  _globals['_EVENTEXPIRYFUTURESMARKETUPDATE'].fields_by_name['expiry_futures_market_info']._serialized_options = b'\310\336\037\001'
  _globals['_EVENTPERPETUALMARKETFUNDINGUPDATE'].fields_by_name['funding']._loaded_options = None
  _globals['_EVENTPERPETUALMARKETFUNDINGUPDATE'].fields_by_name['funding']._serialized_options = b'\310\336\037\000'
  _globals['_EVENTPERPETUALMARKETFUNDINGUPDATE'].fields_by_name['funding_rate']._loaded_options = None
  _globals['_EVENTPERPETUALMARKETFUNDINGUPDATE'].fields_by_name['funding_rate']._serialized_options = b'\310\336\037\001\332\336\037\033cosmossdk.io/math.LegacyDec'
  _globals['_EVENTPERPETUALMARKETFUNDINGUPDATE'].fields_by_name['mark_price']._loaded_options = None
  _globals['_EVENTPERPETUALMARKETFUNDINGUPDATE'].fields_by_name['mark_price']._serialized_options = b'\310\336\037\001\332\336\037\033cosmossdk.io/math.LegacyDec'
  _globals['_EVENTSUBACCOUNTDEPOSIT'].fields_by_name['amount']._loaded_options = None
  _globals['_EVENTSUBACCOUNTDEPOSIT'].fields_by_name['amount']._serialized_options = b'\310\336\037\000'
  _globals['_EVENTSUBACCOUNTWITHDRAW'].fields_by_name['amount']._loaded_options = None
  _globals['_EVENTSUBACCOUNTWITHDRAW'].fields_by_name['amount']._serialized_options = b'\310\336\037\000'
  _globals['_EVENTSUBACCOUNTBALANCETRANSFER'].fields_by_name['amount']._loaded_options = None
  _globals['_EVENTSUBACCOUNTBALANCETRANSFER'].fields_by_name['amount']._serialized_options = b'\310\336\037\000'
  _globals['_DERIVATIVEMARKETORDERCANCEL'].fields_by_name['market_order']._loaded_options = None
  _globals['_DERIVATIVEMARKETORDERCANCEL'].fields_by_name['market_order']._serialized_options = b'\310\336\037\001'
  _globals['_DERIVATIVEMARKETORDERCANCEL'].fields_by_name['cancel_quantity']._loaded_options = None
  _globals['_DERIVATIVEMARKETORDERCANCEL'].fields_by_name['cancel_quantity']._serialized_options = b'\310\336\037\000\332\336\037\033cosmossdk.io/math.LegacyDec'
  _globals['_EVENTCANCELDERIVATIVEORDER'].fields_by_name['limit_order']._loaded_options = None
  _globals['_EVENTCANCELDERIVATIVEORDER'].fields_by_name['limit_order']._serialized_options = b'\310\336\037\001'
  _globals['_EVENTCANCELDERIVATIVEORDER'].fields_by_name['market_order_cancel']._loaded_options = None
  _globals['_EVENTCANCELDERIVATIVEORDER'].fields_by_name['market_order_cancel']._serialized_options = b'\310\336\037\001'
  _globals['_EVENTCANCELCONDITIONALDERIVATIVEORDER'].fields_by_name['limit_order']._loaded_options = None
  _globals['_EVENTCANCELCONDITIONALDERIVATIVEORDER'].fields_by_name['limit_order']._serialized_options = b'\310\336\037\001'
  _globals['_EVENTCANCELCONDITIONALDERIVATIVEORDER'].fields_by_name['market_order']._loaded_options = None
  _globals['_EVENTCANCELCONDITIONALDERIVATIVEORDER'].fields_by_name['market_order']._serialized_options = b'\310\336\037\001'
  _globals['_EVENTGRANTACTIVATION'].fields_by_name['amount']._loaded_options = None
  _globals['_EVENTGRANTACTIVATION'].fields_by_name['amount']._serialized_options = b'\310\336\037\000\332\336\037\025cosmossdk.io/math.Int'
  _globals['_EVENTBATCHSPOTEXECUTION']._serialized_start=208
  _globals['_EVENTBATCHSPOTEXECUTION']._serialized_end=428
  _globals['_EVENTBATCHDERIVATIVEEXECUTION']._serialized_start=431
  _globals['_EVENTBATCHDERIVATIVEEXECUTION']._serialized_end=790
  _globals['_EVENTLOSTFUNDSFROMLIQUIDATION']._serialized_start=793
  _globals['_EVENTLOSTFUNDSFROMLIQUIDATION']._serialized_end=1115
  _globals['_EVENTBATCHDERIVATIVEPOSITION']._serialized_start=1118
  _globals['_EVENTBATCHDERIVATIVEPOSITION']._serialized_end=1255
  _globals['_EVENTDERIVATIVEMARKETPAUSED']._serialized_start=1258
  _globals['_EVENTDERIVATIVEMARKETPAUSED']._serialized_end=1445
  _globals['_EVENTMARKETBEYONDBANKRUPTCY']._serialized_start=1448
  _globals['_EVENTMARKETBEYONDBANKRUPTCY']._serialized_end=1591
  _globals['_EVENTALLPOSITIONSHAIRCUT']._serialized_start=1594
  _globals['_EVENTALLPOSITIONSHAIRCUT']._serialized_end=1730
  _globals['_EVENTBINARYOPTIONSMARKETUPDATE']._serialized_start=1732
  _globals['_EVENTBINARYOPTIONSMARKETUPDATE']._serialized_end=1843
  _globals['_EVENTNEWSPOTORDERS']._serialized_start=1846
  _globals['_EVENTNEWSPOTORDERS']._serialized_end=2047
  _globals['_EVENTNEWDERIVATIVEORDERS']._serialized_start=2050
  _globals['_EVENTNEWDERIVATIVEORDERS']._serialized_end=2269
  _globals['_EVENTCANCELSPOTORDER']._serialized_start=2271
  _globals['_EVENTCANCELSPOTORDER']._serialized_end=2394
  _globals['_EVENTSPOTMARKETUPDATE']._serialized_start=2396
  _globals['_EVENTSPOTMARKETUPDATE']._serialized_end=2489
  _globals['_EVENTPERPETUALMARKETUPDATE']._serialized_start=2492
  _globals['_EVENTPERPETUALMARKETUPDATE']._serialized_end=2787
  _globals['_EVENTEXPIRYFUTURESMARKETUPDATE']._serialized_start=2790
  _globals['_EVENTEXPIRYFUTURESMARKETUPDATE']._serialized_end=3018
  _globals['_EVENTPERPETUALMARKETFUNDINGUPDATE']._serialized_start=3021
  _globals['_EVENTPERPETUALMARKETFUNDINGUPDATE']._serialized_end=3353
  _globals['_EVENTSUBACCOUNTDEPOSIT']._serialized_start=3356
  _globals['_EVENTSUBACCOUNTDEPOSIT']._serialized_end=3507
  _globals['_EVENTSUBACCOUNTWITHDRAW']._serialized_start=3510
  _globals['_EVENTSUBACCOUNTWITHDRAW']._serialized_end=3662
  _globals['_EVENTSUBACCOUNTBALANCETRANSFER']._serialized_start=3665
  _globals['_EVENTSUBACCOUNTBALANCETRANSFER']._serialized_end=3842
  _globals['_EVENTBATCHDEPOSITUPDATE']._serialized_start=3844
  _globals['_EVENTBATCHDEPOSITUPDATE']._serialized_end=3953
  _globals['_DERIVATIVEMARKETORDERCANCEL']._serialized_start=3956
  _globals['_DERIVATIVEMARKETORDERCANCEL']._serialized_end=4155
  _globals['_EVENTCANCELDERIVATIVEORDER']._serialized_start=4158
  _globals['_EVENTCANCELDERIVATIVEORDER']._serialized_end=4453
  _globals['_EVENTFEEDISCOUNTSCHEDULE']._serialized_start=4455
  _globals['_EVENTFEEDISCOUNTSCHEDULE']._serialized_end=4558
  _globals['_EVENTTRADINGREWARDCAMPAIGNUPDATE']._serialized_start=4561
  _globals['_EVENTTRADINGREWARDCAMPAIGNUPDATE']._serialized_end=4787
  _globals['_EVENTTRADINGREWARDDISTRIBUTION']._serialized_start=4789
  _globals['_EVENTTRADINGREWARDDISTRIBUTION']._serialized_end=4906
  _globals['_EVENTNEWCONDITIONALDERIVATIVEORDER']._serialized_start=4909
  _globals['_EVENTNEWCONDITIONALDERIVATIVEORDER']._serialized_end=5090
  _globals['_EVENTCANCELCONDITIONALDERIVATIVEORDER']._serialized_start=5093
  _globals['_EVENTCANCELCONDITIONALDERIVATIVEORDER']._serialized_end=5380
  _globals['_EVENTCONDITIONALDERIVATIVEORDERTRIGGER']._serialized_start=5383
  _globals['_EVENTCONDITIONALDERIVATIVEORDERTRIGGER']._serialized_end=5634
  _globals['_EVENTORDERFAIL']._serialized_start=5636
  _globals['_EVENTORDERFAIL']._serialized_end=5744
  _globals['_EVENTATOMICMARKETORDERFEEMULTIPLIERSUPDATED']._serialized_start=5747
  _globals['_EVENTATOMICMARKETORDERFEEMULTIPLIERSUPDATED']._serialized_end=5895
  _globals['_EVENTORDERBOOKUPDATE']._serialized_start=5898
  _globals['_EVENTORDERBOOKUPDATE']._serialized_end=6092
  _globals['_ORDERBOOKUPDATE']._serialized_start=6094
  _globals['_ORDERBOOKUPDATE']._serialized_end=6198
  _globals['_ORDERBOOK']._serialized_start=6201
  _globals['_ORDERBOOK']._serialized_end=6375
  _globals['_EVENTGRANTAUTHORIZATIONS']._serialized_start=6377
  _globals['_EVENTGRANTAUTHORIZATIONS']._serialized_end=6501
  _globals['_EVENTGRANTACTIVATION']._serialized_start=6504
  _globals['_EVENTGRANTACTIVATION']._serialized_end=6633
  _globals['_EVENTINVALIDGRANT']._serialized_start=6635
  _globals['_EVENTINVALIDGRANT']._serialized_end=6706
  _globals['_EVENTORDERCANCELFAIL']._serialized_start=6709
  _globals['_EVENTORDERCANCELFAIL']._serialized_end=6880
# @@protoc_insertion_point(module_scope)
