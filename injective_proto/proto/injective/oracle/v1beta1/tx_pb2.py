from injective_proto.proto.descriptor import INJECTIVE_DESCRIPTOR_POOL
# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: injective/oracle/v1beta1/tx.proto
# Protobuf Python Version: 5.26.1
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from injective_proto.proto.gogoproto import gogo_pb2 as gogoproto_dot_gogo__pb2
from injective_proto.proto.injective.oracle.v1beta1 import oracle_pb2 as injective_dot_oracle_dot_v1beta1_dot_oracle__pb2
from injective_proto.proto.cosmos.msg.v1 import msg_pb2 as cosmos_dot_msg_dot_v1_dot_msg__pb2
from injective_proto.proto.cosmos_proto import cosmos_pb2 as cosmos__proto_dot_cosmos__pb2
from injective_proto.proto.amino import amino_pb2 as amino_dot_amino__pb2


DESCRIPTOR = INJECTIVE_DESCRIPTOR_POOL.AddSerializedFile(b'\n!injective/oracle/v1beta1/tx.proto\x12\x18injective.oracle.v1beta1\x1a\x14gogoproto/gogo.proto\x1a%injective/oracle/v1beta1/oracle.proto\x1a\x17\x63osmos/msg/v1/msg.proto\x1a\x19\x63osmos_proto/cosmos.proto\x1a\x11\x61mino/amino.proto\"\xda\x01\n\x16MsgRelayProviderPrices\x12\x16\n\x06sender\x18\x01 \x01(\tR\x06sender\x12\x1a\n\x08provider\x18\x02 \x01(\tR\x08provider\x12\x18\n\x07symbols\x18\x03 \x03(\tR\x07symbols\x12;\n\x06prices\x18\x04 \x03(\tB#\xc8\xde\x1f\x00\xda\xde\x1f\x1b\x63osmossdk.io/math.LegacyDecR\x06prices:5\x88\xa0\x1f\x00\xe8\xa0\x1f\x00\x82\xe7\xb0*\x06sender\x8a\xe7\xb0*\x1doracle/MsgRelayProviderPrices\" \n\x1eMsgRelayProviderPricesResponse\"\xcc\x01\n\x16MsgRelayPriceFeedPrice\x12\x16\n\x06sender\x18\x01 \x01(\tR\x06sender\x12\x12\n\x04\x62\x61se\x18\x02 \x03(\tR\x04\x62\x61se\x12\x14\n\x05quote\x18\x03 \x03(\tR\x05quote\x12\x39\n\x05price\x18\x04 \x03(\tB#\xc8\xde\x1f\x00\xda\xde\x1f\x1b\x63osmossdk.io/math.LegacyDecR\x05price:5\x88\xa0\x1f\x00\xe8\xa0\x1f\x00\x82\xe7\xb0*\x06sender\x8a\xe7\xb0*\x1doracle/MsgRelayPriceFeedPrice\" \n\x1eMsgRelayPriceFeedPriceResponse\"\xcd\x01\n\x11MsgRelayBandRates\x12\x18\n\x07relayer\x18\x01 \x01(\tR\x07relayer\x12\x18\n\x07symbols\x18\x02 \x03(\tR\x07symbols\x12\x14\n\x05rates\x18\x03 \x03(\x04R\x05rates\x12#\n\rresolve_times\x18\x04 \x03(\x04R\x0cresolveTimes\x12\x1e\n\nrequestIDs\x18\x05 \x03(\x04R\nrequestIDs:)\x82\xe7\xb0*\x07relayer\x8a\xe7\xb0*\x18oracle/MsgRelayBandRates\"\x1b\n\x19MsgRelayBandRatesResponse\"\xa7\x01\n\x18MsgRelayCoinbaseMessages\x12\x16\n\x06sender\x18\x01 \x01(\tR\x06sender\x12\x1a\n\x08messages\x18\x02 \x03(\x0cR\x08messages\x12\x1e\n\nsignatures\x18\x03 \x03(\x0cR\nsignatures:7\x88\xa0\x1f\x00\xe8\xa0\x1f\x00\x82\xe7\xb0*\x06sender\x8a\xe7\xb0*\x1foracle/MsgRelayCoinbaseMessages\"\"\n MsgRelayCoinbaseMessagesResponse\"\x88\x01\n\x13MsgRelayStorkPrices\x12\x16\n\x06sender\x18\x01 \x01(\tR\x06sender\x12\x44\n\x0b\x61sset_pairs\x18\x02 \x03(\x0b\x32#.injective.oracle.v1beta1.AssetPairR\nassetPairs:\x13\x88\xa0\x1f\x00\xe8\xa0\x1f\x00\x82\xe7\xb0*\x06sender\"\x1d\n\x1bMsgRelayStorkPricesResponse\"\x86\x01\n\x16MsgRequestBandIBCRates\x12\x16\n\x06sender\x18\x01 \x01(\tR\x06sender\x12\x1d\n\nrequest_id\x18\x02 \x01(\x04R\trequestId:5\x88\xa0\x1f\x00\xe8\xa0\x1f\x00\x82\xe7\xb0*\x06sender\x8a\xe7\xb0*\x1doracle/MsgRequestBandIBCRates\" \n\x1eMsgRequestBandIBCRatesResponse\"\xba\x01\n\x12MsgRelayPythPrices\x12\x16\n\x06sender\x18\x01 \x01(\tR\x06sender\x12Y\n\x12price_attestations\x18\x02 \x03(\x0b\x32*.injective.oracle.v1beta1.PriceAttestationR\x11priceAttestations:1\x88\xa0\x1f\x00\xe8\xa0\x1f\x00\x82\xe7\xb0*\x06sender\x8a\xe7\xb0*\x19oracle/MsgRelayPythPrices\"\x1c\n\x1aMsgRelayPythPricesResponse\"\xb4\x01\n\x0fMsgUpdateParams\x12\x36\n\tauthority\x18\x01 \x01(\tB\x18\xd2\xb4-\x14\x63osmos.AddressStringR\tauthority\x12>\n\x06params\x18\x02 \x01(\x0b\x32 .injective.oracle.v1beta1.ParamsB\x04\xc8\xde\x1f\x00R\x06params:)\x82\xe7\xb0*\tauthority\x8a\xe7\xb0*\x16oracle/MsgUpdateParams\"\x19\n\x17MsgUpdateParamsResponse2\xf6\x07\n\x03Msg\x12\x81\x01\n\x13RelayProviderPrices\x12\x30.injective.oracle.v1beta1.MsgRelayProviderPrices\x1a\x38.injective.oracle.v1beta1.MsgRelayProviderPricesResponse\x12\x81\x01\n\x13RelayPriceFeedPrice\x12\x30.injective.oracle.v1beta1.MsgRelayPriceFeedPrice\x1a\x38.injective.oracle.v1beta1.MsgRelayPriceFeedPriceResponse\x12r\n\x0eRelayBandRates\x12+.injective.oracle.v1beta1.MsgRelayBandRates\x1a\x33.injective.oracle.v1beta1.MsgRelayBandRatesResponse\x12\x81\x01\n\x13RequestBandIBCRates\x12\x30.injective.oracle.v1beta1.MsgRequestBandIBCRates\x1a\x38.injective.oracle.v1beta1.MsgRequestBandIBCRatesResponse\x12\x87\x01\n\x15RelayCoinbaseMessages\x12\x32.injective.oracle.v1beta1.MsgRelayCoinbaseMessages\x1a:.injective.oracle.v1beta1.MsgRelayCoinbaseMessagesResponse\x12y\n\x11RelayStorkMessage\x12-.injective.oracle.v1beta1.MsgRelayStorkPrices\x1a\x35.injective.oracle.v1beta1.MsgRelayStorkPricesResponse\x12u\n\x0fRelayPythPrices\x12,.injective.oracle.v1beta1.MsgRelayPythPrices\x1a\x34.injective.oracle.v1beta1.MsgRelayPythPricesResponse\x12l\n\x0cUpdateParams\x12).injective.oracle.v1beta1.MsgUpdateParams\x1a\x31.injective.oracle.v1beta1.MsgUpdateParamsResponse\x1a\x05\x80\xe7\xb0*\x01\x42\xf7\x01\n\x1c\x63om.injective.oracle.v1beta1B\x07TxProtoP\x01ZLgithub.com/InjectiveLabs/injective-core/injective-chain/modules/oracle/types\xa2\x02\x03IOX\xaa\x02\x18Injective.Oracle.V1beta1\xca\x02\x18Injective\\Oracle\\V1beta1\xe2\x02$Injective\\Oracle\\V1beta1\\GPBMetadata\xea\x02\x1aInjective::Oracle::V1beta1b\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'injective.oracle.v1beta1.tx_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'\n\034com.injective.oracle.v1beta1B\007TxProtoP\001ZLgithub.com/InjectiveLabs/injective-core/injective-chain/modules/oracle/types\242\002\003IOX\252\002\030Injective.Oracle.V1beta1\312\002\030Injective\\Oracle\\V1beta1\342\002$Injective\\Oracle\\V1beta1\\GPBMetadata\352\002\032Injective::Oracle::V1beta1'
  _globals['_MSGRELAYPROVIDERPRICES'].fields_by_name['prices']._loaded_options = None
  _globals['_MSGRELAYPROVIDERPRICES'].fields_by_name['prices']._serialized_options = b'\310\336\037\000\332\336\037\033cosmossdk.io/math.LegacyDec'
  _globals['_MSGRELAYPROVIDERPRICES']._loaded_options = None
  _globals['_MSGRELAYPROVIDERPRICES']._serialized_options = b'\210\240\037\000\350\240\037\000\202\347\260*\006sender\212\347\260*\035oracle/MsgRelayProviderPrices'
  _globals['_MSGRELAYPRICEFEEDPRICE'].fields_by_name['price']._loaded_options = None
  _globals['_MSGRELAYPRICEFEEDPRICE'].fields_by_name['price']._serialized_options = b'\310\336\037\000\332\336\037\033cosmossdk.io/math.LegacyDec'
  _globals['_MSGRELAYPRICEFEEDPRICE']._loaded_options = None
  _globals['_MSGRELAYPRICEFEEDPRICE']._serialized_options = b'\210\240\037\000\350\240\037\000\202\347\260*\006sender\212\347\260*\035oracle/MsgRelayPriceFeedPrice'
  _globals['_MSGRELAYBANDRATES']._loaded_options = None
  _globals['_MSGRELAYBANDRATES']._serialized_options = b'\202\347\260*\007relayer\212\347\260*\030oracle/MsgRelayBandRates'
  _globals['_MSGRELAYCOINBASEMESSAGES']._loaded_options = None
  _globals['_MSGRELAYCOINBASEMESSAGES']._serialized_options = b'\210\240\037\000\350\240\037\000\202\347\260*\006sender\212\347\260*\037oracle/MsgRelayCoinbaseMessages'
  _globals['_MSGRELAYSTORKPRICES']._loaded_options = None
  _globals['_MSGRELAYSTORKPRICES']._serialized_options = b'\210\240\037\000\350\240\037\000\202\347\260*\006sender'
  _globals['_MSGREQUESTBANDIBCRATES']._loaded_options = None
  _globals['_MSGREQUESTBANDIBCRATES']._serialized_options = b'\210\240\037\000\350\240\037\000\202\347\260*\006sender\212\347\260*\035oracle/MsgRequestBandIBCRates'
  _globals['_MSGRELAYPYTHPRICES']._loaded_options = None
  _globals['_MSGRELAYPYTHPRICES']._serialized_options = b'\210\240\037\000\350\240\037\000\202\347\260*\006sender\212\347\260*\031oracle/MsgRelayPythPrices'
  _globals['_MSGUPDATEPARAMS'].fields_by_name['authority']._loaded_options = None
  _globals['_MSGUPDATEPARAMS'].fields_by_name['authority']._serialized_options = b'\322\264-\024cosmos.AddressString'
  _globals['_MSGUPDATEPARAMS'].fields_by_name['params']._loaded_options = None
  _globals['_MSGUPDATEPARAMS'].fields_by_name['params']._serialized_options = b'\310\336\037\000'
  _globals['_MSGUPDATEPARAMS']._loaded_options = None
  _globals['_MSGUPDATEPARAMS']._serialized_options = b'\202\347\260*\tauthority\212\347\260*\026oracle/MsgUpdateParams'
  _globals['_MSG']._loaded_options = None
  _globals['_MSG']._serialized_options = b'\200\347\260*\001'
  _globals['_MSGRELAYPROVIDERPRICES']._serialized_start=196
  _globals['_MSGRELAYPROVIDERPRICES']._serialized_end=414
  _globals['_MSGRELAYPROVIDERPRICESRESPONSE']._serialized_start=416
  _globals['_MSGRELAYPROVIDERPRICESRESPONSE']._serialized_end=448
  _globals['_MSGRELAYPRICEFEEDPRICE']._serialized_start=451
  _globals['_MSGRELAYPRICEFEEDPRICE']._serialized_end=655
  _globals['_MSGRELAYPRICEFEEDPRICERESPONSE']._serialized_start=657
  _globals['_MSGRELAYPRICEFEEDPRICERESPONSE']._serialized_end=689
  _globals['_MSGRELAYBANDRATES']._serialized_start=692
  _globals['_MSGRELAYBANDRATES']._serialized_end=897
  _globals['_MSGRELAYBANDRATESRESPONSE']._serialized_start=899
  _globals['_MSGRELAYBANDRATESRESPONSE']._serialized_end=926
  _globals['_MSGRELAYCOINBASEMESSAGES']._serialized_start=929
  _globals['_MSGRELAYCOINBASEMESSAGES']._serialized_end=1096
  _globals['_MSGRELAYCOINBASEMESSAGESRESPONSE']._serialized_start=1098
  _globals['_MSGRELAYCOINBASEMESSAGESRESPONSE']._serialized_end=1132
  _globals['_MSGRELAYSTORKPRICES']._serialized_start=1135
  _globals['_MSGRELAYSTORKPRICES']._serialized_end=1271
  _globals['_MSGRELAYSTORKPRICESRESPONSE']._serialized_start=1273
  _globals['_MSGRELAYSTORKPRICESRESPONSE']._serialized_end=1302
  _globals['_MSGREQUESTBANDIBCRATES']._serialized_start=1305
  _globals['_MSGREQUESTBANDIBCRATES']._serialized_end=1439
  _globals['_MSGREQUESTBANDIBCRATESRESPONSE']._serialized_start=1441
  _globals['_MSGREQUESTBANDIBCRATESRESPONSE']._serialized_end=1473
  _globals['_MSGRELAYPYTHPRICES']._serialized_start=1476
  _globals['_MSGRELAYPYTHPRICES']._serialized_end=1662
  _globals['_MSGRELAYPYTHPRICESRESPONSE']._serialized_start=1664
  _globals['_MSGRELAYPYTHPRICESRESPONSE']._serialized_end=1692
  _globals['_MSGUPDATEPARAMS']._serialized_start=1695
  _globals['_MSGUPDATEPARAMS']._serialized_end=1875
  _globals['_MSGUPDATEPARAMSRESPONSE']._serialized_start=1877
  _globals['_MSGUPDATEPARAMSRESPONSE']._serialized_end=1902
  _globals['_MSG']._serialized_start=1905
  _globals['_MSG']._serialized_end=2919
# @@protoc_insertion_point(module_scope)
