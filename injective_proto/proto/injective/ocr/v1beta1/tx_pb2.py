from injective_proto.proto.descriptor import INJECTIVE_DESCRIPTOR_POOL
# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: injective/ocr/v1beta1/tx.proto
# Protobuf Python Version: 5.26.1
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from injective_proto.proto.cosmos.base.v1beta1 import coin_pb2 as cosmos_dot_base_dot_v1beta1_dot_coin__pb2
from injective_proto.proto.cosmos.msg.v1 import msg_pb2 as cosmos_dot_msg_dot_v1_dot_msg__pb2
from injective_proto.proto.gogoproto import gogo_pb2 as gogoproto_dot_gogo__pb2
from injective_proto.proto.injective.ocr.v1beta1 import ocr_pb2 as injective_dot_ocr_dot_v1beta1_dot_ocr__pb2
from injective_proto.proto.cosmos_proto import cosmos_pb2 as cosmos__proto_dot_cosmos__pb2
from injective_proto.proto.amino import amino_pb2 as amino_dot_amino__pb2


DESCRIPTOR = INJECTIVE_DESCRIPTOR_POOL.AddSerializedFile(b'\n\x1einjective/ocr/v1beta1/tx.proto\x12\x15injective.ocr.v1beta1\x1a\x1e\x63osmos/base/v1beta1/coin.proto\x1a\x17\x63osmos/msg/v1/msg.proto\x1a\x14gogoproto/gogo.proto\x1a\x1finjective/ocr/v1beta1/ocr.proto\x1a\x19\x63osmos_proto/cosmos.proto\x1a\x11\x61mino/amino.proto\"\x8d\x01\n\rMsgCreateFeed\x12\x16\n\x06sender\x18\x01 \x01(\tR\x06sender\x12\x39\n\x06\x63onfig\x18\x02 \x01(\x0b\x32!.injective.ocr.v1beta1.FeedConfigR\x06\x63onfig:)\x88\xa0\x1f\x00\xe8\xa0\x1f\x00\x82\xe7\xb0*\x06sender\x8a\xe7\xb0*\x11ocr/MsgCreateFeed\"\x17\n\x15MsgCreateFeedResponse\"\xb0\x03\n\rMsgUpdateFeed\x12\x16\n\x06sender\x18\x01 \x01(\tR\x06sender\x12\x17\n\x07\x66\x65\x65\x64_id\x18\x02 \x01(\tR\x06\x66\x65\x65\x64Id\x12\x18\n\x07signers\x18\x03 \x03(\tR\x07signers\x12\"\n\x0ctransmitters\x18\x04 \x03(\tR\x0ctransmitters\x12O\n\x14link_per_observation\x18\x05 \x01(\tB\x1d\xc8\xde\x1f\x01\xda\xde\x1f\x15\x63osmossdk.io/math.IntR\x12linkPerObservation\x12Q\n\x15link_per_transmission\x18\x06 \x01(\tB\x1d\xc8\xde\x1f\x01\xda\xde\x1f\x15\x63osmossdk.io/math.IntR\x13linkPerTransmission\x12\x1d\n\nlink_denom\x18\x07 \x01(\tR\tlinkDenom\x12\x1d\n\nfeed_admin\x18\x08 \x01(\tR\tfeedAdmin\x12#\n\rbilling_admin\x18\t \x01(\tR\x0c\x62illingAdmin:)\x88\xa0\x1f\x00\xe8\xa0\x1f\x00\x82\xe7\xb0*\x06sender\x8a\xe7\xb0*\x11ocr/MsgUpdateFeed\"\x17\n\x15MsgUpdateFeedResponse\"\xbd\x02\n\x0bMsgTransmit\x12 \n\x0btransmitter\x18\x01 \x01(\tR\x0btransmitter\x12#\n\rconfig_digest\x18\x02 \x01(\x0cR\x0c\x63onfigDigest\x12\x17\n\x07\x66\x65\x65\x64_id\x18\x03 \x01(\tR\x06\x66\x65\x65\x64Id\x12\x14\n\x05\x65poch\x18\x04 \x01(\x04R\x05\x65poch\x12\x14\n\x05round\x18\x05 \x01(\x04R\x05round\x12\x1d\n\nextra_hash\x18\x06 \x01(\x0cR\textraHash\x12\x35\n\x06report\x18\x07 \x01(\x0b\x32\x1d.injective.ocr.v1beta1.ReportR\x06report\x12\x1e\n\nsignatures\x18\x08 \x03(\x0cR\nsignatures:,\x88\xa0\x1f\x00\xe8\xa0\x1f\x00\x82\xe7\xb0*\x0btransmitter\x8a\xe7\xb0*\x0focr/MsgTransmit\"\x15\n\x13MsgTransmitResponse\"\xb4\x01\n\x15MsgFundFeedRewardPool\x12\x16\n\x06sender\x18\x01 \x01(\tR\x06sender\x12\x17\n\x07\x66\x65\x65\x64_id\x18\x02 \x01(\tR\x06\x66\x65\x65\x64Id\x12\x37\n\x06\x61mount\x18\x03 \x01(\x0b\x32\x19.cosmos.base.v1beta1.CoinB\x04\xc8\xde\x1f\x00R\x06\x61mount:1\x88\xa0\x1f\x00\xe8\xa0\x1f\x00\x82\xe7\xb0*\x06sender\x8a\xe7\xb0*\x19ocr/MsgFundFeedRewardPool\"\x1f\n\x1dMsgFundFeedRewardPoolResponse\"\xbc\x01\n\x19MsgWithdrawFeedRewardPool\x12\x16\n\x06sender\x18\x01 \x01(\tR\x06sender\x12\x17\n\x07\x66\x65\x65\x64_id\x18\x02 \x01(\tR\x06\x66\x65\x65\x64Id\x12\x37\n\x06\x61mount\x18\x03 \x01(\x0b\x32\x19.cosmos.base.v1beta1.CoinB\x04\xc8\xde\x1f\x00R\x06\x61mount:5\x88\xa0\x1f\x00\xe8\xa0\x1f\x00\x82\xe7\xb0*\x06sender\x8a\xe7\xb0*\x1docr/MsgWithdrawFeedRewardPool\"#\n!MsgWithdrawFeedRewardPoolResponse\"\xa5\x01\n\x0cMsgSetPayees\x12\x16\n\x06sender\x18\x01 \x01(\tR\x06sender\x12\x17\n\x07\x66\x65\x65\x64_id\x18\x02 \x01(\tR\x06\x66\x65\x65\x64Id\x12\"\n\x0ctransmitters\x18\x03 \x03(\tR\x0ctransmitters\x12\x16\n\x06payees\x18\x04 \x03(\tR\x06payees:(\x88\xa0\x1f\x00\xe8\xa0\x1f\x00\x82\xe7\xb0*\x06sender\x8a\xe7\xb0*\x10ocr/MsgSetPayees\"\x16\n\x14MsgSetPayeesResponse\"\xb7\x01\n\x14MsgTransferPayeeship\x12\x16\n\x06sender\x18\x01 \x01(\tR\x06sender\x12 \n\x0btransmitter\x18\x02 \x01(\tR\x0btransmitter\x12\x17\n\x07\x66\x65\x65\x64_id\x18\x03 \x01(\tR\x06\x66\x65\x65\x64Id\x12\x1a\n\x08proposed\x18\x04 \x01(\tR\x08proposed:0\x88\xa0\x1f\x00\xe8\xa0\x1f\x00\x82\xe7\xb0*\x06sender\x8a\xe7\xb0*\x18ocr/MsgTransferPayeeship\"\x1e\n\x1cMsgTransferPayeeshipResponse\"\x9a\x01\n\x12MsgAcceptPayeeship\x12\x14\n\x05payee\x18\x01 \x01(\tR\x05payee\x12 \n\x0btransmitter\x18\x02 \x01(\tR\x0btransmitter\x12\x17\n\x07\x66\x65\x65\x64_id\x18\x03 \x01(\tR\x06\x66\x65\x65\x64Id:3\x88\xa0\x1f\x00\xe8\xa0\x1f\x00\x82\xe7\xb0*\x0btransmitter\x8a\xe7\xb0*\x16ocr/MsgAcceptPayeeship\"\x1c\n\x1aMsgAcceptPayeeshipResponse\"\xae\x01\n\x0fMsgUpdateParams\x12\x36\n\tauthority\x18\x01 \x01(\tB\x18\xd2\xb4-\x14\x63osmos.AddressStringR\tauthority\x12;\n\x06params\x18\x02 \x01(\x0b\x32\x1d.injective.ocr.v1beta1.ParamsB\x04\xc8\xde\x1f\x00R\x06params:&\x82\xe7\xb0*\tauthority\x8a\xe7\xb0*\x13ocr/MsgUpdateParams\"\x19\n\x17MsgUpdateParamsResponse2\xdc\x07\n\x03Msg\x12`\n\nCreateFeed\x12$.injective.ocr.v1beta1.MsgCreateFeed\x1a,.injective.ocr.v1beta1.MsgCreateFeedResponse\x12`\n\nUpdateFeed\x12$.injective.ocr.v1beta1.MsgUpdateFeed\x1a,.injective.ocr.v1beta1.MsgUpdateFeedResponse\x12Z\n\x08Transmit\x12\".injective.ocr.v1beta1.MsgTransmit\x1a*.injective.ocr.v1beta1.MsgTransmitResponse\x12x\n\x12\x46undFeedRewardPool\x12,.injective.ocr.v1beta1.MsgFundFeedRewardPool\x1a\x34.injective.ocr.v1beta1.MsgFundFeedRewardPoolResponse\x12\x84\x01\n\x16WithdrawFeedRewardPool\x12\x30.injective.ocr.v1beta1.MsgWithdrawFeedRewardPool\x1a\x38.injective.ocr.v1beta1.MsgWithdrawFeedRewardPoolResponse\x12]\n\tSetPayees\x12#.injective.ocr.v1beta1.MsgSetPayees\x1a+.injective.ocr.v1beta1.MsgSetPayeesResponse\x12u\n\x11TransferPayeeship\x12+.injective.ocr.v1beta1.MsgTransferPayeeship\x1a\x33.injective.ocr.v1beta1.MsgTransferPayeeshipResponse\x12o\n\x0f\x41\x63\x63\x65ptPayeeship\x12).injective.ocr.v1beta1.MsgAcceptPayeeship\x1a\x31.injective.ocr.v1beta1.MsgAcceptPayeeshipResponse\x12\x66\n\x0cUpdateParams\x12&.injective.ocr.v1beta1.MsgUpdateParams\x1a..injective.ocr.v1beta1.MsgUpdateParamsResponse\x1a\x05\x80\xe7\xb0*\x01\x42\xe5\x01\n\x19\x63om.injective.ocr.v1beta1B\x07TxProtoP\x01ZIgithub.com/InjectiveLabs/injective-core/injective-chain/modules/ocr/types\xa2\x02\x03IOX\xaa\x02\x15Injective.Ocr.V1beta1\xca\x02\x15Injective\\Ocr\\V1beta1\xe2\x02!Injective\\Ocr\\V1beta1\\GPBMetadata\xea\x02\x17Injective::Ocr::V1beta1b\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'injective.ocr.v1beta1.tx_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'\n\031com.injective.ocr.v1beta1B\007TxProtoP\001ZIgithub.com/InjectiveLabs/injective-core/injective-chain/modules/ocr/types\242\002\003IOX\252\002\025Injective.Ocr.V1beta1\312\002\025Injective\\Ocr\\V1beta1\342\002!Injective\\Ocr\\V1beta1\\GPBMetadata\352\002\027Injective::Ocr::V1beta1'
  _globals['_MSGCREATEFEED']._loaded_options = None
  _globals['_MSGCREATEFEED']._serialized_options = b'\210\240\037\000\350\240\037\000\202\347\260*\006sender\212\347\260*\021ocr/MsgCreateFeed'
  _globals['_MSGUPDATEFEED'].fields_by_name['link_per_observation']._loaded_options = None
  _globals['_MSGUPDATEFEED'].fields_by_name['link_per_observation']._serialized_options = b'\310\336\037\001\332\336\037\025cosmossdk.io/math.Int'
  _globals['_MSGUPDATEFEED'].fields_by_name['link_per_transmission']._loaded_options = None
  _globals['_MSGUPDATEFEED'].fields_by_name['link_per_transmission']._serialized_options = b'\310\336\037\001\332\336\037\025cosmossdk.io/math.Int'
  _globals['_MSGUPDATEFEED']._loaded_options = None
  _globals['_MSGUPDATEFEED']._serialized_options = b'\210\240\037\000\350\240\037\000\202\347\260*\006sender\212\347\260*\021ocr/MsgUpdateFeed'
  _globals['_MSGTRANSMIT']._loaded_options = None
  _globals['_MSGTRANSMIT']._serialized_options = b'\210\240\037\000\350\240\037\000\202\347\260*\013transmitter\212\347\260*\017ocr/MsgTransmit'
  _globals['_MSGFUNDFEEDREWARDPOOL'].fields_by_name['amount']._loaded_options = None
  _globals['_MSGFUNDFEEDREWARDPOOL'].fields_by_name['amount']._serialized_options = b'\310\336\037\000'
  _globals['_MSGFUNDFEEDREWARDPOOL']._loaded_options = None
  _globals['_MSGFUNDFEEDREWARDPOOL']._serialized_options = b'\210\240\037\000\350\240\037\000\202\347\260*\006sender\212\347\260*\031ocr/MsgFundFeedRewardPool'
  _globals['_MSGWITHDRAWFEEDREWARDPOOL'].fields_by_name['amount']._loaded_options = None
  _globals['_MSGWITHDRAWFEEDREWARDPOOL'].fields_by_name['amount']._serialized_options = b'\310\336\037\000'
  _globals['_MSGWITHDRAWFEEDREWARDPOOL']._loaded_options = None
  _globals['_MSGWITHDRAWFEEDREWARDPOOL']._serialized_options = b'\210\240\037\000\350\240\037\000\202\347\260*\006sender\212\347\260*\035ocr/MsgWithdrawFeedRewardPool'
  _globals['_MSGSETPAYEES']._loaded_options = None
  _globals['_MSGSETPAYEES']._serialized_options = b'\210\240\037\000\350\240\037\000\202\347\260*\006sender\212\347\260*\020ocr/MsgSetPayees'
  _globals['_MSGTRANSFERPAYEESHIP']._loaded_options = None
  _globals['_MSGTRANSFERPAYEESHIP']._serialized_options = b'\210\240\037\000\350\240\037\000\202\347\260*\006sender\212\347\260*\030ocr/MsgTransferPayeeship'
  _globals['_MSGACCEPTPAYEESHIP']._loaded_options = None
  _globals['_MSGACCEPTPAYEESHIP']._serialized_options = b'\210\240\037\000\350\240\037\000\202\347\260*\013transmitter\212\347\260*\026ocr/MsgAcceptPayeeship'
  _globals['_MSGUPDATEPARAMS'].fields_by_name['authority']._loaded_options = None
  _globals['_MSGUPDATEPARAMS'].fields_by_name['authority']._serialized_options = b'\322\264-\024cosmos.AddressString'
  _globals['_MSGUPDATEPARAMS'].fields_by_name['params']._loaded_options = None
  _globals['_MSGUPDATEPARAMS'].fields_by_name['params']._serialized_options = b'\310\336\037\000'
  _globals['_MSGUPDATEPARAMS']._loaded_options = None
  _globals['_MSGUPDATEPARAMS']._serialized_options = b'\202\347\260*\tauthority\212\347\260*\023ocr/MsgUpdateParams'
  _globals['_MSG']._loaded_options = None
  _globals['_MSG']._serialized_options = b'\200\347\260*\001'
  _globals['_MSGCREATEFEED']._serialized_start=216
  _globals['_MSGCREATEFEED']._serialized_end=357
  _globals['_MSGCREATEFEEDRESPONSE']._serialized_start=359
  _globals['_MSGCREATEFEEDRESPONSE']._serialized_end=382
  _globals['_MSGUPDATEFEED']._serialized_start=385
  _globals['_MSGUPDATEFEED']._serialized_end=817
  _globals['_MSGUPDATEFEEDRESPONSE']._serialized_start=819
  _globals['_MSGUPDATEFEEDRESPONSE']._serialized_end=842
  _globals['_MSGTRANSMIT']._serialized_start=845
  _globals['_MSGTRANSMIT']._serialized_end=1162
  _globals['_MSGTRANSMITRESPONSE']._serialized_start=1164
  _globals['_MSGTRANSMITRESPONSE']._serialized_end=1185
  _globals['_MSGFUNDFEEDREWARDPOOL']._serialized_start=1188
  _globals['_MSGFUNDFEEDREWARDPOOL']._serialized_end=1368
  _globals['_MSGFUNDFEEDREWARDPOOLRESPONSE']._serialized_start=1370
  _globals['_MSGFUNDFEEDREWARDPOOLRESPONSE']._serialized_end=1401
  _globals['_MSGWITHDRAWFEEDREWARDPOOL']._serialized_start=1404
  _globals['_MSGWITHDRAWFEEDREWARDPOOL']._serialized_end=1592
  _globals['_MSGWITHDRAWFEEDREWARDPOOLRESPONSE']._serialized_start=1594
  _globals['_MSGWITHDRAWFEEDREWARDPOOLRESPONSE']._serialized_end=1629
  _globals['_MSGSETPAYEES']._serialized_start=1632
  _globals['_MSGSETPAYEES']._serialized_end=1797
  _globals['_MSGSETPAYEESRESPONSE']._serialized_start=1799
  _globals['_MSGSETPAYEESRESPONSE']._serialized_end=1821
  _globals['_MSGTRANSFERPAYEESHIP']._serialized_start=1824
  _globals['_MSGTRANSFERPAYEESHIP']._serialized_end=2007
  _globals['_MSGTRANSFERPAYEESHIPRESPONSE']._serialized_start=2009
  _globals['_MSGTRANSFERPAYEESHIPRESPONSE']._serialized_end=2039
  _globals['_MSGACCEPTPAYEESHIP']._serialized_start=2042
  _globals['_MSGACCEPTPAYEESHIP']._serialized_end=2196
  _globals['_MSGACCEPTPAYEESHIPRESPONSE']._serialized_start=2198
  _globals['_MSGACCEPTPAYEESHIPRESPONSE']._serialized_end=2226
  _globals['_MSGUPDATEPARAMS']._serialized_start=2229
  _globals['_MSGUPDATEPARAMS']._serialized_end=2403
  _globals['_MSGUPDATEPARAMSRESPONSE']._serialized_start=2405
  _globals['_MSGUPDATEPARAMSRESPONSE']._serialized_end=2430
  _globals['_MSG']._serialized_start=2433
  _globals['_MSG']._serialized_end=3421
# @@protoc_insertion_point(module_scope)